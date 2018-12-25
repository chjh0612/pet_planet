#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 下午10:27
# @Author  : Chen Junhua
# @File    : goods.py
# @Software: PyCharm

from .service import *
import time
from bs4 import BeautifulSoup

class Good():
    def __init__(self, product_link, product_name, browser):
        self.product_link = product_link
        self.product_name = product_name
        self.pause_time = 10
        # self.chrome_opt = webdriver.ChromeOptions()
        # #self.chrome_opt.add_argument("--headless")
        # self.driver = webdriver.Chrome(chrome_options = self.chrome_opt)
        self.driver = browser
        self.content_img_div_class = 'content'
        self.product_img_div_id = 'J_UlThumb'
        self.driver.get(self.product_link)
        close_button = self.driver.find_element_by_id('sufei-dialog-close')
        close_button.click()
        time.sleep(self.pause_time)
        self.product_page_html = self.driver.page_source.encode('utf-8')
        self.soup = BeautifulSoup(self.product_page_html, 'html.parser')

    def get_img_link(self, **params):
        img_container = self.soup.find(**params)
        all_img_node = img_container.find_all('img')
        img_link = []
        for each_img_node in all_img_node:
            link = ''
            if 'data-ks-lazyload' in each_img_node:
                link = each_img_node.get('data-ks-lazyload')
            else:
                link = each_img_node.get('src')
            if 'https:' not in link:
                link = 'https:{}'.format(link)
            img_link.append(link)

        return img_link

    def get_content_img_link(self):
        img_link = self.get_img_link(class_ = self.content_img_div_class)

        return img_link

    def get_product_img_link(self):
        img_link = cut_product_img_link(self.get_img_link(id = self.product_img_div_id))

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

if __name__ == '__main__':
    cut_product_img_link('//img.alicdn.com/imgextra11111')