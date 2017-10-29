#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from flask import Flask,render_template
import os
import json

app=Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    path = '/home/shiyanlou/files'
    files = os.listdir(path)
    for file in files:
        if not os.path.isdir(file):
            #iter_r = iter(open(path+"/"+file))
            #for line in iter_r:
            with open(path+"/"+file) as f:
                title_data =json.load(f)
        return render_template('index.html', title_data=title_data)
