# Scrapy settings for Myscrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Myscrapy'

SPIDER_MODULES = ['Myscrapy.spiders']
NEWSPIDER_MODULE = 'Myscrapy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Myscrapy (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
DOWNLOADER_MIDDLEWARES = {
#    'Myscrapy.middlewares.MyscrapySpiderMiddleware': 543,
    'Myscrapy.middlewares.RandomUaMiddleware': 200,
    'Myscrapy.middlewares.RandomCookieMiddleware': 300,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Myscrapy.middlewares.MyscrapyDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Myscrapy.pipelines.MySqlPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# MYSQL
MYSQL_LOCAL_CONF = {
    "host": "localhost",
    "user": "root",
    "password": "123456",
    "db": "scrapy"
}

# LOG
# import sys
# if sys.platform == 'win32':
#     LOG_FILE = r'C:\Users\Jove\PycharmProjects\MyScrapy\Myscrapy\log\jd.log'
# else:
#     LOG_FILE = ""
#
# LOG_LEVEL = "ERROR"

# RETRY, 如果复杂的重试机制, 需要重写 RetryMiddleware 需要关闭 RETRY_ENABLE
RETRY_ENABLE = True
# 一定要设置 retry_times
RETRY_TIMES = 6

# SCHEDULER 要使用 scrapy-redis 的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 保证所有的爬虫通过 redis 的重复过滤器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# Specify the host and port to use when connecting to Redis (optional).
REDIS_HOST = 'my_linux'
REDIS_PORT = 6379
# REDIS_PASSWORD = 'Wecf09#Huipm'

# Specify the full Redis URL for connecting (optional).
# If set, this takes precedence over the REDIS_HOST and REDIS_PORT settings.
# REDIS_URL = 'redis://AUTH:Wecf09#Huipm@my_linux:6379'

# Custom redis client parameters (i.e.: socket timeout, etc.)
# REDIS_PARAMS  = {'db': '3'}
REDIS_PARAMS  = {'db': '3', 'password': 'Wecf09#Huipm'}