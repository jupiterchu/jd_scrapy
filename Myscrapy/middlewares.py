# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import json
import random

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class RandomUaMiddleware:
    UA_ARRAY = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4240.111 Safari/537.36",
    ]

    def process_request(self, request, spider):
        ua = random.choice(self.UA_ARRAY)
        request.headers['user-agent'] = ua

        # raise Exception('a')

class RandomCookieMiddleware:
    COOKIE_ARRAY = [
        "areaId=1;"
    ]

    def process_request(self, request, spider):
        cookies = random.choice(self.COOKIE_ARRAY)
        request.headers['cookies'] = cookies


class ProxyMiddleware:
    """
    尽量搭建一个代理池, 请求同一个位置, 在一定时间后, 可以拿到不同的ip
    """
    json_data = json.loads("""{"code":0,"data":[{"ip":"112.83.180.133","port":4231},{"ip":"49.87.49.46","port":4257},{"ip":"49.82.123.226","port":4236},{"ip":"112.84.193.179","port":4245},{"ip":"49.85.110.88","port":4216},{"ip":"106.111.13.22","port":4253},{"ip":"121.226.187.199","port":4264},{"ip":"180.122.147.237","port":4236},{"ip":"49.71.133.104","port":4257},{"ip":"49.82.120.36","port":4268},{"ip":"122.192.227.37","port":4278},{"ip":"106.111.13.207","port":4257},{"ip":"117.90.221.63","port":4216},{"ip":"121.226.76.210","port":4264},{"ip":"58.217.55.249","port":4203},{"ip":"122.194.84.249","port":4231},{"ip":"121.226.152.105","port":4236},{"ip":"180.119.156.167","port":4278},{"ip":"114.227.9.22","port":4275},{"ip":"114.237.133.70","port":4250},{"ip":"49.84.50.235","port":4207},{"ip":"180.122.147.223","port":4257},{"ip":"49.88.249.57","port":4214},{"ip":"218.91.135.253","port":4282},{"ip":"49.70.180.17","port":4207},{"ip":"117.95.1.150","port":4236},{"ip":"180.104.2.101","port":4278},{"ip":"153.99.2.120","port":4245},{"ip":"112.87.90.9","port":4245},{"ip":"114.238.219.31","port":4236},{"ip":"121.226.4.98","port":4256},{"ip":"49.84.87.188","port":4203},{"ip":"114.227.9.192","port":4276},{"ip":"153.99.7.191","port":4207},{"ip":"122.194.84.223","port":4231},{"ip":"153.99.13.79","port":4245},{"ip":"49.82.26.96","port":4261},{"ip":"49.72.192.23","port":4236},{"ip":"117.95.200.227","port":4236},{"ip":"49.71.163.233","port":4285},{"ip":"180.125.233.245","port":4278},{"ip":"222.190.198.127","port":4257},{"ip":"106.111.13.111","port":4236},{"ip":"180.122.149.83","port":4257},{"ip":"114.227.9.210","port":4275},{"ip":"49.85.81.212","port":4257},{"ip":"114.238.173.215","port":4268},{"ip":"180.122.180.155","port":4253},{"ip":"180.122.151.198","port":4236},{"ip":"180.122.145.217","port":4257},{"ip":"117.94.236.153","port":4257},{"ip":"117.63.129.221","port":4276},{"ip":"49.71.133.177","port":4257},{"ip":"58.218.33.164","port":4278},{"ip":"121.233.206.13","port":4264},{"ip":"114.238.197.129","port":4217},{"ip":"218.91.135.34","port":4278},{"ip":"121.226.2.217","port":4256},{"ip":"180.125.96.92","port":4236},{"ip":"49.70.67.56","port":4264},{"ip":"117.95.198.205","port":4264},{"ip":"112.84.210.201","port":4245},{"ip":"49.74.55.233","port":4217},{"ip":"180.122.151.215","port":4257},{"ip":"117.91.170.128","port":4278},{"ip":"117.94.127.66","port":4216},{"ip":"121.226.3.29","port":4264},{"ip":"117.94.158.37","port":4236},{"ip":"49.82.51.249","port":4253},{"ip":"114.227.104.115","port":4275},{"ip":"49.85.184.205","port":4257},{"ip":"180.122.182.215","port":4257},{"ip":"122.192.227.46","port":4278},{"ip":"117.95.201.31","port":4236},{"ip":"153.99.4.24","port":4207},{"ip":"49.70.184.247","port":4203},{"ip":"221.231.91.46","port":4232},{"ip":"49.70.180.69","port":4207},{"ip":"153.99.5.254","port":4245},{"ip":"112.83.181.91","port":4231},{"ip":"49.81.168.202","port":4278},{"ip":"49.64.247.172","port":4236},{"ip":"114.239.148.10","port":4245},{"ip":"180.122.147.38","port":4257},{"ip":"49.87.83.252","port":4268},{"ip":"114.230.64.2","port":4226},{"ip":"114.227.9.221","port":4276},{"ip":"117.94.177.191","port":4257},{"ip":"222.190.163.99","port":4236},{"ip":"221.230.233.207","port":4216},{"ip":"121.226.214.130","port":4245},{"ip":"180.117.218.93","port":4278},{"ip":"49.70.85.129","port":4264},{"ip":"114.230.66.8","port":4278},{"ip":"114.233.70.16","port":4216},{"ip":"49.88.157.170","port":4234},{"ip":"112.64.52.173","port":4275},{"ip":"49.87.117.42","port":4217},{"ip":"117.63.130.73","port":4276},{"ip":"49.70.99.36","port":4245},{"ip":"121.226.186.145","port":4264},{"ip":"180.105.146.50","port":4234},{"ip":"117.63.130.179","port":4276},{"ip":"49.86.176.100","port":4264},{"ip":"117.90.222.94","port":4216},{"ip":"121.233.175.108","port":4236},{"ip":"122.192.227.20","port":4278},{"ip":"114.239.146.76","port":4245},{"ip":"180.109.126.255","port":4232},{"ip":"49.88.159.251","port":4234},{"ip":"114.238.154.24","port":4261},{"ip":"49.70.67.163","port":4236},{"ip":"121.233.163.237","port":4282},{"ip":"222.189.104.100","port":4250},{"ip":"49.69.251.175","port":4232},{"ip":"49.85.2.188","port":4257},{"ip":"221.230.162.32","port":4216},{"ip":"114.236.148.47","port":4232},{"ip":"114.239.110.241","port":4236},{"ip":"117.63.128.81","port":4275},{"ip":"49.81.190.180","port":4278},{"ip":"121.224.50.85","port":4236},{"ip":"49.82.123.239","port":4257},{"ip":"180.122.151.89","port":4257},{"ip":"114.233.159.184","port":4257},{"ip":"112.83.171.108","port":4231},{"ip":"112.84.244.48","port":4207},{"ip":"180.122.180.43","port":4257},{"ip":"112.83.180.30","port":4231},{"ip":"117.63.26.58","port":4276},{"ip":"114.238.38.177","port":4217},{"ip":"49.84.87.191","port":4203},{"ip":"221.6.186.202","port":4231},{"ip":"180.125.88.233","port":4257},{"ip":"106.111.28.39","port":4285},{"ip":"180.122.41.24","port":4257},{"ip":"114.226.116.112","port":4275},{"ip":"122.192.226.112","port":4278},{"ip":"112.85.45.72","port":4217},{"ip":"49.88.249.94","port":4214},{"ip":"49.85.81.188","port":4236},{"ip":"49.70.240.229","port":4203},{"ip":"180.111.110.246","port":4232},{"ip":"218.91.4.114","port":4264},{"ip":"153.36.73.60","port":4278},{"ip":"114.233.71.75","port":4285},{"ip":"114.227.104.55","port":4275},{"ip":"117.95.192.97","port":4264},{"ip":"180.104.2.90","port":4278},{"ip":"121.226.155.254","port":4264},{"ip":"121.233.160.24","port":4226},{"ip":"122.192.227.77","port":4278},{"ip":"117.94.180.150","port":4257},{"ip":"49.89.61.92","port":4245},{"ip":"153.99.5.60","port":4245},{"ip":"49.87.83.114","port":4278},{"ip":"49.88.245.129","port":4214},{"ip":"112.87.3.194","port":4207},{"ip":"49.71.158.183","port":4257},{"ip":"180.122.144.146","port":4236},{"ip":"117.92.126.73","port":4234},{"ip":"180.119.157.167","port":4226},{"ip":"49.88.106.175","port":4250},{"ip":"153.99.8.219","port":4245},{"ip":"49.71.133.110","port":4257},{"ip":"49.87.83.166","port":4253},{"ip":"114.230.67.248","port":4278},{"ip":"49.74.57.182","port":4217},{"ip":"114.238.108.142","port":4217},{"ip":"153.99.27.75","port":4245},{"ip":"114.229.4.56","port":4207},{"ip":"114.239.30.100","port":4236},{"ip":"180.122.147.128","port":4253},{"ip":"117.63.26.113","port":4276},{"ip":"180.127.0.235","port":4234},{"ip":"114.238.173.156","port":4253},{"ip":"49.71.158.199","port":4257},{"ip":"139.227.191.22","port":4275},{"ip":"153.99.5.145","port":4245},{"ip":"106.111.229.22","port":4203},{"ip":"114.227.9.49","port":4275},{"ip":"180.104.182.204","port":4278},{"ip":"153.36.226.235","port":4278},{"ip":"49.65.164.11","port":4232},{"ip":"114.227.104.36","port":4275},{"ip":"153.36.226.247","port":4278},{"ip":"112.85.45.217","port":4217},{"ip":"114.238.108.71","port":4278},{"ip":"180.119.157.14","port":4226},{"ip":"121.226.153.23","port":4236},{"ip":"112.85.45.224","port":4217},{"ip":"49.70.168.160","port":4207},{"ip":"49.87.117.89","port":4268},{"ip":"106.111.70.6","port":4232},{"ip":"58.217.55.186","port":4203},{"ip":"112.83.143.205","port":4231},{"ip":"122.195.255.215","port":4207},{"ip":"112.64.53.200","port":4275},{"ip":"49.82.123.244","port":4236},{"ip":"117.95.192.215","port":4245}],"msg":"0","success":true}""")
    IP_ARRAY = json_data['data']

    def process_request(self, request, spider):
        ip = random.choice(self.IP_ARRAY)
        ip = f"{ip['host']}:{ip['port']}"
        request.meta['proxy'] = ip