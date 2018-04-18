#coding=utf8
import itchat
import datetime
import time
from itchat.content import *

itchat.auto_login(hotReload=True)

users = itchat.search_friends(name='羽暮')
userName = users[0]['UserName']



def timeRun():
    while 1:
        now=datetime.datetime.now()
        now_str = now.strftime('%Y/%m/%d %H:%M:%S')[11:]
        print('\r{}'.format(now_str),end='')
        if now_str in ['13:54:00']:
            itchat.send("下午好啊", toUserName=userName)
        time.sleep(1)




if __name__ == '__main__':
    itchat.auto_login()
    timeRun()
    itchat.run()


