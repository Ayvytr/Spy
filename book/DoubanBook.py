import urllib
from urllib.parse import urlencode

from selenium import webdriver

from book.Book import Book


class DoubanBook(Book):
    def __init__(self):
        super().__init__()
        self.url = 'https://search.douban.com/book/subject_search?search_text={}&start={}'
        self.page_size = 15
        self.browser = webdriver.Chrome()

    def search(self, key):
        for i in range(self.max_page):
            self.browser.get(self.getUrl(key, i))

            page_size = self.parseResponse(None)
            if page_size < self.page_size:
                break

    def getUrl(self, key, current_page):
        url = self.url.format(urllib.parse.quote(key), current_page * self.page_size)
        print(key, current_page, url, self.page_size)
        return url

    def parseResponse(self, text):
        books = self.browser.find_elements_by_class_name('sc-bZQynM')
        for i in books:

            img = i.find_element_by_tag_name('a').find_element_by_tag_name('img')
            title = img.get_property('alt')
            photo = img.get_property('src')

            detail = i.find_element_by_css_selector('div.meta').text
            score = '0'
            try:
                score = i.find_element_by_class_name('rating').find_element_by_class_name('rating_nums').text
            except:
                pass

            book = [title, detail, photo, score]
            print(book)

        return len(books)
