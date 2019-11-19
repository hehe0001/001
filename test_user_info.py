#!/user/bin/env python
#  _*_ coding:utf-8 _*_
# @Author:hehe

import pytest
import requests
from client import Client
import allure


class TestUserInfo:

    def setup_class(self):
        self.url = Client.dawn_url + 'user/info'
        self.token = Client.TOKEN
        self.headers = {'token': self.token}

    @allure.feature('userinfo')
    @allure.story('用户信息接口')
    def test_user_info(self):
        """test01"""
        res = requests.get(url=self.url, headers=self.headers)
        # print(res.json())
        Client.assert_equal(res.status_code, 200)
        # assert res.status_code, 200
        # print(res.json()['data'])
        Client.assert_equal(res.json()['data']['id'], 91778)
        # assert res.json()['data']['id'], 91778
        Client.equal(res.json()['data']['token'], self.token)
        # assert res.json()['data']['token'], self.token
        # assert 0

    def test_01(self):
        assert 1
