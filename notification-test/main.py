import firebase_admin
import flask
import pyfcm
from firebase_admin import credentials, messaging
from firebase_admin import firestore
from flask import jsonify
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

arr1 = None
def hello_world(request):
    recdata = flask.request.json
    fcm_id = recdata['fcm_id']
    arr1 = []
    arr1 = arr1.append(fcm_id)
    
    
    data = {
        "notification": {
            "body": "Notification from postman",
            "title": "You have a new message."
        },
        "priority": "high",
        "data": {
            "click_action": "FLUTTER_NOTIFICATION_CLICK",
            "id": "1",
            "status": "done"
        },
        # "to": "/topics/all",
        "registration_ids":arr1
    }

    headers = {
        'Content-type': 'application/json',
        'Authorization': 'key=AAAANwzJXd8:APA91bGr_iEZG2r4VFv5SEuVIRHM3511N-6TTIgh46Jkp52ko25UIg-pEkrGOR-2gitB5IP0L86RQa6AwDxdHwIqltGffnZeZXx5i836HLiIEyaG7La69mD6gM_sQlpfnNHsctkCle-1'
        #'Authorization': 'fAV9wSaLTiCem7XuIi7TJ7:APA91bE7iFgAdhZUqv_aTX_nq7v61ErDezERL4giwMg03Js000DuJAXvYpK3e_X3rAdgz5R5mYAP4abNoM7zLIpXns21NdMC3x_OLpgAMRgpWhuS2QlpjcWVjDUTwRq2qAGEMZzi-n7J'
    }
    
    result = requests.post('https://fcm.googleapis.com/fcm/send', data=json.dumps(data), headers=headers)
    print(result.text)
    response = {
        "status" : True,
        "output" : result.text
    }
    return jsonify(response)
