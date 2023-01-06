# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 20:55:02 2022

@author: perry
"""
import pymysql
dbsetting ={
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'password':'123456789',
    'db':'test1',
    'charset':'utf8'
    
    
    
    }

conn=pymysql.connect(**dbsetting) 
