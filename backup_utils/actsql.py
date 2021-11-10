# -*- coding:UTF-8 -*-
# author:wangjian

from redis import Redis,ConnectionPool
from HtmlTestRunner import HTMLTestRunner
from abc import ABCMeta,abstractmethod
import optparse
import pymysql
import time
import os,sys

class DataBase(metaclass=ABCMeta):

    @abstractmethod
    def add(self):
        pass
    
    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def change(self):
        pass
    
    @abstractmethod
    def query(self):
        pass

class ActMysql(DataBase):
    '''action mysql'''
    def __init__(self,host,user,passwd,db,port=3306):
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=passwd,
            database=db,
            port=port,
            charset='utf-8'
        )
        self.cursor = self.conn.cursor()

    def exec_sql(self,sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
            self.close_sql()

    def add(self,sql):
        self.exec_sql(sql)

    def delete(self,sql):
        self.exec_sql(sql)

    def query(self,sql):
        try:
            self.cursor.execute(sql)
            fetchall = self.cursor.fetchall()
        except Exception as e:
            print(e)
            fetchall = e
        finally:
            self.close_sql()
        return fetchall

    def change(self,sql):
        self.exec_sql(sql)

    def close_sql(self):
        self.cursor.close()
        self.conn.close()

class ActRedis(DataBase):
    '''action redis'''
    def __init__(self,host,port,db,passwd):
        self.pool = ConnectionPool(host=host, port=port, password=passwd)
        self.rd = Redis(connection_pool=self.pool,decode_responses=True)

    def add(self,key,val):
        self.rd.set(key,val)

    def delete(self):
        pass

    def change(self):
        pass

    def query(self):
        pass
        
    def __del__(self):
        pass


if __name__ == "__main__":
    pass
