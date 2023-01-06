# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 15:39:14 2022

@author: perry
"""


import db


# 載入函式庫
import cfscrape, bs4




# 使用網頁右上角 > 更多工具 > 開發人員工具 觀察網頁結果
# ------------------------ iCook 搜尋結果 ------------------------ #
# <h2 class="browse-recipe-name">食譜標題</h2>

# 獲取指定網頁
scraper = cfscrape.create_scraper()
result = scraper.get("https://icook.tw/search/%E6%B2%B9%E7%82%B8/")

# 進行網頁分析
soup = bs4.BeautifulSoup(result.text, "html.parser")
titles = soup.find_all("li", attrs={"class": "browse-recipe-item"})

cursor =db.conn.cursor()

for row in titles:
    
    title=row.find('h2',class_="browse-recipe-name").text
    link=row.find('a',class_="browse-recipe-link").get('href')
    infomation=row.find('p',class_="browse-recipe-content-ingredient").text
    
      
    link1='https://icook.tw'+link
    print(link1)
    print(title)
    print(infomation)
   
    sql= "insert into diyfood (name,link,infomation)values('{}','{}','{}')" .format(title,link1,infomation)
    cursor.execute(sql)
    db.conn.commit()
  
    
     