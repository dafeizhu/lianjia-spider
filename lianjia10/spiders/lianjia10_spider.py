# -*- coding: utf-8 -*-
import scrapy
from lianjia10.items import Lianjia10Item

class Lianjia10SpiderSpider(scrapy.Spider):
    # 访问链家租房网
    name = 'lianjia10_spider'
    allowed_domains = ['dg.lianjia.com']
    start_urls = ['https://dg.lianjia.com/zufang/pg1/#contentList']

    def parse(self, response):
        # 使用xpath和CSS选择器参数属性提取数据
        a= response.xpath("//div[@class='content__list--item--main']")
        b= response.css("div[class='content__list--item--main']")
        # 遍历获取到的对象
        for i in a:
            item = Lianjia10Item()
            # 数据清洗
            title = i.xpath("./p[1]/a/text()").extract()[0]
            detail_link = i.xpath("./p[1]/a/@href").extract()[0]
            prize = i.xpath("./span/em/text()").extract()[0]
            time = i.xpath("./p[4]/text()").extract()[0]
            des = b.css("p[class='content__list--item--des'] a::text").extract()[0:2]
            location = str(des[0]+des[1]).replace('\n','').strip()
            # 将处理完的数据一个个存储到字典中
            item["title"] = title.strip()
            item["detail_link"] = "https://dg.lianjia.com" + str(detail_link).replace("['","").replace("']","")
            item["prize"] = prize
            item["time"] = time
            item["location"] = location
            request = scrapy.Request(url = item["detail_link"],callback = self.parse_body)
            request.meta["item"] = item
            yield request
        # 遍历下一页
        for i in range(1,100):
            yield scrapy.Request(url = "https://dg.lianjia.com/zufang/pg" + str(i) +"/#contentList",callback=self.parse)

    # 回调函数 结果返回第31行
    def parse_body(self,response):
        item = response.meta["item"]  
        # 同理 使用xpath定位房屋信息和房源描述
        fangwuxinxi = response.xpath("//li[@class='fl oneline']/text()").extract()
        fangyuanmiaoshu = response.xpath("//p[@data-el='houseComment']/text()").extract()
        fangwuxinxi = "\n".join(fangwuxinxi)
        fangyuanmiaoshu = "\n".join(fangyuanmiaoshu)
        item["content"] = "房屋信息：\n" + fangwuxinxi + "\n房源描述：\n" + fangyuanmiaoshu
        yield item


    