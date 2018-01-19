# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
import codecs
import json
# class MorePicPipeline(ImagesPipeline):
    # def get_media_requests(self,item,info):
    #     for image_url in item['image_url']:
    #         yield Request(image_url)
    #
    # def item_completed(self,results,item,info):
    #     image_paths=[x['path'] for ok,x in results if ok]
    #     if not image_paths:
    #         raise DropItem('图片未下载好'%image_paths)
class MorePicPipeline(object):
    def __init__(self):
        self.file = codecs.open('more1_pic.json', mode='wb', encoding='utf-8')

    def process_item(self, item, spider):
        line=json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.file.write(line)
        return item
    def close_spider(self,spider):
        self.file.close()
