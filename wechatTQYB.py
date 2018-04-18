import itchat
import datetime
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup

itchat.auto_login(hotReload=True)

users = itchat.search_friends(name='青青')
userName = users[0]['UserName']

def get_page():
    response = urlopen('http://www.weather.com.cn/weather/101230201.shtml')
    soup = BeautifulSoup(response,'html.parser')
    # 获取当天的天气预报标签，本来想用这个的 <li class="sky skyid lv3 on">，结果发现这个标签的class居然不是固定的
    tagWeather=soup.find('ul', class_="t clearfix")
    date = tagWeather.h1.string
    wea = tagWeather.p.string

    # 获取当天温度的标签
    tagTemperature = soup.find('p', class_="tem")
    temperatureHigh=tagTemperature.span.string
    temperatureLOW = tagTemperature.i.string

    #获取当天风级
    tagWind=soup.find('p',class_="win")
    winL=tagWind.i.string

    str = '厦门： %s \n天气 ：%s \n最高气温： %s\n' \
          '最低气温： %s\n风级： %s\n' % (date, wea, temperatureHigh, temperatureLOW, winL)
    return  str

def timeRun():

    while 1:
        now=datetime.datetime.now()
        now_str = now.strftime('%Y/%m/%d %H:%M:%S')[11:]
        print('\r{}'.format(now_str),end='')
        if now_str in ['07:30:00']:
            itchat.send(str(get_page()), toUserName=userName)
        time.sleep(1)

if __name__ == '__main__':
    itchat.auto_login()
    get_page()
    timeRun()
    itchat.run()
