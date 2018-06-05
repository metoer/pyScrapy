# -*- coding: utf-8 -*-
import scrapy
import  sys,os

path = os.path.abspath(sys.argv[0])
path = os.path.dirname(path)
path = os.path.dirname(path)
print(os.path.dirname(path))
sys.path.append(os.path.dirname(path))
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from TencentSpider.items import TencentspiderItem

class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ["http://hr.tencent.com/position.php?&start=0#a"]

    # Respone里链接的提取规则，返回的服务匹配规则的链接匹配对象的列表
    pagelink = LinkExtractor(allow = ('start=\d+'))

    rules = (
        Rule(pagelink, callback='parse_item', follow=True),
    )

    ##替换原来的start_requests，callback为
    # def start_requests(self):
    #     return [Request("http://www.zhihu.com/#signin", meta = {'cookiejar': 1}, callback = self.post_login)]
    # def post_login(self, response):
    #     # print
    #     'Preparing login'
    #     # 下面这句话用于抓取请求网页后返回网页中的_xsrf字段的文字, 用于成功提交表单
    #     xsrf = Selector(response).xpath('//input[@name="_xsrf"]/@value').extract()[0]
    #     # print       xsrf
    #     # FormRequeset.from_response是Scrapy提供的一个函数, 用于post表单
    #     # 登陆成功后, 会调用after_login回调函数
    #     return [FormRequest.from_response(response,  # "http://www.zhihu.com/login",
    #                                       meta = {'cookiejar': response.meta['cookiejar']},
    #                                       headers = self.headers,
    #                                       formdata = {
    #                                           '_xsrf'   : xsrf,
    #                                           'email'   : '1527927373@qq.com',
    #                                           'password': '321324jia'
    #                                       },
    #                                       callback = self.after_login,
    #                                       dont_filter = True
    #                                       )]
    #
    # # make_requests_from_url会调用parse，就可以与CrawlSpider的parse进行衔接了
    # def after_login(self, response):
    #     for url in self.start_urls:
    #         yield self.make_requests_from_url(url)
    def parse_item(self, response):
        print('dfdfd')
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            # 初始化模型对象
            item = TencentspiderItem()
            item['positionname'] = each.xpath('./td[1]/a/text()').extract()[0]
            item['postionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            item['postionType'] = each.xpath("./td[2]/text()").extract()[0]
            # 招聘人数
            item['peopleNum'] = each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]

            yield item
