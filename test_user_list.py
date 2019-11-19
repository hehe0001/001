#!/user/bin/env python
#  _*_ coding:utf-8 _*_
import requests
from client import Client
from dbclient import ClientDB
import allure


class TestUserList:

    def setup_class(self):
        self.url = Client.dawn_url+ 'user/patient/list'
        self.token = Client.TOKEN
        self.headers = {'token':Client.TOKEN}


    @allure.feature('患者列表')
    @allure.story('接口')
    def test_userlist(self):
        """列表信息"""
        res = requests.get(url=self.url,headers = self.headers)
        # print(res.json())

        assert res.status_code,200
        data = res.json()['data']
        # print(len(data))
        db = ClientDB()
        s = db.db_execute('select * from yb_patient where user_id = 91778')
        # print(s)
        assert len(data),s

    def teardown_class(self):
        ClientDB.DB.close()



