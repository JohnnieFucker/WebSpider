# -*- coding: utf-8 -*-
import scrapy
from webspider.items import A51CTOBookItem


class A51ctobookspiderSpider(scrapy.Spider):
    name = '51CTOBookSpider'
    allowed_domains = ['51cto.com']
    start_urls = []
    headers = {
        'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
        'Accept-Encoding': 'deflate, br',
        'Conection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'

    }

    def start_requests(self):
        global headers
        url_head = 'http://book.51cto.com/art/201106/2690'
        for i in range(31):
            urlSuffix = i + 36
            url = url_head + '%s.htm' % urlSuffix
            self.start_urls.append(url)
        for url in self.start_urls:
            print url
            yield scrapy.Request(url, callback=self.parse, headers=self.headers)


    def parse(self, response):
        global headers
        content = response.xpath('//div[@id="content"]').extract_first()
        fitem = A51CTOBookItem()
        fitem['content'] = content
        yield fitem
