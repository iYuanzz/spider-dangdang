# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from spider.items import BookItem


class SpiderPipeline(object):

    def process_item(self, item, spider):
        # if isinstance(item, BookItem):
            return item
        # else:
        #     return None