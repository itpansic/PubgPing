# -*- coding: utf-8 -*-

import urllib
import time
import random
import string
import datetime
import urllib2
from urllib2 import Request, urlopen, URLError, HTTPError

def pingUrl(url):
    try:
        response = urllib2.urlopen(url)
    except HTTPError as e:
        return True
    except URLError as e:
        return False
    else:
        return False


def pingWithNum(strNum):
    if strNum == "1":
        print("---\033[1;32m首尔\033[0m")
        url = "http://dynamodb.ap-northeast-2.amazonaws.com/ping?x="
    elif strNum == "2":
        print("---\033[1;32m新加坡\033[0m")
        url = "http://dynamodb.ap-northeast-1.amazonaws.com/ping?x="
    elif strNum == "3":
        print("---\033[1;32m北京\033[0m")
        url = "http://dynamodb.cn-north-1.amazonaws.com.cn/ping?x="
    i = 0
    column = 0
    amount = 0
    count = 0
    urlTmp = url + ''.join(random.sample(string.ascii_letters + string.digits, 13))
    result = pingUrl(urlTmp)
    while i < 24:
        i = i + 1
        column = column + 1
        t = time.time()
        result = pingUrl(urlTmp)
        if result:
            te = time.time()
            delta = int(round((te - t) * 1000))
            count = count + 1
            amount = amount + delta
            if column < 8:
                print delta, "\t",

            else:
                print delta, "\t"
                column = 0

            continue
        else:
            continue

    if count > 0:
        print "---\033[1;32mavg:      %s\033[0m"%int(round(amount / count)),
    print "\n"

def showInput():
    url = "http://dynamodb.ap-northeast-2.amazonaws.com/ping?x="

    str = None
    while True:
        if str is not None:
            print "输入错误，请重新输出...\n"
        str = raw_input("选择Ping目标：\n0. 全部 \n1. 首尔 \n2. 新加坡\n3. 北京\n")
        if str == "0" or str == "1" or str == "2" or str == "3":
            break;
    if str == "1" or str == "2" or str == "3":
        pingWithNum(str)
    elif str == "0":
        pingWithNum("1")
        pingWithNum("2")
        pingWithNum("3")



while True:
    showInput()


