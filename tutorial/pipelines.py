# -*- coding: utf-8 -*-
# 项目中的pipelines 文件
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class TutorialPipeline(object):
    # 每个item pipeline组件都需要调用该方法，这个方法必须返回一个 Item (或任何继承类)对象，或是抛出 DropItem异常，被丢弃的item将不会被之后的pipeline组件所处理。
    # 参数: item: 由parse方法返回的Item对象(Item对象) spider: 抓取到这个Item对象对应的爬虫对象(Spider对象)
    # words_to_filter = ['politics', 'religion']

    def process_item(self, item, spider):
        pass
        # for word in self.words_to_filter:
        #     if word in unicode(item['description']).lower():
        #         raise DropItem("Contains forbidden word: %s" % word)
        # else:
        #     return item
