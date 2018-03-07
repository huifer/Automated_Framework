#!/usr/bin/env python
#-*-coding:utf-8-*-
# @Time    : 2018-03-07 19:31
# @Author  : huifer
# @File    : Pressure.py
# @Software: PyCharm
import threading
from time import ctime, sleep
import requests

def pressure(func):
    for i in range(100):
        header= {
            'Host':"www.zhihuihedao.cn",
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',

        }
        r = requests.get("http://www.zhihuihedao.cn",headers=header)
        s =r.status_code
        print(s,r)
        print("round:%s, tread number:%s, returnValue:%s,time:%s" % (i, func, s,ctime()))

        sleep(1)


if __name__ == '__main__':
    threads = []
    for i in range(500):
        name = "t%s" % (i)
        name = threading.Thread(target=pressure, args=(i,))
        threads.append(name)

    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()