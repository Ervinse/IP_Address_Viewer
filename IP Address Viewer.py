import socket
import requests
import tkinter as tk
from datetime import datetime


# 获取本地IP地址的函数
def get_local_ip():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except Exception as e:
        return f"Error: {str(e)}"


# 获取公共IP地址的函数
def get_public_ip():
    try:
        response = requests.get('http://checkip.amazonaws.com')
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"


# 更新IP地址显示的函数
def update_ips():
    try:
        last_update_time.set("Updated At: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        local_ip.set("Local IP Address: " + get_local_ip())
        public_ip.set("Public IP Address: " + get_public_ip())
    except Exception as e:
        print(f"An error occurred: {str(e)}")


# 实时更新当前时间的函数
def update_current_time():
    current_time.set("Current Time: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    root.after(1000, update_current_time)  # 每秒调用一次自身


# 复制到剪切板的函数
def copy_to_clipboard(content):
    root.clipboard_clear()
    root.clipboard_append(content)
    root.update()


root = tk.Tk()
root.title("IP Address Viewer")
root.minsize(300, 100)

# 初始化StringVar变量
local_ip = tk.StringVar()
public_ip = tk.StringVar()
last_update_time = tk.StringVar()
current_time = tk.StringVar()

# 创建并配置本地IP地址的标签
local_ip_label = tk.Label(root, textvariable=local_ip)
local_ip_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

# 创建并配置复制本地IP地址的按钮
copy_local_ip_button = tk.Button(root, text="Copy Local IP", command=lambda: copy_to_clipboard(get_local_ip()))
copy_local_ip_button.grid(row=0, column=1, padx=10, pady=5)

# 创建并配置公共IP地址的标签
public_ip_label = tk.Label(root, textvariable=public_ip)
public_ip_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)

# 创建并配置复制公共IP地址的按钮
copy_public_ip_button = tk.Button(root, text="Copy Public IP", command=lambda: copy_to_clipboard(get_public_ip()))
copy_public_ip_button.grid(row=1, column=1, padx=10, pady=5)

# 创建并配置上次更新时间的标签
last_update_time_label = tk.Label(root, textvariable=last_update_time)
last_update_time_label.grid(row=2, column=0, columnspan=2, sticky=tk.W, padx=10, pady=5)

# 创建并配置当前时间的标签（修复部分）
current_time_label = tk.Label(root, textvariable=current_time)
current_time_label.grid(row=3, column=0, columnspan=2, sticky=tk.W, padx=10, pady=5)

# 创建并配置“更新IP”按钮
update_button = tk.Button(root, text="Update IPs", command=update_ips)
update_button.grid(row=4, column=0, columnspan=2, pady=10)

update_ips()  # 初始运行时更新IP地址
update_current_time()  # 启动实时更新当前时间

root.mainloop()
