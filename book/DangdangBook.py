import urllib

from bs4 import BeautifulSoup

from book import source
from book.Book import Book


class DangdangBook(Book):
    def __init__(self):
        self.url = 'http://search.dangdang.com/?key={}&act=input&page_index={}'
        self.page_size = 60
        super().__init__()

    def getUrl(self, key, current_page):
        url = self.url.format(urllib.parse.quote(key), current_page + 1)
        print(url)
        return url

    def parseResponse(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        div = soup.find('div', {'id':'search_nature_rg'})

        li = div.ul.find_all('li')
        # print(len(li))

        for i in li:
            detail_p = i.find('p', {'class':'detail'})

            # 获取不到data-original图片链接
            book = [i.a['title'], detail_p.string, i.a.img['src'], source.DANGDANG]
            self.list.append(book)

        return len(li)

