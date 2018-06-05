# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import  json

class TencentPipeline(object):

    def __init__(self):
        self.fileName = open('tencent.json','wb+')

    def process_item(self, item, spider):
        print('save')
        text = json.dumps(dict(item),ensure_ascii = False) +",\n"
        self.fileName.write(text.encode('utf-8'))

        return item
    def close_spider(self,spider):
        self.fileName.close()