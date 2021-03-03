# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter

from Myscrapy.settings import MYSQL_LOCAL_CONF
from Myscrapy.items import MyscrapyItem

class MyscrapyPipeline:
    def process_item(self, item, spider):
        return item


class MySqlPipeline:
    def __init__(self):
        self.mysql_server = pymysql.connect(**MYSQL_LOCAL_CONF)
        self.cursor = self.mysql_server.cursor()

    def process_item(self, item, spider):
        if isinstance(item, MyscrapyItem):
            SQL = "INSERT INTO jd_crawler(`img`, `price`, `name`, `shop`, `icons`, `keyword`, `create_time`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            self.cursor.executemany(SQL, [[item['img'],
                                           item['price'],
                                           item['name'],
                                           item['shop'],
                                           item['icons'],
                                           item['keyword'],
                                           item['create_time']],])
            self.mysql_server.commit()