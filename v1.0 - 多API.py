import json
import requests
import os
import re

print("1.韩小韩")
print("2.樱花")
print("3.三秋")
print("4.吃猫酱")
command = input("请输入要获取图片的源:")

if command == "1":
    url = 'https://api.vvhan.com/api/acgimg'
    params = {'type': 'json'}
    res = requests.get(url, params=params).json()
    print(json.dumps(res, indent=2))

    text = (json.dumps(res, indent=2))

    print(text)

    # 使用正则表达式匹配链接的模式
    pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    # 查找第三行
    third_line = text.split('\n')[2]

    print(third_line)

    # 提取链接
    links = re.findall(pattern, third_line)

    # 打印结果
    print(links)

    os.makedirs('./image/', exist_ok=True)
    IMAGE_URL = links[0]

    def urllib_download():
        from urllib.request import urlretrieve
        urlretrieve(IMAGE_URL, './image/img1.png')
    
    urllib_download()
        
if command == "2":
    url = 'http://www.dmoe.cc/random.php'
    params = {'return': 'json'}
    res = requests.get(url, params=params).json()
    print(json.dumps(res, indent=2))

if command == "3":
    url = 'https://api.ghser.com/random/api.php'
    res = requests.get(url)
    print(res.url)

if command == "4":
    url = 'https://api.yimian.xyz/img'
    params = {
        'type': 'moe',
        'size': '1920x1080'
    }
    res = requests.get(url, params=params)
    print(res.url)