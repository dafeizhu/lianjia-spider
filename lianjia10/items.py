# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Lianjia10Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义变量
    title = scrapy.Field()
    detail_link = scrapy.Field()
    prize = scrapy.Field()
    time = scrapy.Field()

    content = scrapy.Field()
    location = scrapy.Field()

    # area = scrapy.Field()

