# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 20:58:16 2022

@author: perry
"""

import requests
from bs4 import BeautifulSoup
import db
from datetime import datetime as dt

today=dt.today()
todayS=today.strftime('%Y-%m-%d')

url="https://decathlon.tw/category-acc-hikingbag"

# payload={'p':'女鞋'}

data=requests.get(url).text
soup=BeautifulSoup(data,'html.parser')

goods=soup.find_all('li',class_='item product product-item infinite')

# allgoods=goods.find_all('div',class_='product photo product-item-photo')

print(goods)
cursor =db.conn.cursor()

for row in goods:
    
    title=row.find('span',class_="product name product-item-name").text
    link=row.find('a',class_='product-item-link d-block').get('href')
    photo=row.find('img',class_="product-image-photo").get('src')
    price = row.find('span',class_='price').text
    price = price.replace('$','').replace(',','')
     
    print(title)
    print(link)
    print(photo)
    print(price)
    print()
   

    sql="insert into product(name,price,photo_url,  product_url,create_data,discount) values('{}','{}','{}','{}','{}','1')".format(title,price,photo,link,todayS)
        
        
    cursor.execute(sql)
    db.conn.commit()
    db.conn.close()  