  
import firebase_admin
import flask
import pyfcm
from firebase_admin import credentials, messaging
from firebase_admin import firestore
from datetime import date
from datetime import datetime
from flask import request, jsonify
from pyfcm import FCMNotification

import urllib.request
import json
import time
import requests
import ast

firebase_admin.initialize_app()
db = firestore.client()

def hello_world(request):
    recdata = flask.request.json
    
    uname = recdata['uname']
    pwd = recdata['pwd']
    
    #create account
    lFlag = 1
    doc_ref = db.collection(u'LoginInfo').where("username","==",uname).limit(1).stream()

    userData = []
    status = "True"
    for doc in doc_ref:
        lFlag = 0
        docData = doc.to_dict()
        if docData['password'] == pwd:
            userData.append(docData)
    if lFlag:
        status ="False"
    
    
    response = {
                "status": status,
                "username" : userData[0]['username']
                }
    return jsonify(response)


