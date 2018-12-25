#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 下午10:18
# @Author  : Chen Junhua
# @File    : service.py
# @Software: PyCharm

import os
import requests


def cut_product_img_link(img_link):
    new_img_link = []
    for link in img_link:
        if '//img.alicdn.com/imgextra/' in link:
            new_link = link.lstrip('//img.alicdn.com/imgextra/').split('_60x60q90.jpg')[0]
            new_img_link.append(new_link)
        elif '_50x50.jpg_.webp' in link:
            new_link = link.split('_50x50.jpg_.webp')[0]
        new_img_link.append(new_link)

    return new_img_link


def store(name, folder, content, type):
    path = make_dictionary(folder, type)
    file = '{}/{}'.format(path, name)
    with open(file, 'wb') as fj:
        fj.write(content)

def make_dictionary(folder, type):
    path = 'picture/{}/{}'.format(folder, type)
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)

    return path

def get_content(url):
    res = requests.get(url)
    content = res.content

    return content

def store_product_link(name, url):
    file = 'picture/{}/url.txt'.format(name)
    try:
        with open(file, 'w') as fj:
            fj.write(url)
            print('『商品链接』：+++商品链接保存成功！')
    except BaseException as e:
        print(e)
        print('『商品链接』：---商品链接保存失败！')

def wait_for_login(browser):
    browser.get('https://www.taobao.com')
    while True:
        a = input('+++淘宝登录成功后,输入任意字符继续: ')
        if a:
            break

