import os
from datetime import datetime


class Config(object):
    now = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    ROOT =os.path.dirname(os.path.abspath(__file__))
    LOG_NAME = os.path.join(ROOT, 'logs','file-{}.log').format(now)
    JSON_AS_ASCII = False  

    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PWD = '12345678'
    DBNAME = 'tars'


    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(MYSQL_USER, MYSQL_PWD,MYSQL_HOST,MYSQL_PORT,DBNAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False



