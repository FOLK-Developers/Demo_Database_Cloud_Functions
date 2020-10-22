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

def hello_world(request):
    recdata = flask.request.json
    fcm_id = recdata['fcm_id']
    event_id = recdata['event_id']
    typ = recdata['notification_type']
    folk_guide = recdata['FOLK_guide']
    user_name = recdata['user_name']
    user_zone = recdata['user_zone']
    user_phone = recdata['user_phone']
    title = recdata['title']
    body = recdata['body']
    gender = ['gender']

    docs = db.collection(u'Events').document(event_id)
    docs = docs.get()
    docs = docs.to_dict()

    zone = docs['zone']
    image = docs['event_img_url']
    program = docs['program']
    program_title = docs['category']
    event_link = docs['venue']
    session = docs['session']
    
    response = None
    result = None
    
    data_message = {
    "feedDocumentId": event_id,
    "type": typ,
    "title": title,
    "image": image,
    "icon": "notificationbar",
    "sound": "text_notification",
    "android_channel_id": "Krishna_Channel",
    "body": body,
    "click_action": "FLUTTER_NOTIFICATION_CLICK",
    "zone": zone,
    "program": program,
    "program_title": program_title,
    "event_link": event_link,
    "session": session
    }
    
    push_service = FCMNotification(
    api_key="AAAANwzJXd8:APA91bGr_iEZG2r4VFv5SEuVIRHM3511N-6TTIgh46Jkp52ko25UIg-pEkrGOR-2gitB5IP0L86RQa6AwDxdHwIqltGffnZeZXx5i836HLiIEyaG7La69mD6gM_sQlpfnNHsctkCle-1",
    proxy_dict=None)

    if fcm_id is not None:
        message_title = "New Notification from FOLK!"
        #message_body = "Hey, EVENT STARTED"
        extra_notification_kwargs = {
        'android_channel_id': 2
        }
        result = push_service.notify_single_device(registration_id=fcm_id, message_title=message_title,
                                                   data_message=data_message, extra_notification_kwargs=extra_notification_kwargs)
        print("result : ", result)
        response = {
            "status" : True,
            "output" : result
        }
    else:
        response = {
            "status" : False,
            "output" : "No fcm_id"
        }
        
            
    return jsonify(response)
