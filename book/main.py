import os
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

    def save(self):
        # self.douban_book.save()
        # self.dangdang_book.save()
        self.jd_book.save()


def main():
    begin = time.time()
    bookSpy = BookSpy("情商")
    bookSpy.search()
    bookSpy.save()
    # bookSpy.show()
    end = time.time()
    print("用时：{}".format(end - begin))
    os.startfile(bookSpy.dangdang_book.file_name)
    # time.sleep(1000)

if __name__ == '__main__':
    main()