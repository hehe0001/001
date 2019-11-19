#!/user/bin/env python
#  _*_ coding:utf-8 _*_

import pymysql

db = pymysql.connect('118.178.95.142',
                     'heyuju',
                     'XzBdjMSOhr5foPIRlNEk',
                     'yibao_health')

cursor = db.cursor()

s = cursor.execute('select * from yibao_health.yb_patient where user_id=91778')
db.commit()
print(s)
print(type(s))
