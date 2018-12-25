#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 下午10:18
# @Author  : Chen Junhua
# @File    : main.py
# @Software: PyCharm

from .service import store_product_link, wait_for_login
from .goods import Good
from selenium import webdriver
from json import dump, load

if __name__ == '__main__':
    chrome_opt = webdriver.ChromeOptions()
    # chrome_opt.add_argument("--headless")
    browser = webdriver.Chrome(chrome_options=chrome_opt)
    url = 'https://pidan.tmall.com/search.htm?spm=a1z10.3-b-s.w4011-16379494030.72.298d6435C2AzyR&search=y&viewType=list&tsearch=y'
    wait_for_login(browser)
    # shop = Shop(url, browser)
    # good_links = shop.good_links()
    with open('pidanlinks.json', 'r') as fj:
        good_links = load(fj)
    for good_link in good_links.keys():
        NAME = good_links.get(good_link)
        URL = 'https:{}'.format(good_link)
        print(URL)
        good = Good(URL, NAME, browser)
        good.store_video()
        good.store_img(good.get_product_img_link(), '产品图')
        good.store_img(good.get_content_img_link(), '商品详情图')
        good.get_detail()
        store_product_link(NAME, URL)
