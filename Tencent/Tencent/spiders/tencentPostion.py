# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem
from scrapy.loader import ItemLoader

class TencentpostionSpider(scrapy.Spider):
    # 名字
    name = 'tencentPostion'
    # 范围
    allowed_domains = ['tencent.com']
    url = "http://hr.tencent.com/position.php?&start="
    offset = 0
    #起始
    start_urls = [url + str(offset)]

    def parse(self, response):
        print('dfdfd')
        itemLoader = ItemLoader(item = TencentItem(), response = response)
        itemLoader.add_xpath('positionname', '//td[1]/a/text()')
        itemLoader.add_xpath('postionlink', '//td[1]/a/@hre')
        itemLoader.add_xpath('postionType', '//td[2]/text()')
        itemLoader.add_xpath('peopleNum', '//td[3]/text()')
        itemLoader.add_xpath('workLocation', '//td[4]/text()')
        itemLoader.add_xpath('publishTime', '//td[5]/text()')
        yield itemLoader.load_item()

        if self.offset < 168:
            self.offset += 10

        yield scrapy.Request(self.url + str(self.offset), callback = self.parse)
        # index = 0
        # for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
        #     # 初始化模型对象
        #     index += 1
        #     print(index)
        #     item = TencentItem()
        #     item['positionname'] = each.xpath('./td[1]/a/text()').extract()[0]
        #     item['postionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
        #     # 职位类别
        #     item['postionType'] = each.xpath("./td[2]/text()").extract()[0]
        #     # 招聘人数
        #     item['peopleNum'] = each.xpath("./td[3]/text()").extract()[0]
        #     # 工作地点
        #     item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
        #     # 发布时间
        #     item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]
        #
        #     yield item
        #
        # if  self.offset<1680:
        #     self.offset += 10
        #
        # print('next')
        # yield  scrapy.Request(self.url + str(self.offset),callback = self.parse)
