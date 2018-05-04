# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    room_link = scrapy.Field()
    image_src = scrapy.Field()
    nick_name = scrapy.Field()
    city = scrapy.Field()
    image_path = scrapy.Field()
    utc_time = scrapy.Field()
    source = scrapy.Field()

