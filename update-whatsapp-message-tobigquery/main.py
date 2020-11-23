import datetime as datetime
import bigquery
import firebase_admin
import flask
import google.cloud
from dateutil.tz import tzutc
from firebase_admin import credentials, messaging
from firebase_admin import firestore
import urllib.request
import json
import requests
import messagebird
from messagebird.conversation_message import MESSAGE_TYPE_TEXT
from flask import request, jsonify
import datetime
from datetime import date
from datetime import datetime
import pytz
from pytz import timezone
import time as t1
from google.cloud import bigquery
# time t1
from time import time
from google.oauth2 import service_account
import firebase_admin
from firebase_admin import credentials
from google.cloud import bigquery
import json
from firebase_admin import credentials

# BIGQUERY
# TODO(developer): Set key_path to the path to the service account key
#                  file.
key_path = "folk-database-firebase-adminsdk-ulj3e-890294e600.json"

credentials = service_account.Credentials.from_service_account_file(
    key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

# # Construct a BigQuery client object.
client = bigquery.Client()

print("Send Individual Whatsapp Message Logic initiated.")


recdata = {
    "to": ["919481192803"],
    "templateName": "update_on_upcoming_session",
    "default1": "Hare Krishna! Welcome to Braj Mandal Parikrama 2020",
    "default2": "tonights visit to Mathura & Gokul (Day 1)",
    "default3": "https://youtu.be/jgFS5RD-Wfw",
    "default4": "on YouTube, For English visit the above link"
}

doc_id = recdata["to"]
templateName = recdata["templateName"]
default1 = recdata["default1"]
default2 = recdata["default2"]
default3 = recdata["default3"]
default4 = recdata["default4"]
client = messagebird.Client('uCZWekG3IoT7RPBeEjMp65Eg1')


sent_timestamp = int(time())
msg = client.conversation_start({
    'channelId': 'a4341dd8dfe34df6aad904e9d765653d',
    'to': doc_id[0],
    'type': "hsm",
    'content': {
        'hsm': {
            'namespace': '0468f3bd_4f10_4bad_bbed_0f70096b0626',
            'templateName': templateName,
            'language': {
                'policy': 'deterministic',
                'code': 'en'
            },
            'params': [
                {"default": default1},
                {"default": default2},
                {"default": default3},
                {"default": default4}
            ]
        }
    }
})

if msg is not None:
    sent_timestamp = int(time())

msgData = msg.__dict__
contactInfo = msgData['_contact'].__dict__
messagesInfo = msgData['_messages'].__dict__
channelsInfo = msgData['_channels'][0].__dict__
print("msg: ", msg)
created_datetime = msgData['_createdDatetime']
updated_datetime = msgData['_createdDatetime']
last_received_datetime = msgData['_lastReceivedDatetime']
completeMessage = default1 + default2 + default3 + default4

dic = {
    "id": msgData['id'],
    "mobile": doc_id[0],
    "sent_timestamp": sent_timestamp,
    "message_total_count": messagesInfo['totalCount'],
    "last_received_date": last_received_datetime,
    "status": msgData['status'],
    "createdDatetime": created_datetime,
    "updatedDatetime": updated_datetime,
    "channelId": channelsInfo['id'],
    "contact_id": contactInfo['id'],
    "type": "hsm",
    "last_used_channel_id": "a4341dd8dfe34df6aad904e9d765653d",
    "content_hsm_namespace": "0468f3bd_4f10_4bad_bbed_0f70096b0626",
    "content_hsm_templateName": templateName,
    "content_hsm_params_message": completeMessage,
    "content_hsm_language_policy": "deterministic",
    "content_hsm_language_code": "en"
}

print("dic:",dic)


# bigquerycode
query = f"""
        INSERT `folk-database.FOLKReports.WhatsAppMessageReports` (id,mobile,sent_timestamp,message_total_count,last_received_date,status,createdDatetime,updatedDatetime,channelId,contact_id,type,last_used_channel_id,content_hsm_namespace,content_hsm_templateName,content_hsm_params_message,content_hsm_language_policy,content_hsm_language_code)
        VALUES (@id,@mobile,@sent_timestamp,@message_total_count,@last_received_date,@status,@createdDatetime,@updatedDatetime,@channelId,@contact_id,@type,@last_used_channel_id,@content_hsm_namespace,@content_hsm_templateName,@content_hsm_params_message,@content_hsm_language_policy,@content_hsm_language_code)
    """
job_config = bigquery.QueryJobConfig(
    query_parameters=[
        bigquery.ScalarQueryParameter("id", "STRING", dic['id']),
        bigquery.ScalarQueryParameter("mobile", "STRING", dic['mobile']),
        bigquery.ScalarQueryParameter("sent_timestamp", "STRING", dic['sent_timestamp']),
        bigquery.ScalarQueryParameter("message_total_count", "STRING", dic['message_total_count']),
        bigquery.ScalarQueryParameter("last_received_date", "STRING", dic['last_received_date']),
        bigquery.ScalarQueryParameter("status", "STRING", dic['status']),
        bigquery.ScalarQueryParameter("createdDatetime", "STRING", dic['createdDatetime']),
        bigquery.ScalarQueryParameter("updatedDatetime", "STRING", dic['updatedDatetime']),
        bigquery.ScalarQueryParameter("channelId", "STRING", dic['channelId']),
        bigquery.ScalarQueryParameter("contact_id", "STRING", dic['contact_id']),
        bigquery.ScalarQueryParameter("type", "STRING", dic['type']),
        bigquery.ScalarQueryParameter("last_used_channel_id", "STRING", dic['last_used_channel_id']),
        bigquery.ScalarQueryParameter("content_hsm_namespace", "STRING", dic['content_hsm_namespace']),
        bigquery.ScalarQueryParameter("content_hsm_templateName", "STRING", dic['content_hsm_templateName']),
        bigquery.ScalarQueryParameter("content_hsm_params_message", "STRING", dic['content_hsm_params_message']),
        bigquery.ScalarQueryParameter("content_hsm_language_policy", "STRING", dic['content_hsm_language_policy']),
        bigquery.ScalarQueryParameter("content_hsm_language_code", "STRING", dic['content_hsm_language_code']),

    ]
)
query_job = client.query(query, job_config=job_config)  # Make an API request.

print(query_job.__dict__)
print("Finished")
