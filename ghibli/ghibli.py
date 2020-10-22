#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : umm233

import requests, threading, os
from bs4 import BeautifulSoup


def download_pics(url, pic_dir, n):
    pic_path = pic_dir + str(n) + '.jpg'
    if not os.path.isfile(pic_path):
        r = requests.get(url, headers=headers)
        path = pic_dir + str(n) + '.jpg'
        with open(path, 'wb') as f:
            f.write(r.content)
        # 下载完解锁
        print('No.{} pic download successfully.'.format(n))
    else:
        print('No.{} pic exist => pass'.format(n))
    thread_lock.release()


def main(ca):
    pic_dir = ca + "/"
    if not os.path.exists(pic_dir):
        os.mkdir(pic_dir)
    max_id = 50
    # 多线程下载
    for n in range(1, max_id + 1):
        pic_id = (3 - len(str(n))) * '0' + str(n)
        url = "http://www.ghibli.jp/gallery/"+ca+"{}.jpg".format(pic_id)
        print('downloading {}-No.{} pic ...'.format(ca,n))
        # 上锁
        thread_lock.acquire()
        t = threading.Thread(target=download_pics, args=(url, pic_dir, n))
        t.start()


if __name__ == '__main__':
    headers = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    # 设置最大线程数
    thread_lock = threading.BoundedSemaphore(value=5)
    # 设置下载分类
    pic_ca = ["karigurashi", "kokurikozaka", "kazetachinu", "kaguyahime", "marnie","ged","chihiro", "ponyo", "baron", "mononoke", "howl", "mimi", "yamada", "ghiblies"]
    for ca in pic_ca:
        print("=== 开始下载 {} 分类 ===".format(ca))
        pic_dir = ca + "/"
        main(ca)
        print("=== 分类 {} 下载完成 ===".format(ca))
