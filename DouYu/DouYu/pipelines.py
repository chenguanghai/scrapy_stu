# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
from datetime import datetime
from .settings import IMAGES_STORE
import logging
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class DouyuJsonPipeline(object):
    def open_spider(self, spider):
        self.f = open("douyu.json", "w")

    def process_item(self, item, spider):
        item["utc_time"] = str(datetime.utcnow())
        item['source'] = spider.name
        content = json.dumps(dict(item)) + ",\n"
        self.f.write(content)
        return item

    def close_spider(self, spider):
        self.f.close()


class DouyuImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 发送图片请求，响应保存到settings.py IMAGES_STORE指定的路径下
        yield scrapy.Request(item["image_src"])

    def item_completed(self, results, item, info):
        # 取出原始图片存储路径
        image_path = [x["path"] for ok, x in results if ok][0]
        item["image_path"] = IMAGES_STORE+ "\\" + item['nick_name'] + ".jpg"

        #  通过图片原路径修改新名称
        #os.rename("old_name", "new_name")
        try:
            os.rename(
                IMAGES_STORE + image_path,
                item["image_path"]
            )
        except:
            logging.error("%s 图片修改失败.." % IMAGES_STORE + image_path)


        return item
