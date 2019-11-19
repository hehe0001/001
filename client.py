#!/user/bin/env python
#  _*_ coding:utf-8 _*_
import pytest


class Client:
    def assert_equal(first,second):
        try:
            assert first == second
            print("检查点成功，实际结果[{first}]，预期结果[{second}]".format(first=first, second=second))
        except:
            '''此处不写信息，默认捕获所有'''
            print("检查点失败，实际结果[{first}]，预期结果[{second}]".format(first=first, second=second))

# assert_equal(2,3)