import chardet
from bson.objectid import ObjectId
from urllib import parse
from pymongo import MongoClient
port = 27017
host = 'localhost'
user_name = 'aaa'
db_name = 'aaa'
passwd = 'aaa'
passwd = parse.quote(passwd)  # 对密码先进行编码


def conn_mongo(coll_name):
    mango_uri = 'mongodb://%s:%s@%s:%s/%s' % (user_name, passwd, host, port, db_name)  # 链接时需要指定数据库
    conn = MongoClient(mango_uri)  # 创建链接
    db = conn[db_name]  # 连接coder数据库
    mongodata=db[coll_name]
    return mongodata


if __name__ == '__main__':
    conn_mongo()
