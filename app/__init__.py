# encoding: utf-8
#@author: chenjunhua
#time: 2018/12/25 16:46

from flask import Flask
from app.api import config_blueprint


#将创建app的动作封装成一个函数
def create_app():
    # 创建app实例对象
    app = Flask(__name__)

    # 配置蓝本
    config_blueprint(app)

    # 返回app实例对象
    return app