#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 接口自动化测试.py
# @Author: huifer
# @Date  : 2018-3-6
import json

import requests
import unittest
from urllib import parse


# url = "http://127.0.0.1:8060/api/v1.0/"
# ins = parse.urljoin(url, 'getall')
# print(ins)
# r = requests.get(ins)
# print(r.json()['status'])


class GetEventListTest(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:8060/api/v1.0/"

    @unittest.skip('暂时test_get_data_all的测试')
    def test_get_data_all(self):
        """查询所有"""
        ins = parse.urljoin(self.url, 'getall')
        r = requests.get(ins)
        result = r.json()
        self.assertEqual(result['status']['code'], 200)
        self.assertEqual(result['status']['message'], "OK")

    @unittest.skip('暂时test_get_data_one的测试')
    def test_get_data_one(self):
        ins = parse.urljoin(self.url, 'getid/2')
        r = requests.get(ins)
        result = r.json()
        self.assertEqual(result['status']['code'], 200)
        self.assertEqual(result['status']['message'], "OK")
        self.assertEqual(result['data']['description'], "Need to find a good Python tutorial on the web")
        self.assertEqual(result['data']['done'], False)
        self.assertEqual(result['data']['id'], 2)
        self.assertEqual(result['data']['title'], "Learn Python")

    @unittest.skip('暂时跳过test_del_one用例2的测试')
    def test_del_one(self):
        ins = parse.urljoin(self.url, 'delone/1')
        r = requests.delete(ins)
        result = r.json()
        self.assertEqual(result['status']['code'], 204)
        self.assertEqual(result['status']['message'], "NO CONTENT")

    @unittest.skip('暂时跳过test_create_one用例2的测试')
    def test_create_one(self):
        ins = parse.urljoin(self.url, 'create')
        payload = {u"title": 123}
        headers = {'Content-Type': 'application/json',
                   'accept': "application/json"
                   }

        r = requests.post(ins, data=json.dumps(payload), headers=headers, verify=False)


    def test_authenticate(self):
        ins = parse.urljoin(self.url, 'sec')
        r = requests.get(ins, auth=('admin', 'admin'))
        result = r.json()
        self.assertEqual(result['status']['code'], 200)
        self.assertEqual(result['status']['message'], "OK")



if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(GetEventListTest("test_authenticate"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
