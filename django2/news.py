# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 14:52:18 2022

@author: perry
"""

import requests#上網用
from bs4 import BeautifulSoup#爬蟲專用
import db
from datetime import datetime as dt

today=dt.today()
todayS=today.strftime('%Y-%m-%d')
url="https://www.taiwan.net.tw/m1.aspx?sNo=0001001&page=3"
data=requests.get(url)
data.encoding="utf8" #將資料編碼為:UTF8
data=data.text
soup= BeautifulSoup(data,'html.parser')
news=soup.find_all('div',class_='columnBlock')
cursor =db.conn.cursor()

for row in news:
    title=row.find('h3').text
    link=row.find('a').get('href')
    # photo=row.find('img',class_=" lazyloaded").get('src')
    link1='https://www.taiwan.net.tw/'+link
   
    
    sql= "insert into news (title,link,create_date)values('{}','{}','{}')" .format(title,link1,todayS)
    cursor.execute(sql)
    db.conn.commit()