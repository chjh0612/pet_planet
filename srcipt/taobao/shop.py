#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 下午10:27
# @Author  : Chen Junhua
# @File    : shop.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import time

class Shop():
    def __init__(self, url, browser):
        self.url = url
        self.browser = browser

    def good_page_source(self, url):
        self.browser.get(url)
        page_source = self.browser.page_source

        return page_source

    def good_links(self):
        print('+++开始获取商品链接')
        goods_link = {}
        for i in range(1, 10):
            new_url = self.url + '&pageNo={}'.format(i)
            page = self.good_page_source(new_url)
            if '没找到符合条件的商品,换个条件或关键词试试吧' in page:
                print('+++商品链接获取完毕')
                break
            else:
                soup = BeautifulSoup(page, features="html.parser")
                items = soup.select('.items li a')
                for good in items:
                    goods_link[good['href']] = good.get_text().strip()
                print('+++第{}页获取完毕'.format(i))
            time.sleep(5)

        return goods_link


