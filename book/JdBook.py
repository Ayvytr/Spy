import time
import urllib

from selenium import webdriver

from book import source
from book.Book import Book


class JdBook(Book):
    def __init__(self):
        super().__init__()

        self.page_size = 60
        self.url = 'https://search.jd.com/Search?keyword={}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page={}'
        self.browser = webdriver.Chrome()
        # self.browser.maximize_window()

    def search(self, key):
        # for i in range(self.max_page):
        for i in range(1):
            self.browser.get(self.getUrl(key, i))

            js = "var q=document.documentElement.scrollTop = {}"
            self.browser.execute_script(js.format(10000))
            for n in range(10):
                self.browser.execute_script(js.format((n + 1) * 1000))
                time.sleep(0.5)

            page_size = self.parseResponse(None)
            # if page_size < self.page_size:
            #     break

    def getUrl(self, key, current_page):
        url = self.url.format(urllib.parse.quote(key), (current_page + 1) * 2 - 1)
        print(url)
        return url

    def parseResponse(self, text):
        div = self.browser.find_element_by_id('J_goodsList')
        books = div.find_element_by_tag_name('ul').find_elements_by_tag_name('li')
        print(len(books))

        list = []
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
            title = i.find_element_by_css_selector('div.p-name').find_element_by_tag_name('a')\
                .find_element_by_tag_name('em').text
            book = [title, desc, photo, source.JD]
            list.append(book)
            self.list.append(book)
            print(title, desc, photo)

        print(len(list))
        for i in list:
            print(i)
        return len(books)
