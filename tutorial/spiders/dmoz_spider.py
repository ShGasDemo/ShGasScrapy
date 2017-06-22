# -*- coding: utf-8 -*-
# 放置spider代码的目录
from scrapy.spider import Spider
from scrapy.selector import Selector
from tutorial.items import DmozItem
import re

class DmozSpider(Spider):
    name = "dmoz" #爬虫的识别名，它必须是唯一的，在不同的爬虫中你必须定义不同的名字.
    # allowed_domains = ["dmoz.org"]
    houseUrls= []
    for i in range(1,101):
        url = "http://sh.lianjia.com/ershoufang/d{0}".format(str(i))
        houseUrls.append(url)
    start_urls = houseUrls #start_urls：包含了Spider在启动时进行爬取的url列表。因此，第一个被获取到的页面将是其中之一。后续的URL则从初始的URL获取到的数据中提取。我们可以利用正则表达式定义和过滤需要进行跟进的链接。

    # 这个方法负责解析返回的数据、匹配抓取的数据(解析为 item )并跟踪更多的 URL。
    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="js_fang_list"]/li/div[@class="info"]')
        items = []
        for site in sites:
            item = DmozItem()
            item['xiaoqu'] = ''.join(site.xpath('div[@class="info-table"]//a[@class="laisuzhou"]/span/text()').extract())
            item['houseType'] = site.xpath('div[@class="info-table"]//span[@class="info-col row1-text"]/text()').extract()[1].split('|')[0].strip()
            item['square'] = site.xpath('div[@class="info-table"]//span[@class="info-col row1-text"]/text()').extract()[1].split('|')[1].strip()
            item['houseUrl'] = 'http://sh.lianjia.com' + ''.join(site.xpath('div[@class="prop-title"]/a/@href').extract())
            item['floor'] = site.xpath('div[@class="info-table"]//span[@class="info-col row1-text"]/text()').extract()[1].split('|')[2].strip()
            if(len(site.xpath('div[@class="info-table"]//span[@class="info-col row1-text"]/text()').extract()[1].split('|'))>3):
                item['orientation'] = site.xpath('div[@class="info-table"]//span[@class="info-col row1-text"]/text()').extract()[1].split('|')[3].strip()
            if (len(site.xpath('div[@class="info-table"]//span[@class="info-col row2-text"]/text()').extract()[4].split('|')) > 1):
                item['buildInfo'] = site.xpath('div[@class="info-table"]//span[@class="info-col row2-text"]/text()').extract()[4].split('|')[1].strip()
            item['houseArea'] = ''.join(site.xpath('div[@class="info-table"]//span[@class="info-col row2-text"]/a/text()').extract()).strip()
            item['perSquarePrice'] = re.search(r'\d+',''.join(site.xpath('div[@class="info-table"]//span[@class="info-col price-item minor"]/text()').extract()).strip()).group()
            item['totalPrice'] = ''.join(site.xpath('div[@class="info-table"]//div[@class="info-col price-item main"]/span/text()').extract())
            items.append(item)
        return items
