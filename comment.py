import json
import traceback

import requests


class Comment(object):
    def __init__(self):
        self.url = "https://api-zero.livere.com/v1/comments/list?callback=jQuery112408139205952394444_1579919509410&limit=10&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1579919509412"
        self.list = []
        self.limit = 10
        self.page = 1

    def query(self):
        try:
            hasMore = True
            while hasMore:
                url = self.url + '&offset=' + str(self.page)
                print(url)
                text = self.queryByUrl(url)
                size = self.parse(text)
                self.page += 1
                hasMore = size == self.limit

        except:
            traceback.print_exc()

        pass

    def show(self):
        print(len(self.list))
        for i in self.list:
            print(i)

    def parse(self, text):
        str = text[text.find('{'):text.rfind('}') + 1]
        json_result = json.loads(str)
        comments = json_result['results']['parents']

        for comment in comments:
            self.list.append(comment['content'])

        # print(len(self.list))
        # print(self.list)

        return len(comments)

    def queryByUrl(self, url):
        headers = {
            'User-Agent': "User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E)"}
        r = requests.get(url, headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text


def main():
    comment = Comment()
    comment.query()
    comment.show()


if __name__ == '__main__':
    main()
