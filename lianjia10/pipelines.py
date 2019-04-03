# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exceptions import DropItem
import json
from lianjia10.db import Lianjia10Info

# 通过管道将数据压进数据库
class Lianjia10Pipeline(object):
    def __init__(self):
        # self.file = open("hr10.json","w",encoding="utf-8")
        pass

    def process_item(self, item, spider):
        if item["title"]:
            # line = json.dumps(dict(item))+"\n"
            # self.file.write(line.encode("utf-8").decode("unicode_escape"))
            lianjia10 = Lianjia10Info("lianjiainfo10")
            lianjia10.add_lianjia10(item["title"],item["detail_link"],item["prize"],item["time"],item["location"],item["content"])
            return item
        else:
            raise DropItem("没有标题 %s"%item)