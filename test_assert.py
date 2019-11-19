#!/user/bin/env python
#  _*_ coding:utf-8 _*_
import pytest
from client import Client
import allure
import requests


@allure.feature('test')
class TestA:
    def setup_class(self):
        print('1111')
    def test_01(self):
        url = 'https://t-user.120yibao.com/api/user/patient/list'
        headers = {'token': '0926fb15-d352-472c-b808-f296618c92fb'}
        res = requests.get(url=url,headers = headers)
        data = res.json()['data']
        Client.assert_equal(len(data),3)

        # Test.assert_equal(1,2)
        Client.assert_equal(2,2)
    def teardown_class(self):
        print('222')




