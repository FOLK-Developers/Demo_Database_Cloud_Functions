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
    event_id = recdata['event_id']
    response = None
    
    data_message = {
    "feedDocumentId": event_id,
    "type": "typ",
    "title": "title",
    "image": "image",
    "icon": "notificationbar",
    "sound": "text_notification",
    "android_channel_id": "Krishna_Channel",
    "body": "body",
    "click_action": "FOLKActivity",
    "zone": "folkevent['zone']",
    "program": "folkevent['program']",
    "program_title": "folkevent['category']",
    "event_link": "folkevent['venue']",
    "session": "folkevent['session']"
    }
    push_service = FCMNotification(
    api_key="AAAANwzJXd8:APA91bGr_iEZG2r4VFv5SEuVIRHM3511N-6TTIgh46Jkp52ko25UIg-pEkrGOR-2gitB5IP0L86RQa6AwDxdHwIqltGffnZeZXx5i836HLiIEyaG7La69mD6gM_sQlpfnNHsctkCle-1",
    proxy_dict=None)

    if fcm_id is not None:
        message_title = "Folk NOTFICATION 2"
        message_body = "Hey, EVENT STARTED"
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
