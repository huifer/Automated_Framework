#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : webtest.py
# @Author: huifer
# @Date  : 2018-3-8
from selenium import webdriver
import unittest

import time


class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.msg = 'python'
        self.url = 'http://www.baidu.com'

    def test_Search(self):
        """
        :return:
        """
        # open browser
        self.driver.get(self.url)
        time.sleep(3)
        # click search input
        self.driver.find_element_by_id('kw').click()
        time.sleep(1)

        # input value
        self.driver.find_element_by_id('kw').send_keys(self.msg)
        time.sleep(1)
        self.driver.find_element_by_id('su').click()
        time.sleep(1)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
