from app.libs.req import REQ
from flask import current_app


class YuShuBook:
    """
    鱼书Api接口封装
    """
    per_page = 15
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        """
        通过isbn 检索数据
        :param isbn:
        :return:
        """
        url = cls.isbn_url.format(isbn)
        result = REQ.get(url)

        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        """
        通过关键字简述数据
        :param keyword:
        :param page:
        :return:
        """
        url = cls.keyword_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
        print(url)
        result = REQ.get(url)

        return result

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']
