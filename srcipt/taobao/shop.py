#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 下午10:27
# @Author  : Chen Junhua
# @File    : shop.py
# @Software: PyCharm

from .service import soups
import time

class Shop():
    def __init__(self, url, browser):
        self.url = url
        self.browser = browser

    def good_page_source(self):
        items = self.browser.find_element_by_class_name('items')
        return items.get_attribute('outerHTML')

    def page_has_goods(self):
        try:
            self.browser.find_element_by_class_name('items')
            return True
        except :
            return False


    def good_links(self):
        goods_link = {}
        page_no = 1
        while True:
            new_url = self.url + '&pageNo={}'.format(page_no)
            self.browser.get(new_url)
            if self.page_has_goods():
                items_DOM = self.good_page_source()
                soup = soups(items_DOM)
                items = soup.select('.items li a')
                for good in items:
                    goods_link[good['href']] = good.get_text().strip()
                page_no += 1
                time.sleep(5)
            else:
                break
        return goods_link

