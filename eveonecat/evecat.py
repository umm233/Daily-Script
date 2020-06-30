#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-06-30 15:50:54
# @Author  : umm233

import requests, threading, os
from bs4 import BeautifulSoup


def download_pics(url, pic_dir, n):
    pic_path = pic_dir + str(n) + '.gif'
    if not os.path.isfile(pic_path):
        r = requests.get(url, headers=headers)
        path = pic_dir + str(n) + '.gif'
        with open(path, 'wb') as f:
            f.write(r.content)
        # 下载完了，解锁
        print('No.{} pic download successfully.'.format(n))
    else:
        print('No.{} pic exist => pass'.format(n))
    thread_lock.release()


def get_max_pic_id():
    url = 'http://motions.cat/top.html'
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'lxml')
    a0 = soup.find_all("a", "eoc-image-link")[0]
    return (int)(a0.attrs['id'])


def main(pic_dir):
    if not os.path.exists(pic_dir):
        os.mkdir("pics")
    # 获取最新图片id
    max_id = get_max_pic_id()
    # 多线程下载
    for n in range(1, max_id + 1):
        pic_id = (4 - len(str(n))) * '0' + str(n)
        url = "http://motions.cat/gif/nhn/{}.gif".format(pic_id)
        print('downloading No.{} pic ...'.format(n))
        # 上锁
        thread_lock.acquire()
        t = threading.Thread(target=download_pics, args=(url, pic_dir, n))
        t.start()
    print('--- End! ---')


if __name__ == '__main__':
    headers = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    # 设置最大线程数，开启5个线程就锁住
    thread_lock = threading.BoundedSemaphore(value=5)
    # 设置下载目录
    pic_dir = "pics/"
    main(pic_dir)
