# encoding: utf-8
#@author: chenjunhua
#time: 2018/12/25 18:51

from app.models import Base, Record_Time, engine
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index ,DateTime, func, Float

# 商品品牌表
class Brands(Base, Record_Time):
    __tablename__ = 'brands'
    name = Column(String(20))
    state = Column(Integer)
    remark = Column(String(128))

# 商品表
class Goods(Base, Record_Time):
    __tablename__ = 'goods'
    name = Column(String(70))
    brand_id = Column(ForeignKey('brands.id'), nullable = False)
    purchasing_price = Column(Float(precision='5, 2'))
    selling_price = Column(Float(precision='5, 2'))
    cover_picture = Column(String(200))
    video = Column(String(100))
    details = Column(String(200))
    detail_picture = Column(String(200))
    category_id = Column(Integer)
    inventory = Column(Integer)
    parameter =  Column(String(200))
    state = Column(Integer)
    specification =  Column(String(200))
    remark = Column(String(128))

Base.metadata.create_all(engine)

# # 用户表
# class Users(Base, Record_Time):
#     pass
#
# # 登录历史
# class Login_historys(Base, Record_Time):
#     pass
#
# # 订单表
# class Orders(Base, Record_Time):
#     pass
#
# #支付信息表
# class Payments(Base, Record_Time):
#     pass
#
# #退款表
# class Refounds(Base, Record_Time):
#     pass
# # 评价表
# class Comments(Base, Record_Time):
#     pass


Base.metadata.create_all(engine)