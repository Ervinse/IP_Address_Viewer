import socket
import requests
import tkinter as tk


# 获取本地IP地址的函数
def get_local_ip():
    hostname = socket.gethostname()  # 获取当前设备的主机名
    local_ip = socket.gethostbyname(hostname)  # 根据主机名获取本地IP地址
    return local_ip


# 获取公共IP地址的函数
def get_public_ip():
    response = requests.get('http://checkip.amazonaws.com')  # 发送请求到Amazon的IP检查服务
    return response.text.strip()  # 清除响应文本的前后空格并返回


# 更新IP地址显示的函数
def update_ips():
    local_ip_label.config(text="Local IP Address: " + get_local_ip())  # 更新本地IP地址标签的文本
    public_ip_label.config(text="Public IP Address: " + get_public_ip())  # 更新公共IP地址标签的文本


root = tk.Tk()
root.title("IP Address Viewer")  # 设置窗口标题

# 设置窗口的最小尺寸
root.minsize(300, 100)

# 创建并配置本地IP地址的标签
local_ip_label = tk.Label(root, text="Local IP Address: ")
local_ip_label.pack()

# 创建并配置公共IP地址的标签
public_ip_label = tk.Label(root, text="Public IP Address: ")
public_ip_label.pack()

# 创建并配置“更新IP”按钮，点击时会调用update_ips函数
update_button = tk.Button(root, text="Update IPs", command=update_ips)
update_button.pack()

update_ips()  # 初始运行时更新IP地址

root.mainloop()  # 启动tkinter事件循环
