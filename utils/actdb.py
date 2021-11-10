# -*- coding:UTF-8 -*-
# author:wangjian

from redis import StrictRedis,ConnectionPool
import optparse
import pymysql
import time
import os,sys

class ActMysql(object):
    '''action mysql'''
    def __init__(self,host,user,passwd,db):
        try:
            self.conn = pymysql.connect(host=host,user=user,password=passwd,database=db)
        except Exception as e:
            print(e)
        self.cursor = self.conn.cursor()

    def exec_sql(self,sql):
        fetchall = None
        i = 0
        while i<3:
            try:
                self.cursor.execute(sql)
                fetchall = self.cursor.fetchall()
                break
            except Exception as e:
                print(f"select data failed! reason:{e}")
                i+=1
        return fetchall

    def insertData(self,sql):
        pass

    def __del__(self):
        self.cursor.close()
        self.conn.close()

class ActRedis(object):
    '''action redis'''
    def __init__(self,args):
        try:
            self.pool = ConnectionPool(host=args['host'], port=args['port'], db=args['db'], password=args['password'])
        except:
            self.pool = ConnectionPool.from_url(args)
        self.redis = StrictRedis(connection_pool=self.pool)

    def exec_sql(self,tp,key,value):
        if tp == 'set':
            self.redis.set(key,value)
        if tp == 'get':
            self.redis.get(key)

    def __del__(self):
        pass


if __name__ == "__main__":
    tdict = {'host':'localhost', 'port':6379, 'db':0, 'password':'foobared'}
    ar = ActRedis(tdict)
