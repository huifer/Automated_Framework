#!/usr/bin/env python
# -*-coding:utf-8-*-
# @Time    : 2018-03-05 20:28
# @Author  : huifer
# @File    : TESTrun.py
# @Software: PyCharm
import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from src.yzm.yzm_result import yzm
from unity.LogHandler import LogHandler

class Slide(object):
    def __init__(self, url='http://www.zhihuihedao.cn/login.jsp'):
        self.driver = webdriver.Firefox()
        self.url = "http://www.zhihuihedao.cn/login.jsp"
        self.wait = WebDriverWait(self.driver, 10)
        self.log = LogHandler("Framework")

    def run(self, pic_name='1.png'):
        self.driver.get(self.url)
        action = ActionChains(self.driver)

        # 滑块验证码
        # dragger = self.driver.find_element_by_class_name("handler")

        bg_pic = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,
                                                                 "validate-image")))
        # 截图数据获取
        top, bottom, left, right = (
            bg_pic.location['y'], bg_pic.location['y'] + bg_pic.size['height'],
            bg_pic.location['x'], bg_pic.location['x'] + bg_pic.size['width'])
        time.sleep(1)
        cp1 = self.crop(left, top, right, bottom, pic_name)
        yzm_res = yzm(pic_name)

        self.driver.find_element_by_xpath('//*[@id="userNameInput"]').send_keys('user')
        self.driver.find_element_by_xpath('//*[@id="passwordInput"]').send_keys('pwd')
        self.driver.find_element_by_xpath('//*[@id="validateCode"]').send_keys(yzm_res)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/ul/li[5]/a').click()
        self.log.info("test")
        # 不同速度移动
        # x = 0
        # while x < 50:
        #     x += random.randint(1, 30)
        #     action.click_and_hold(dragger).move_by_offset(x, 0).perform()

    def crop(self, left, top, right, bottom, pic_name):
        """截图函数"""
        ss = Image.open(BytesIO(self.driver.get_screenshot_as_png()))
        cp = ss.crop((left, top, right, bottom))
        cp.save(pic_name)
        return cp

    def __del__(self):
        # self.driver.quit()
        pass

if __name__ == '__main__':
    Slide().run()
