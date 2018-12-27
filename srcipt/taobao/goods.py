#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 下午10:27
# @Author  : Chen Junhua
# @File    : goods.py
# @Software: PyCharm

from .service import *
from time import sleep
from bs4 import BeautifulSoup


class Good():
    def __init__(self, product_link, product_name, browser):
        self.product_link = product_link
        self.product_name = product_name
        self.pause_time = 10
        self.driver = browser
        self.driver.get(self.product_link)
        try:
            close_button = self.driver.find_element_by_id('sufei-dialog-close')
            close_button.click()
        except:
            print('++++++没有弹框！')
        sleep(self.pause_time)
        self.product_page_html = self.driver.page_source
        self.soup = soups(self.product_page_html)

    def get_content_img_link(self):
        img_link = get_img_link(self.soup, class_ = Config.deitail_picture_class)

        return img_link

    def get_cover_img_link(self):
        img_link = cut_product_img_link(get_img_link(self.soup, id = Config.cover_picture_id))

        return img_link

    def get_detail(self):
        try:
            detail = self.driver.find_element_by_id('attributes')
            file = 'picture/{}/{}'.format(self.product_name, '商品规格.png')
            detail.screenshot(file)
            print('『商品规格』：+++商品规格保存成功')
        except:
            print('『商品规格』：---商品规格保存失败')

    def has_video(self):
        video_node = self.soup('video')
        if len(video_node) == 0:
            return False
        else:
            return True

    def get_vidio_link(self):
        video_link = ''
        if self.has_video():
            video_node = self.soup.find('video')
            video_link_original = video_node.get('src')
            video_link = 'https:{}'.format(video_link_original)

        return video_link

    def store_img(self, img_link_list, img_type):
        for each_img_link in img_link_list:
            picture_content = get_content(each_img_link)
            file_name = '{}{}'.format(img_link_list.index(each_img_link),each_img_link[-4:])
            a = img_link_list.index(each_img_link)
            try:
                store(file_name, self.product_name, picture_content, img_type)
                print('『{}』：+++第『{}』张图保存成功！\n'.format(img_type, img_link_list.index(each_img_link)))
            except:
                print('『{}』---第『{}』张图保存失败！\n---URL: {}\n'.format(img_type, img_link_list.index(each_img_link), each_img_link))

    def store_video(self):
        video_link = self.get_vidio_link()
        if video_link == '':
            print('---该产品没有视频！\n')
        else:
            video_content = get_content(video_link)
            try:
                store('{}.mp4'.format(self.product_name), self.product_name, video_content, '视频')
                print('『视频』：+++视频保存成功！\n')
            except:
                print('『视频』：---视频保存失败！\n')

    def details(self):
        detail_container = self.soup.select('#J_AttrUL li')
        deitails = []
        if len(detail_container):
            for li in detail_container:
                detail = li.text
                deitails.append(detail)

        return deitails