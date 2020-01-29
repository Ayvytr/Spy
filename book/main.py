import time

from book.DangdangBook import DangdangBook
from book.DoubanBook import DoubanBook
from book.JdBook import JdBook


class BookSpy:
    def __init__(self, key):
        self.key = key

        self.douban_book = DoubanBook()
        self.dangdang_book = DangdangBook()
        self.jd_book = JdBook()

    def search(self):
        # self.douban_book.search(self.key)
        # self.dangdang_book.search(self.key)
        self.jd_book.search(self.key)

    def show(self):
        # self.douban_book.show()
        # self.dangdang_book.show()
        self.jd_book.show()
        pass

    def save(self):
        pass


def main():
    bookSpy = BookSpy("情商")
    bookSpy.search()
    bookSpy.show()

    time.sleep(1000)


if __name__ == '__main__':
    main()