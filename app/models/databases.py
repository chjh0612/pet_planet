# encoding: utf-8
#@author: chenjunhua
#time: 2018/12/25 18:51

from app.models import Base, Record_Time, engine
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index ,DateTime, func, Float

# 商品品牌表
class Brands(Base, Record_Time):
    __tablename__ = 'brands'
    name = Column(String(20), comment='品牌名', nullable=False)
    state = Column(Integer, comment='是否上线，0下线，1上线')
    remark = Column(String(128),comment='备注')

    @classmethod
    def brand_id(cls, name, session):
        brand = session.query(cls).filter_by(name=name).first()

        return brand.id

# 商品表
class Goods(Base, Record_Time):
    __tablename__ = 'goods'
    name = Column(String(70), comment='商品名称')
    brand_id = Column(ForeignKey('brands.id'), nullable = False, comment='所属品牌')
    purchasing_price = Column(Float(precision='5, 2'), comment='进价')
    selling_price = Column(Float(precision='5, 2'), comment='出售价格')
    cover_picture = Column(String(200), comment='封面图片')
    video = Column(String(100), comment='视频地址')
    details = Column(String(200), comment='商品详情')
    detail_picture = Column(String(200), comment='详情图片地址')
    category_id = Column(Integer, ForeignKey('categorys.id'), comment='类别规格')
    inventory = Column(Integer, comment='库存')
    state = Column(Integer)
    specification =  Column(String(200), comment='类别规格')
    taobao_name = Column(String(70), comment='淘宝名称')
    taobao_link = Column(String(200), comment='淘宝链接')
    remark = Column(String(128), comment='备注')


class Categorys(Base, Record_Time):
    __tablename__ = 'categorys'
    category_name =Column(String(10))

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

if __name__ == '__main__':
    Base.metadata.create_all(engine)