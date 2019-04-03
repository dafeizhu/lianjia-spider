from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from lianjia10.spiders.lianjia10_spider import Lianjia10SpiderSpider
from lianjia10.db import Lianjia10Info

# 在Scrapy框架内控制爬虫
if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())
    process.crawl("lianjia10_spider")
    
    # 控制台主界面
    main = int(input("请输入操作类型：（1或2）"))
    if main == 1:
        process.start()

    elif main == 2:
        keyword = input("关键字：")
        city = input("区域：")
        begin = input("起点位置：")
        total = input("显示多少记录：")
        print(Lianjia10Info("lianjiainfo10").outinfo(keyword,city,begin,total))
 
    else:
        print("输入错误！")

