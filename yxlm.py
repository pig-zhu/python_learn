import urllib3
import os
import sys
import json
from bs4 import BeautifulSoup
# 创建连接
http = urllib3.PoolManager()
# 根目录
root = "C:\\Users\\Administrator\\Downloads\\python-pa\\yxlm\\"
# 发送请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
res = http.request('GET',
                    'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?v=45')
html = json.loads(res.data.decode('gbk')).get('hero')
# 拿到英雄id ， 用于拼接图片的url
for item in html:
    # 设置文件路径与文件名字
    directory = item['name']+'-'+item['title']
    # 新建英雄的目录
    if os.path.exists(root+directory):
        pass
    else:
        os.mkdir(root+directory)
    print(directory+'的皮肤正在下载...')
    url = "https://game.gtimg.cn/images/lol/act/img/js/hero/" +str(item['heroId']) + '.js'
    try:
        result = http.request('GET',url)
        imgUrl = json.loads(result.data)['skins']
        for i in imgUrl:
            if i.get('mainImg'):
                imgContent = http.request('GET',i['mainImg']).data
            else:
                imgContent = http.request('GET',i['chromaImg']).data
            with open(os.path.join(root+directory, i['name']+'.jpg'), 'wb') as jpg:
                jpg.write(imgContent)
    except Exception as e:
        print(e)
print('全部下载完啦！')

