import requests
import json
import time


def look(data):
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0'
                }
        url = 'https://www.ichunqiu.com/courses/ajaxCourses'
        r = requests.post(url=url, headers=headers, data=data)
        datas = json.loads(r.content)
        for i in datas['course']['result']:
                print(i['courseName']+'---------------'+i['producerName'])

for i in range(1,13):
        data = 'courseTag=&courseDiffcuty=&IsExp=&producerId=&orderField=&orderDirection=&tagType=' \
               '&isOpen=&pageIndex=%s'%(i)
        look(data)
        time.sleep(0.5)
