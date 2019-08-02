# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from datetime import date
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello_world():
    return ':)'

@app.route('/requestfollowdata', methods=['GET'])
def send_data():
    ds = request.args.get('ds', '')
    if ds == '':
        ds = date.today()

    cnx = mysql.connector.connect(user='csfb', password='beepboop',
                          host='csfb.mysql.pythonanywhere-services.com',
                          database='csfb$scrapes')

    cursor = cnx.cursor()

    cursor.execute("select * from followers_7d")

    out = cursor.fetchall()

    header = [(
        'row', 
        'name', 
        'watch_hours', 
        'broadcast_hours', 
        'peak_viewers', 
        'avg_viewers', 
        'followers', 
        'new_followers', 
        'partnered', 
        'mature', 
        'language',
        'ds')]

    
    return '\n'.join(['\t'.join([str(x) for x in row]) for row in (header+out)])
