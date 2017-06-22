# -*- coding: utf-8 -*-
# 项目的item文件
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field

class DmozItem(Item):
    # define the fields for your item here like:
    # 小区
    xiaoqu = Field()
    # 户型
    houseType = Field()
    # 面积
    square = Field()
    # 房屋详情链接
    houseUrl = Field()
    # 房屋朝向
    orientation = Field()
    # 楼层
    floor = Field()
    # 建房信息
    buildInfo = Field()
    # 房子所在位置
    houseArea = Field()
    # 平方均价
    perSquarePrice = Field()
    # 总价
    totalPrice = Field()

