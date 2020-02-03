import traceback
from abc import abstractmethod

import requests


class Book(object):
    def __init__(self):
        self.list = []
        self.headers = {
            'User-Agent': "User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E)"}
        self.max_page = 10
        self.page_size = 10
        self.file_name = "book.md"

    def search(self, key):
        try:
            for i in range(self.max_page):
                r = requests.get(self.getUrl(key, i), self.headers)
                r.raise_for_status()
                if r.encoding != r.apparent_encoding:
                    r.encoding = r.apparent_encoding

                page_size = self.parseResponse(r.text)
                if page_size < self.page_size:
                    break
        except:
            traceback.print_exc()
        pass

    def show(self):
        for i in self.list:
            print(i)

    def save(self):
        with open(self.file_name, "w+", encoding="utf-8") as file:
            file.seek(0, 0)
            file.write("## 心理学书单\n")
            if len(self.list) == 0:
                return

            file.write("|书名|详情|预览图|来源|\n")
            file.write("| ----------------- | --------------------------------------------- | ------------------------------------- | ------------- |\n")
            file.seek(0, 2)
            for i in self.list:
                img = "" if i[2] is None else "![]({})".format(i[2])
                file.write("|{}|{}|{}|{}|\n".format(i[0], i[1], img, i[3]))


    @abstractmethod
    def getUrl(self, key, current_page):
        '''
        :param key: 搜索关键字
        :param current_page: 当前页，0开始
        :return: 加了关键字和当前页的url
        '''
        pass

    @abstractmethod
    def parseResponse(self, text):
        return 0

