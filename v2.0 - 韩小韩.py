import json
import requests
import os
import re
import ctypes

url = 'https://api.vvhan.com/api/acgimg'
params = {'type': 'json'}
res = requests.get(url, params=params).json()
print(json.dumps(res, indent=2))

print("已获取到API返回信息")

text = (json.dumps(res, indent=2))

print(text)

print("检测API返回信息")

# 使用正则表达式匹配链接的模式
pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

# 查找第三行
third_line = text.split('\n')[2]

print(third_line)

print("定位链接行数")

# 提取链接
links = re.findall(pattern, third_line)

# 打印结果
print(links)

print("定位链接")

os.makedirs('./image/', exist_ok=True)
IMAGE_URL = links[0]

def urllib_download():
    from urllib.request import urlretrieve
    urlretrieve(IMAGE_URL, './image/img1.png')
    
urllib_download()

print("正在下载并设置为桌面壁纸")

image_path = os.path.abspath('./image/img1.png')
ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)