# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 15:39:14 2022

@author: perry
"""


import db


# 載入函式庫
import cfscrape, bs4
from datetime import datetime as dt

today=dt.today()
todayS=today.strftime('%Y-%m-%d')



# 使用網頁右上角 > 更多工具 > 開發人員工具 觀察網頁結果
# ------------------------ iCook 搜尋結果 ------------------------ #
# <h2 class="browse-recipe-name">食譜標題</h2>

# 獲取指定網頁
scraper = cfscrape.create_scraper()
result = scraper.get("https://decathlon.tw/category-weighttraining?p=2")

# 進行網頁分析
soup = bs4.BeautifulSoup(result.text, "html.parser")
goods = soup.find_all("li", attrs={"class": "item product product-item infinite"})
print(goods)

cursor =db.conn.cursor()


for row in goods:
    
    title=row.find('span',class_="product name product-item-name").text
    title=title.lstrip()
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
  
    # sql= "insert into diyfood (name,link,infomation)values('{}','{}','{}')" .format(title,link1,infomation)
     