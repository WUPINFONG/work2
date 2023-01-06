# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 14:16:41 2022

@author: perry
"""

from flask import Flask,render_template,request,url_for,redirect
import db

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/food',methods=['GET'])
def food():
    items = request.args.get('item')
    keyword = request.args.get('p')
   
    if items == None and keyword == None:
        sql = "select * from food order by id desc"
    elif len(items) > 0 and len(keyword) == 0:  
       
        sql = "select * from food where name like '%{}%'".format(items)
    
    elif len(items) == 0 and len(keyword) > 0:
       
        sql = "select * from food where address like '%{}%'".format(keyword)
        
    else:
         
        sql = "select * from food where name like '%{}%' and  address like '%{}%' ".format(items,keyword)
      
    cursor = db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    res = cursor.fetchall()
    return render_template("food.html",result=res)    


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/addMessage",methods=['POST'])
def addContact():
    if request.method=="POST":
        username=request.form.get('username')
        title=request.form.get('title')
        email=request.form.get('email')
        content=request.form.get('content')
        
        sql="insert into message (title,username,email,content) values('{}','{}','{}','{}')".format(title,username,email,content)
        
        cursor=db.conn.cursor()
        cursor.execute(sql)
        db.conn.commit()
    
    return redirect(url_for('contact'))

@app.route('/foodupdata')
def foodupdata():
    return render_template('foodupdata.html')

@app.route('/diyfood',methods=['GET'])
def diyfood():
    items = request.args.get('item')
    keyword = request.args.get('p')
    page =request.args.get('page')
    
    sql= "select count(*) as allcount from diyfood"
    cursor =db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    res= cursor.fetchone()#抓到全部的資料，一維呈現
    count=int(res[0])
    
   
    if items == None and keyword == None:
        sql = "select * from diyfood order by id desc"
    elif len(items) > 0 and len(keyword) == 0:  
       
        sql = "select * from diyfood where name like '%{}%'".format(items)
    
    elif len(items) == 0 and len(keyword) > 0:
       
        sql = "select * from diyfood where infomation like '%{}%'".format(keyword)
        
    else:
         
        sql = "select * from diyfood where name like '%{}%' and infomation like '%{}%' ".format(items,keyword)
      
    cursor = db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    res = cursor.fetchall()
        
    return render_template('diyfood.html',result=res)




app.run(debug=True)

