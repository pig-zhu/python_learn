import urllib3
import os
import sys
import json
from bs4 import BeautifulSoup
# 创建连接
http = urllib3.PoolManager()
# 根目录
root = "C:\\Users\\Administrator\\Downloads\\python-pa\\img\\"
# 发送请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
res = http.request('GET',
                    'https://pvp.qq.com/web201605/js/herolist.json')
# 获取到的网页 -- 直接获取数据
directory = 'page'
html = json.loads(res.data.decode())
# 拿到英雄id ， 用于拼接图片的url
for item in html:
    # 设置文件路径与文件名字
    directory = item['cname']
    # 皮肤的名称列表
    if item.get('skin_name'):
        skinList = item['skin_name'].split('|')
    else:
        skinList = list(range(1,12))
    # 新建英雄的目录
    if os.path.exists(root+directory):
        pass
    else:
        os.mkdir(root+directory)
    print(directory+'的皮肤正在下载...')
    for i in range(1,13):
        url = "http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/" +str(item['ename'])+'/'+str(item['ename'])+'-bigskin-'+str(i)+'.jpg'
        
        try:
            img = http.request('GET',url)
            with open(os.path.join(root+directory, skinList[i-1]+'.jpg'), 'wb') as jpg:
                jpg.write(img.data)
        except Exception as e:
            break
print('全部下载完啦！')







# HTML = BeautifulSoup(html, 'html.parser')
# 从网页中提取到各个英雄的链接
# 先提取到ul列表
# ul = HTML.find_all("ul", {"class":"herolist"})
# 再从ul中提取到a
# aList= ul[0].find_all('a')
# print('a的内容:',html)
# print('a的内容:',aList[0].string, aList[0].get('href'))
 
