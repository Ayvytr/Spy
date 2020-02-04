import asyncio
import os
import threading
import time
import traceback
import urllib
from abc import abstractmethod

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from book import source


class BookThread(threading.Thread):
    def __init__(self, key, list):
        super().__init__()
        self.max_page = 1
        self.key = key
        self.loop = asyncio.new_event_loop()
        self.browser = None
        self.list = list
        # self.source = thread_name
        # self.page_size = page_size
        # self.url = url

    def run(self) -> None:
        tasks = [self.search(self.getUrl(i)) for i in range(self.max_page)]
        self.loop.run_until_complete(asyncio.wait(tasks))

        if self.browser is not None:
            self.browser.close()
        self.loop.close()

    @abstractmethod
    async def search(self, url):
        pass

    @abstractmethod
    def getUrl(self, current_page):
        pass

    @abstractmethod
    def parseResponse(self, text):
        pass


class DoubanThread(BookThread):
    def __init__(self, key, list):
        super().__init__(key, list)
        self.url = 'https://search.douban.com/book/subject_search?search_text={}&start={}'
        self.page_size = 15

    def run(self) -> None:
        self.browser = webdriver.Chrome()
        super().run()

    async def search(self, url):
        self.browser.get(url)
        self.parseResponse(None)

    def getUrl(self, current_page):
        url = self.url.format(urllib.parse.quote(self.key), current_page * self.page_size)
        # print(self.key, current_page, url, self.page_size)
        return url

    def parseResponse(self, text):
        books = self.browser.find_elements_by_class_name('sc-bZQynM')
        for i in books:
            img = i.find_element_by_tag_name('a').find_element_by_tag_name('img')
            title = img.get_property('alt')
            photo = img.get_property('src')

            detail = i.find_element_by_css_selector('div.meta').text
            # score = '0'
            # try:
            #     score = i.find_element_by_class_name('rating').find_element_by_class_name('rating_nums').text
            # except:
            #     pass
            #
            # book = [title, detail, photo, score]
            book = [title, detail, photo, source.DOUBAN]
            self.list.append(book)
            # print(book)

        return len(books)


class DangdangBook(BookThread):
    def __init__(self, key, list):
        super().__init__(key, list)
        self.url = 'http://search.dangdang.com/?key={}&act=input&page_index={}'
        self.page_size = 60
        self.headers = {
            'User-Agent': "User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E)"}

    async def search(self, url):
        try:
            r = requests.get(url, self.headers)
            r.raise_for_status()
            if r.encoding != r.apparent_encoding:
                r.encoding = r.apparent_encoding

            self.parseResponse(r.text)
            # if page_size < self.page_size:
            #     break
        except:
            traceback.print_exc()

    def getUrl(self, current_page):
        url = self.url.format(urllib.parse.quote(self.key), current_page + 1)
        # print(url)
        return url

    def parseResponse(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        div = soup.find('div', {'id': 'search_nature_rg'})

        li = div.ul.find_all('li')
        # print(len(li))

        for i in li:
            detail_p = i.find('p', {'class': 'detail'})

            # 获取不到data-original图片链接
            book = [i.a['title'], detail_p.string, i.a.img['src'], source.DANGDANG]
            # print(book)
            self.list.append(book)

        return len(li)


class JdBook(BookThread):
    def __init__(self, key, list):
        super().__init__(key, list)
        self.url = 'https://search.jd.com/Search?keyword={}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page={}'
        self.page_size = 60

    def run(self) -> None:
        self.browser = webdriver.Chrome()
        super().run()

    async def search(self, url):
        self.browser.get(url)
        self.parseResponse(None)

    def getUrl(self, current_page):
        url = self.url.format(urllib.parse.quote(self.key), (current_page + 1) * 2 - 1)
        # print(url)
        return url

    def parseResponse(self, text):
        js = "var q=document.documentElement.scrollTop = {}"
        self.browser.execute_script(js.format(10000))
        time.sleep(1)
        # 需要等待图片加载完成再打开
        # for n in range(10):
        #     self.browser.execute_script(js.format((n + 1) * 1000))
        #     time.sleep(0.5)

        div = self.browser.find_element_by_id('J_goodsList')
        books = div.find_element_by_tag_name('ul').find_elements_by_tag_name('li')
        # print(len(books))

        # list = []
        for i in books:
            # span p-promo-flag 广告
            try:
                i.find_element_by_css_selector('span.p-promo-flag')
                if i.text == '广告':
                    continue
            except:
                pass

            # title = i.find_element_by_css_selector('div.p-name').find_element_by_tag_name('a').get_attribute('title')
            img = i.find_element_by_css_selector('div.p-img').find_element_by_tag_name('a')
            desc = img.get_attribute('title')
            photo = img.find_element_by_tag_name('img').get_attribute('src')
            title = i.find_element_by_css_selector('div.p-name').find_element_by_tag_name('a') \
                .find_element_by_tag_name('em').text
            book = [title, desc, photo, source.JD]
            # list.append(book)
            self.list.append(book)
            # print(title, desc, photo)

        # print(len(list))
        # for i in list:
        #     print(i)
        return len(books)


class MtBook(object):
    def __init__(self, key):
        self.file_name = "book.md"
        self.key = key
        self.list = []

        self.thread_list = [
            DoubanThread(self.key, self.list),
            DangdangBook(self.key, self.list),
            JdBook(self.key, self.list)
        ]

    def search(self):
        for thread in self.thread_list:
            thread.start()

        for thread in self.thread_list:
            thread.join()

        pass

    def save(self):
        with open(self.file_name, "w+", encoding="utf-8") as file:
            file.seek(0, 0)
            file.write("## 心理学书单\n")
            if len(self.list) == 0:
                return

            # 使用pandas简单统计信息
            file.write("总计：{}本书籍\n".format(len(self.list)))

            df = pd.DataFrame(self.list, columns=["title", "detail", "img", "source"])
            file.write("来源\n")
            file.write(str(df['source'].unique()))

            file.write('\n')
            file.write(str(df['source'].value_counts()))
            file.write('\n')

            file.write("\n")
            file.write("|书名|详情|预览图|来源|\n")
            file.write(
                "| ----------------- | --------------------------------------------- | ------------------------------------- | ------------- |\n")
            file.seek(0, 2)
            for i in self.list:
                # 减少耗费流量，不进行图片加载
                # img = "" if i[2] is None else "![]({})".format(i[2])
                img = ""
                file.write("|{}|{}|{}|{}|\n".format(i[0], i[1], img, i[3]))


def main():
    begin = time.time()
    book = MtBook("情商")
    book.search()
    book.save()
    end = time.time()

    print("用时：{}".format(end - begin))
    os.startfile(book.file_name)


if __name__ == '__main__':
    main()
