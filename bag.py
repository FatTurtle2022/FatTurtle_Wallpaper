import tkinter as tk
import requests
import os
import ctypes
import shutil

# 获取当前脚本所在目录的绝对路径
script_dir = os.path.dirname(os.path.abspath(__file__))

# 切换到当前脚本所在目录
os.chdir(script_dir)

# 检测文件是否存在
if os.path.exists("minutes.txt"):
    print("minutes存在")
else:
    # 创建文件并写入数字1
    with open("minutes.txt", "w") as file:
        file.write("1")

# 检测文件是否存在
if os.path.exists("seconds.txt"):
    print("minutes存在")
else:
    # 创建文件并写入数字1
    with open("seconds.txt", "w") as file:
        file.write("1")

window = tk.Tk()
window.title('肥胖龟壁纸')
window.geometry('200x450')

var = tk.StringVar()
command = tk.Label(window, textvariable=var, bg='white', font=('Arial,12'), width=25, height=2)
command.pack()

var.set('肥胖龟壁纸')

def start():
    f = open("minutes.txt", "r")
    minutes = f.read()
    f.close()

    s = open("seconds.txt", "r")
    seconds = s.read()
    s.close()

    times = int(minutes) * 60 + int(seconds)

    def download_and_set_wallpaper():
        url = 'https://t.mwm.moe/ycy'
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
        var.set('已启动')

        window.after(times * 1000, download_and_set_wallpaper)

    download_and_set_wallpaper()

start_button = tk.Button(window, text='启动软件', width=20, height=2, command=start)
start_button.place(x=10, y=50)

def save():
    # 获取当前目录
    current_dir = os.getcwd()

    # 拷贝文件的目标目录
    target_dir = "D:/save"

    # 检查目标目录是否存在，如果不存在则创建
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # 获取目标目录下已存在的文件数量
    existing_files = len(os.listdir(target_dir))

    # 构建新文件名
    new_file_name = f"image{existing_files + 1}.jpg"

    # 拷贝文件
    shutil.copy(os.path.join(current_dir, "image.jpg"), os.path.join(target_dir, new_file_name))

    print("文件拷贝完成！")
    var.set('壁纸已保存至D:\save')

save_button = tk.Button(window, text='保存壁纸', width=20, height=2, command=save)
save_button.place(x=10, y=100)

def next_wallpaper():
    url = 'https://t.mwm.moe/ycy'
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
    var.set('已下一张')

next_button = tk.Button(window, text='下一张壁纸', width=20, height=2, command=next_wallpaper)
next_button.place(x=10, y=150)

qiehuan = tk.Label(window,text='设置切换时间',bg='white', font=('Arial,12'), width=15, height=2)
qiehuan.place(x=10,y=200)

minutes = tk.Entry(window,show=None)
minutes.place(x=10,y=250)

seconds = tk.Entry(window,show=None)
seconds.place(x=10,y=300)

minutes_text = tk.Label(window,text='分',width=5,height=2,bg='white', font=('Arial,12'))
minutes_text.place(x=160,y=250)

seconds_text = tk.Label(window,text='秒',width=5,height=2,bg='white', font=('Arial,12'))
seconds_text.place(x=160,y=300)

def set_time():
    minutes_var = minutes.get()
    seconds_var = seconds.get()
    var.set(str(minutes_var) + '分' + str(seconds_var) + '秒')

    with open("minutes.txt", "w+") as w:
        w.write(str(minutes_var))

    with open("seconds.txt", "w+") as w:
        w.write(str(seconds_var))

set_time_button = tk.Button(window, text='设置切换时间', width=20, height=2, command=set_time)
set_time_button.place(x=10, y=350)

def about():
    about_window = tk.Toplevel()
    about_window.title('肥胖龟壁纸 - 关于软件')
    about_window.geometry('800x100')

    about_text = tk.Label(about_window, text='肥胖龟壁纸：是一款由肥胖龟（隶属于肥胖龟公司及TL工作室）开发的自动二次元壁纸切换软件。', bg='white', font=('Arial', 12))
    about_text.pack()

    about_text_2 = tk.Label(about_window, text='API来源于次元API，可调节切换时间。联系作者：QQ2947158920。', bg='white', font=('Arial', 12))
    about_text_2.pack()

    about_text_3 = tk.Label(about_window, text='Copyright © FATTURTLE INC. & TL Studio 2023；版权所有：肥胖龟公司及TL工作室。', bg='white', font=('Arial', 12))
    about_text_3.pack()

    about_window.mainloop()

about_Button = tk.Button(window,text='关于我们', width=20, height=2, command=about)
about_Button.place(x=10, y=400)

window.mainloop()