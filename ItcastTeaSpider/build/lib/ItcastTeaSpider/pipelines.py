# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class ItcastteaspiderPipeline(object):
    def __init__(self):
        #可选实现，做参数初始化
        self.f=open('tea.json','wb')
    # def open_spider(self,spider):
        # 可选实现，当spider被开启时，这个方法被调用。


    def process_item(self, item, spider):
        content=json.dumps(dict(item),ensure_ascii=False)+'\n'
        # 编码，string--->bytes   encode()
        # 解码，bytes---->string decode()
        self.f.write(content.encode())
        return item

    def close_spider(self,spider):
        #  当spider被关闭时调用
        self.f.close()

class TencentJsonPipeline(object):

    def __init__(self):
        #self.file = open('teacher.json', 'wb')
        self.file = open('tencent.json', 'wb')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(content.encode())
        return item

    def close_spider(self, spider):
        self.file.close()