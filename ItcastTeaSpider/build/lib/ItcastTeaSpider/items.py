# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItcastteaspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 老师姓名
    name = scrapy.Field()
    # 讲师等级
    level = scrapy.Field()
    # 讲师描述
    info = scrapy.Field()

class TencentItem(scrapy.Item):
    # 职位列表页
    # 职位名称
    name = scrapy.Field()
    # 详情链接
    detailLink = scrapy.Field()
    # 职位信息
    positionInfo = scrapy.Field()
    # 需要人数
    peopleNumber = scrapy.Field()
    # 工作地址
    workLocation = scrapy.Field()
    # 发布时间
    publishTime = scrapy.Field()


class PositionItem(scrapy.Item):
    # 职位详情页
    # 职位详情页链接
    position_link=scrapy.Field()
    # 职位职责
    position_zhize=scrapy.Field()
    # 职位要求
    position_yaoqiu=scrapy.Field()