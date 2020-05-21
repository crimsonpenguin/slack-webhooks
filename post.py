#!/bin/python3
import requests
import json

msg = 'test message'

slack_msg = json.dumps({'text':msg, 'icon_emoji':":smile:",'channel':'#general'})
web_hook_url = 'https://hooks.slack.com/services/WEBHOOK'
headers={'Content-Type': 'application/json; charset=UTF-8'}
response = requests.post(web_hook_url, slack_msg, headers)
