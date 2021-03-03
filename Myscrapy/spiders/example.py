import json
import time

import scrapy
from bs4 import BeautifulSoup
from scrapy_redis.spiders import RedisSpider

from Myscrapy.items import MyscrapyItem
from scrapy.exceptions import CloseSpider
from scrapy.selector import Selector


class ExampleSpider(RedisSpider):
    name = 'example'
    # allowed_domains = ['example.com']
    # start_urls = ['http://example.com/']
    redis_key = f"{name}:start_urls"

    def make_request_from_data(self, data):

        task = json.loads(data.decode('utf-8'))

        return scrapy.FormRequest(
            dont_filter=False,
            url=task['url'],
            method=task['method'],
            # formdata=task['body'],  # post请求带上的参数
            callback=self.parse_search,
            errback=self.process_error,
            meta=task['meta'],
        )


    def parse_search(self, response, **kwargs):
        html = response.body.decode('utf-8')
        soup = BeautifulSoup(html, 'lxml')
        parse_array = soup.select('.gl-item')
        # li_ele_array = soup.select("ul[class^='gl-warp'] li[class='gl-item']")
        for item in parse_array:
            try:
                img = item.select('.p-img')
                price = item.select('.p-price')
                name = item.select('.p-name')
                shop = item.select('.p-shop')
                icons = item.select('.p-icons')

                item = MyscrapyItem()
                item['img'] = img[0].img.attrs["data-lazy-img"]
                item['price'] = price[0].i.text
                item['name'] = name[0].em.text
                item['shop'] = shop[0].a.attrs["title"]
                item['icons'] = json.dumps([x.text.strip() for x in icons[0].select("i[class^='goods-icons']")])
                item['keyword'] = response.request.meta['keyword']
                item['create_time'] = time.strftime("%Y-%m-%d")

                yield item
            except Exception as e:
                print(e.args)

    def process_error(self, failure):
        print(failure)
        if failure.value.args[0] == "账号异常":
            raise CloseSpider
        meta = {}
        meta['keyword'] = failure.request._meta['keyword']
        yield failure.request # 将请求抛出交给调度器