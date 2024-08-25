import os
# import psycopg2
import pymysql


basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
     SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/db_hotel'
     SQLALCHEMY_TRACK_MODIFICATIONS = False
# class Config:
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:admin@localhost/db_hotel'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

