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
result = scraper.get("https://www.booking.com/searchresults.zh-tw.html?label=gog235jc-1FCAMYiAQo5wFCCXRhaS1jaHVuZ0gwWANo5wGIAQGYATC4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AuqStZ0GwAIB0gIkMWI0MDI1NjQtODI0OS00YjU1LTk1NzQtMjViMmNhNDFkZDQ32AIF4AIB&sid=709ac0f9fa20f9490b0cebfd7c9a89f7&aid=356980&ss=%E5%8D%97%E6%8A%95&ssne=%E5%9F%BA%E9%9A%86&ssne_untouched=%E5%9F%BA%E9%9A%86&efdco=1&lang=zh-tw&src=searchresults&dest_id=5231&dest_type=region&ac_position=0&ac_click_type=b&ac_langcode=zh&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=3fea40a1c3ce01fe&ac_meta=GhAzZmVhNDBhMWMzY2UwMWZlIAAoATICemg6BuWNl%2BaKlUAASgBQAA%3D%3D&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&nflt=ht_id%3D203")

# 進行網頁分析
soup = bs4.BeautifulSoup(result.text, "html.parser")
goods = soup.find_all("div", attrs={"class": "a826ba81c4 fe821aea6c fa2f36ad22 afd256fc79 d08f526e0d ed11e24d01 ef9845d4b3 da89aeb942"})
# print(goods)

cursor =db.conn.cursor()


for row in goods:
    
    title=row.find('div',class_="fcab3ed991 a23c043802").text
    # title=title.lstrip()
    link=row.find('a').get('href')
    photo=row.find('img').get('src')
    info=row.find('div',class_='d8eab2cf7f').text
    # price = row.find('span',class_='price').text
    # price = price.replace('$','').replace(',','')
     
    print(title)
    print(link)
    print(photo)
    print(info)
    print()
   

    sql="insert into hotle(title,link,photo,content,create_date,number) values('{}','{}','{}','{}','{}','17')".format(title,link,photo,info,todayS)
   
   
    cursor.execute(sql)
    db.conn.commit()
  
    # sql= "insert into diyfood (name,link,infomation)values('{}','{}','{}')" .format(title,link1,infomation)
     