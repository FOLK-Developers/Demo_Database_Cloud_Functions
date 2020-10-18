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
        "registration_ids": [
            'eaSIuUXzRjC3YwIJDnpHbX:APA91bGD56SST2KsD9DByj1e6clD9dt65dkIFLeCB9CVKYNbr3n5xk0dlLk__zzXs_q-Hhh9bDDnkaQ4ljVhxEQozSMPhpc7x6_0N_LCkDeJhTt0YnrHzv-BwGe_9o4o7st-HwHstEhA']
    }

    headers = {
        'Content-type': 'application/json',
        'Authorization': 'key=AAAANwzJXd8:APA91bGr_iEZG2r4VFv5SEuVIRHM3511N-6TTIgh46Jkp52ko25UIg-pEkrGOR-2gitB5IP0L86RQa6AwDxdHwIqltGffnZeZXx5i836HLiIEyaG7La69mD6gM_sQlpfnNHsctkCle-1'
    }
    
    result = requests.post('https://fcm.googleapis.com/fcm/send', data=json.dumps(data), headers=headers)
    print(result.text)
    response = {
        "status" : True,
        "output" : result.text
    }
    return jsonify(response)
