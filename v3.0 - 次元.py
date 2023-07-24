import requests
import os
import ctypes

url = 'https://t.mwm.moe/pc/'

response = requests.get(url)

if response.status_code == 200:
    with open('image.jpg', 'wb') as file:
        file.write(response.content)
    print("图片下载成功")
else:
    print("图片下载失败")

print("设置为桌面壁纸")

image_path = os.path.abspath('image.jpg')
ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)