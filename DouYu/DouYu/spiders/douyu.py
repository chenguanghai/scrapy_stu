# -*- coding: utf-8 -*-
import json

import scrapy

from ..items import DouyuItem

class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyucdn.cn']
    base_url="http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=100&offset="
    offset=0
    start_urls=[base_url+str(offset)]

    def parse(self, response):
        data_list=json.loads(response.body.decode())['data']
        # 当响应数据中的data为空列表时，表示数据提取结束，return parse方法立刻结束
        if not len(data_list):
            return

        for data in data_list:
            item=DouyuItem()
            item['room_link']="http://www.douyu.com/" + data["room_id"]
            item["image_src"] = data["vertical_src"]
            item["nick_name"] = data["nickname"]
            item["city"] = data["anchor_city"]

            yield item

        self.offset+=100
        yield scrapy.Request(self.base_url+str(self.offset),callback=self.parse)
