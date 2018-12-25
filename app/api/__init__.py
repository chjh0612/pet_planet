# encoding: utf-8
#@author: chenjunhua
#time: 2018/12/25 16:47

from app.api.orders.orders import orders
from app.api.personal.personal import personal
from app.api.public.public import public
from app.api.search.search import search

DEFAULT_BLUEPRINT = (
    (orders, '/'),
    (personal,'/'),
    (public,'/'),
    (search, '/')

)

# 封装配置蓝本的函数
def config_blueprint(app):
    # 循环读取元组中的蓝本
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)