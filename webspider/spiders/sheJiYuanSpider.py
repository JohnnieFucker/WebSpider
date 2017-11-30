# -*- coding: utf-8 -*-
import scrapy
from webspider.items import SheJiYuanItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class SheJiYuanSpider(scrapy.Spider):
    name = 'SheJiYuanSpider'
    allowed_domains = ['qieta.com']
    start_urls = []
    headers = {
        'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
        'Accept-Encoding': 'deflate, br',
        'Conection': 'keep-alive'}

    def start_requests(self):
        url_head = 'http://old.qieta.com/engineering/show-'
        for i in range(1, 40002):
            url = url_head + '%s.html' % i
            self.start_urls.append(url)
        for url in self.start_urls:
            print url
            yield scrapy.Request(url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        item = SheJiYuanItem()

        content = response.xpath('//div[@class="content"]/div/text()').extract()
        name = response.xpath('//h1[@class="title"]/text()').extract()[0]
        name = name[:name.index('（')]
        item['name'] = name
        item['foundTime'] = content[1][content[1].index('：')+1:]
        item['type'] = content[2][content[2].index('：')+1:]
        item['area'] = content[3][content[3].index('：')+1:]
        item['address'] = content[4][content[4].index('：')+1:]
        item['contacts'] = content[6][content[6].index('：')+1:]
        item['tel'] = content[7][content[7].index('：')+1:]
        yield item

