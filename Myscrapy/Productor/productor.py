import json

import redis


con = redis.Redis(host='my_linux',
                  port=6379,
                  password='Wecf09#Huipm',
                  db=3,
                  )

def start_requests():
    for keyword in keyword_array:
        for page in range(1, 6):
            url = f"https://search.jd.com/Search?keyword={keyword}&psort=3&suggest=1.his.0.0&wq={keyword}&psort=3&page={page}&s=61&click=0"
            task = {
                "url": url,
                'meta': {'keyword': keyword},
                'method': "GET",
            }
            redis_key = 'example:start_urls'
            con.lpush(redis_key, json.dumps(task))


if __name__ == '__main__':
    keyword_array = ["键盘", "鼠标", "显示器", "机箱", "显卡"]
    start_requests()