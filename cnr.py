# roll.cnr.cn 央广网
import requests
from bs4 import BeautifulSoup


class Cnr:
    def __init__(self):
        self.list = []
        self.url = "http://roll.cnr.cn/"
        pass

    def queryNews(self):
        try:
            headers = {
                'User-Agent': "User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E)"}
            request = requests.get(self.url, headers=headers)
            request.raise_for_status()
            request.encoding = request.apparent_encoding
            self.parseResponse(request.text)
        except Exception as e:
            print(e)

    def showNews(self):
        for i in self.list:
            print(i[0], i[1], i[2])

    def saveNews(self):
        with open('cnr_news.txt', 'w+', encoding='utf-8') as file:
            for i in self.list:
                file.write(i[0] + ' ' + i[1] + ' ' + i[2] + '\n')

    def parseResponse(self, text):
        # print(text)

        soup = BeautifulSoup(text, 'html.parser')
        # list = soup.find_all('div', {'class': 'left', 'style': "width:610px;"})
        list = soup.find('ul', {'class':'wh740 left lh24 f14'}).find_all('li')
        for i in list:
            alist = i.div.find_all('a')
            # a = alist[1]
            # print(i.div)
            # print(i.div.a.string, i.div.a['href'])
            self.list.append([alist[0].string, alist[1].string, alist[1]['href']])

        center = soup.find('center')
        print(center, center.script)


def main():
    cnr = Cnr()
    cnr.queryNews()
    # cnr.showNews()
    # cnr.saveNews()


if __name__ == '__main__':
    main()
