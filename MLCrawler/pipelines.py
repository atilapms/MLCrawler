# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class MlcrawlerPipeline(object):
    def open_spider(self, gpus):
        self.file = open('items.json', 'w')

    def close_spider(self, gpus):
        self.file.close()

    def process_item(self, item, gpus):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
