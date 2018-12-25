# encoding: utf-8
#@author: chenjunhua
#time: 2018/12/25 16:58

from flask import Blueprint

orders = Blueprint('order', __name__)

@orders.route('/')
def hello_world():
    return 'Hello World!'