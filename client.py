#!/user/bin/env python
#  _*_ coding:utf-8 _*_
<<<<<<< HEAD
import requests


class Client():
    dawn_url = 'https://t-user.120yibao.com/api/'
    TOKEN = '0926fb15-d352-472c-b808-f296618c92fb'
    DB = None
    DATA = {}

    def __init__(self, url, headers, method, type=0):
        self.url = url
        self.method = method
        self.type = type
        self.headers = {}
        self.res = None
        self.flag = 0
        self._type_equality_funcs = {}
        self.data = {}

    @property
    def status_code(self):
        return self.res.status_code

    # @property
    # def status(self):
    #     return self.res.status
    @property
    def text(self):
        return self.res.text

    @property
    def json(self):
        return self.res.json()

    @property
    def times(self):
        return (int(round(self.res.elapsed.total_seconds() * 1000)))

    def set_header(self, key, value):
        self.headers[key] = value

    def set_data(self, dic):
        # self.data = dic
        if isinstance(dic, dict):
            self.data = dic
        else:
            raise Exception("请求的参数请以字典格式传递")

    def send(self):
        if self.method == "GET":
            self.res = requests.get(url=self.url, headers=self.headers, params=self.data)
        elif self.method == "POST":
            if self.type == 1:
                self.res = requests.post(url=self.url, headers=self.headers, data=self.data)
            elif self.type == 5:
                self.res = requests.post(url=self.url, headers=self.headers, data=self.data)
            elif self.type == 2:
                self.set_header('Content-Type', 'application/x-www-form-urlencoded')
                self.res = requests.post(url=self.url, cookies=self.headers, data=self.data)
            elif self.type == 3:
                self.set_header = ('Content-Type', 'text/xml')
                xml = self.data.get('xml')
                if xml:
                    self.res = requests.post(url=self.url, headers=self.headers, data=xml)
                else:
                    raise Exception('xml正文，入参格式：{"xml":"xxx"}')
            elif self.type == 4:
                self.set_header('Content-Type', 'application/json')
                # self.data = json.dumps(self.data)
                self.res = requests.post(url=self.url, headers=self.headers, json=self.data)
            elif self.type == 0:
                self.res = requests.post(url=self.url, headers=self.headers)
            else:
                raise Exception("正文格式不支持")
        else:
            raise Exception("请求的方法类型不支持")

    # 传值
    def save(self, name, value):
        Client.DATA[name] = value

    # 取值
    def value(self, name):
        return Client.DATA.get(name)

    def equal(self, first, second):
        try:
            self.assertEqual(first, second)
=======
import pytest


class Client:
    def assert_equal(first,second):
        try:
            assert first == second
>>>>>>> 999
            print("检查点成功，实际结果[{first}]，预期结果[{second}]".format(first=first, second=second))
        except:
            '''此处不写信息，默认捕获所有'''
            print("检查点失败，实际结果[{first}]，预期结果[{second}]".format(first=first, second=second))
<<<<<<< HEAD
            self.flag = + 1

    def less_than(self, first, second):
        try:
            self.assertLess(first, second)
            print("检查点成功，实际结果[{first}]，预期结果[<{second}]".format(first=first, second=second))
        except:
            '''此处不写信息，默认捕获所有'''
            print("检查点失败，实际结果[{first}]，预期结果[<{second}]".format(first=first, second=second))
            self.flag = + 1

    # def db_execute1(self, sql):
    #     cursor = Client.DB.cursor()
    #     cursor.execute(sql)
    #     Client.DB.commit()
    #
    # def db_equal1(self, first, sql):
    #     cursor = Client.DB.cursor()
    #     cursor.execute(sql)
    #     result = cursor.fetchone()[0]
    #     try:
    #         self.assertEqual(first, result)
    #         print("检查点成功，实际结果[{first}]，预期结果[{sql}]".format(first=first, sql=result))
    #     except:
    #         '''此处不写信息，默认捕获所有'''
    #         print("检查点失败，实际结果[{first}]，预期结果[{sql}]".format(first=first, sql=result))
    #         self.flag = + 1

    # def db_equals(self, first, sql):
    #     cursor = Client.DB.cursor()
    #     cursor.execute(sql)
    #     result = cursor.fetchall()
    #     try:
    #         self.assertEqual(first, result)
    #         print("检查点成功，实际结果[{first}]，预期结果[{sql}]".format(first=first, sql=result))
    #     except:
    #         '''此处不写信息，默认捕获所有'''
    #         print("检查点失败，实际结果[{first}]，预期结果[{sql}]".format(first=first, sql=result))
    #         self.flag = + 1

    def result(self):
        '''检查结果确认'''
        # Client.DB.close()
        if self.flag > 0:
            # self.assertTrue(False)
            self.assertTrue(False, '断言出现错误')
            # raise Exception('断言出现错误')

    def is_contain(self, str_one, str_two):
        '''
        判断一个字符串是否在另一个字符串中
        :param str_one:查找的字符串
        :param str_two:被查找的字符串
        :return:
        '''
        flag = None
        # if isinstance(str_one,unicode):
        # str_one = str_one.encode('unicode-escape').decode('string_escape')
        if str_one in str_two:
            flag = True
            print("检查点成功，实际结果[{str_one}]，预期结果[{str_two}]".format(str_one=str_one, str_two=str_two))
        else:
            flag = False
            print("检查点失败，实际结果[{str_one}]，预期结果[{str_two}]".format(str_one=str_one, str_two=str_two))
        # return flag

    def is_contain_result(self, str_one, str_two):
        '''包含结果判断'''
        cli = Client(self, str_one, str_two)
        result = cli.is_contain(str_one, str_two)
        if result:
            try:
                cli.is_contain(str_one, str_two)
                print("检查点成功，实际结果[{str_one}]，预期结果[{str_two}]".format(str_one=str_one, str_two=str_two))
            except:
                '''此处不写信息，默认捕获所有'''
                print("检查点失败，实际结果[{str_one}]，预期结果[{str_two}]".format(str_one=str_one, str_two=str_two))


class Method:
    GET = 'GET'
    POST = 'POST'


class Type:
    FORM = 1
    URL_ENCODE = 2
    XML = 3
    JSON = 4
    FILE = 5
=======

# assert_equal(2,3)
>>>>>>> 999
