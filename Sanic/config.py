import os
from urllib import parse


class Config:
    class Mongodb:
        # 数据库账户名
        username = parse.quote_plus('root')
        # 数据库密码
        password = parse.quote_plus('')
        # 数据库地址
        db_host = parse.quote_plus('localhost:27017')
