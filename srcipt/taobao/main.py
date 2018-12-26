#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 下午10:18
# @Author  : Chen Junhua
# @File    : main.py
# @Software: PyCharm

# from .service import store_product_link, wait_for_login
# from .goods import Good
from selenium import webdriver
# from json import dump, load
from app.models import Session
from app.models.databases import Brands, Goods

chrome_opt = webdriver.ChromeOptions()
# chrome_opt.add_argument("--headless")
browser = webdriver.Chrome(chrome_options=chrome_opt)
browser.implicitly_wait(30)
session = Session()

def run():
    while True:
        brand_name = input('++++++请输入品牌名称：')
        if brand_name:
            break
    new_brand = Brands(name=brand_name, state=0)
    session.add(new_brand)
    session.commit()
    brand_id = Brands.brand_id(brand_name, session)
    good = Goods(
        brand_id = brand_id,
        taobao_name='',
        taobao_link=''
    )


if __name__ == '__main__':
    run()