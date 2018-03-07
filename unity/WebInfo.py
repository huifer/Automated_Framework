#!/usr/bin/env python
# -*-coding:utf-8-*-
# @Time    : 2018-03-07 18:06
# @Author  : huifer
# @File    : WebInfo.py
# @Software: PyCharm
import requests
import socket

from lxml import etree


class WebInfo(object):
    def __init__(self, url):
        self.url = url

    def get_ip(self):
        """
        网站IP查询
        :return:网站IP
        """
        if 'http' in str(self.url):
            url = self.url.split('//')[1]
            ip = socket.gethostbyname(url)
        else:
            ip = socket.gethostbyname(self.url)
        return ip

    def get_server(self):
        """
        获取服务器信息
        :return: 服务器信息
        """

        if 'http' in str(self.url):
            http_url = self.url
            https_url = self.url
        else:
            http_url = 'http://' + str(self.url)
            https_url = 'https://' + str(self.url)
        try:
            re_header = requests.get(http_url).headers
        except:
            re_header = requests.get(https_url).headers
        try:
            server = re_header['server']
        except:
            server = 'unknow'
        return server

    def get_whois(self):
        """
        通过http://whois.chinaz.com/ 返回whois
        :return: whois
        """
        domain = 'http://whois.chinaz.com/' + self.url
        r = requests.get(domain)
        html = r.text
        doc = etree.HTML(html)
        domain_name = doc.xpath('//*[@id="sh_info"]/li[1]/div[2]/p[1]/a[1]/text()')
        Registrar = doc.xpath('//*[@id="sh_info"]/li[2]/div[2]/div/span/text()')
        Contact = doc.xpath('//*[@id="sh_info"]/li[3]/div[2]/span/text()')
        Contact_email = doc.xpath('//*[@id="sh_info"]/li[4]/div[2]/span/text()')
        Create_time = doc.xpath('//*[@id="sh_info"]/li[5]/div[2]/span/text()')
        Expiration = doc.xpath('//*[@id="sh_info"]/li[6]/div[2]/span/text()')
        return (domain_name, Registrar, Contact, Contact_email, Create_time, Expiration)
        pass


if __name__ == "__main__":
    web = WebInfo('http://www.baidu.com')
    print("网站IP \t\t", web.get_ip())
    print("网站服务器 \t", web.get_server())
    print(web.get_whois())
