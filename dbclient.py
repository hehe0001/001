#!/user/bin/env python
#  _*_ coding:utf-8 _*_
from xml.etree import ElementTree as ET
import pymysql
from client import Client


class ClientDB:
    DB = pymysql.connect('118.178.95.142',
                            'heyuju',
                            'XzBdjMSOhr5foPIRlNEk',
                            'yibao_health')

    def db_execute(self,sql):
        cursor = ClientDB.DB.cursor()
        s = cursor.execute(sql)
        ClientDB.DB.commit()
        return s

    def db_equal(self, first, sql):
        cursor = ClientDB.DB.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()[0]
        try:
            self.assertEqual(first, result)
            print("检查点成功，实际结果[{first}]，预期结果[{sql}]".format(first=first, sql=result))
        except:
            '''此处不写信息，默认捕获所有'''
            print("检查点失败，实际结果[{first}]，预期结果[{sql}]".format(first=first, sql=result))
            self.flag = + 1
