import requests
import time
import os

def str_index(num):
    if num<=9:
        return f"0{num}" 
    return str(num)

def download_image(url,file_path):
    flag = 0
    try:
        with open(file_path,'wb') as img:
            content = requests.get(url).content
            img.write(content)
        return True
    except:
        flag+=1
        if flag > 3:
            print("ERROR:" + url)
            return False
        time.sleep(2)
        download_image(url,file_path)

def traverse_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        pass