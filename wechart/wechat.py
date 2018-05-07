#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests


# bot = Bot()
bot=Bot(console_qr=2,cache_path="botoo.pkl")
#bot=Bot()

def send_news():
    try:
        my_friend = bot.friends().search(u'苏小凡')[0]    #你朋友的微信名称，不是备注，也不是微信帐号。
        my_friend.send("你好")
        # t = Timer(86400, send_news)
        # t.start()
    except:
        my_friend = bot.friends().search('苏小凡')[0]
        my_friend.send(u"今天消息发送失败了")

if __name__ == "__main__":
    send_news()