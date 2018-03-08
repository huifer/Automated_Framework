#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Browser.py
# @Author: huifer
# @Date  : 2018-3-8
from selenium import webdriver
from utils._config import *


class Driver(object):
    def __init__(self):
        self.browser = webdriver.Firefox()
        pass

    def open_browser(self):
        self.browser.maximize_window()
        url = Config().get_config().get('testurl')[0]['url']
        self.browser.get(url)
        return self.browser
        pass

    def close_browser(self):
        self.browser.quit()
        pass


if __name__ == '__main__':
    # a = config.get_config().get('testurl')[0]
    # print(a)
    Driver().open_browser()
