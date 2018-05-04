# -*- coding: utf-8 -*-
import scrapy
from ..items import ItcastteaspiderItem

class ItcastSpider(scrapy.Spider):
    # 爬虫名,唯一
    name = 'itcast'
    # 爬虫的爬取的范围
    allowed_domains = ['itcast.cn']
    # 爬虫开始的位置，这个列表的数量可以决定爬虫是否并发
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # 解析的方法，每个初始url完成下载后将被调用
        # with open('teacher.html','wb') as f :
        #     # 写文件时最好转成二进制写不容易出错
        #     content=response.text.encode()
        #     f.write(content)
        # 存放老师信息集合
        items=[]
        node_list=response.xpath('//div[@class="li_txt"]')
        for node in node_list:
            item=ItcastteaspiderItem()
            item['name']=node.xpath('./h3/text()').extract_first()
            item['level']=node.xpath('./h4/text()').extract_first()
            item['info']=node.xpath('./p/text()').extract_first()
            #直接返回数据不经过管道
            # items.append(item)
            #将获取的数据交给管道
            yield item
"""
所有老师的节点：//div[@class='tea_txt tea_txt_cur']//li
//div[@class='li_txt'] 所有老师的信息
//div[@class='tea_con']//div[@class='li_txt']/h3
"""