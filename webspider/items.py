# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class A51CTOBookItem(scrapy.Item):
    # define the fields for your item here like:
    content = scrapy.Field()
    pass

class SheJiYuanItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    foundTime = scrapy.Field()
    type = scrapy.Field()
    area = scrapy.Field()
    address = scrapy.Field()
    contacts = scrapy.Field()
    tel = scrapy.Field()
    pass
