# coding:utf-8
# author by @xiaoyusilen

import MySQLdb
import ConfigParser

'''
MySQL connect select insert update delete operate
'''

# 连接线上数据库，用于查询
class MySQL(object):
    error_code = ''  # MySQL错误码
    _instance = None  # 实例
    _conn = None  # 数据库连接
    _cur = None  # 游标

    _TIMEOUT = 30  # 默认超时时间
    _timecount = 0

    def __init__(self):
        # 数据库配置
        self.conf = ConfigParser.ConfigParser()
        self.conf.read('config.conf')
        print self.conf.get("mysql", 'mysql_host')
        dbconfig = {
            'host': self.conf.get("mysql", "mysql_host"),
            'port': self.conf.getint("mysql", "mysql_port"),
            'user': self.conf.get("mysql", "mysql_user"),
            'passwd': self.conf.get("mysql", "mysql_passwd"),
            'db': self.conf.get("mysql", "mysql_db"),
            'charset': self.conf.get("mysql", "mysql_charset"),
        }
        # 创建MySQL连接
        try:
            self._conn = MySQLdb.connect(host=dbconfig['host'],
                                         port=dbconfig['port'],
                                         user=dbconfig['user'],
                                         passwd=dbconfig['passwd'],
                                         db=dbconfig['db'],
                                         charset=dbconfig['charset'])
        except MySQLdb.Error, e:
            self.error_code = e.args[0]
            error_msg = 'MySQL error!', e.args[0], e.args[1]
            print error_msg

            if self._timecount < self._TIMEOUT:
                interval = 5
                self._timecount += interval
                return self.__init__(dbconfig)
            else:
                raise Exception(error_msg)

        self._cur = self._conn.cursor()
        self._instance = MySQLdb

    def query(self,sql):
        # 执行select语句
        try:
            self._cur.execute("set names utf8")
            query_result = self._cur.execute(sql)
        except MySQLdb.Error, e:
            self.error_code = e.args[0]
            print "Error:MySQL Error Code ", e.args[0], e.args[1]
            query_result = False
        return query_result

    def update(self,sql):
        # 执行update语句
        try:
            self._cur.execute("set names utf8")
            update_result = self._cur.execute(sql)
            self._conn.commit()
        except MySQLdb.Error, e:
            self.error_code = e.args[0]
            print "Error:MySQL Error Code ",e.args[0],e.args[1]
            update_result = False
        return update_result

    def insert(self, sql):
        # 执行insert语句
        try:
            self._cur.execute("set names utf8")
            insert_result = self._cur.execute(sql)
            self._conn.commit()
        except MySQLdb.Error, e:
            self.error_code = e.args[0]
            print "Error:MySQL Error Code ", e.args[0], e.args[1]
            insert_result = False
        return insert_result

    def delete(self, sql):
        # 执行delete语句
        try:
            self._cur.execute("set names utf8")
            delete_result = self._cur.execute(sql)
            self._conn.commit()
        except MySQLdb.Error, e:
            self.error_code = e.args[0]
            print "Error:MySQL Error Code ", e.args[0], e.args[1]
            delete_result = False
        return delete_result

    def fetchAllRows(self):
        # 返回select结果列表
        return self._cur.fetchall()

    def fetchOneRow(self):
        # 返回一行结果，然后游标指向下一行，到达最后一行以后，返回None
        return self._cur.fetchone()

    def getRowCount(self):
        # 获取结果行数
        return int(self._cur.rowcount)

    def commit(self):
        # 提交数据库操作（upate,insert,delete）
        return self._cur.commit()

    def rollback(self):
        # 数据库回滚操作
        return self._cur.rollback()

    def __del__(self):
        # 释放资源
        try:
            self._cur.close()
            self._conn.close()
        except:
            pass

    def close(self):
        # 关闭数据库连接
        self.__del__()

if __name__ == '__main__':
    # import requests
    import json
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')