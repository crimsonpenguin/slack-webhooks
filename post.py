#pyhton 2.7 no addons or addtinal modules installed

#!/usr/bin/python
import urllib
import httplib

msg = 'test'

slack_msg = json.dumps({'text':msg, 'icon_emoji':':smile:','username':'Test','channel':'#test'})
link = httplib.HTTPSConnection('hooks.slack.com')
#add full link for slack web hook
web_hook_url = '/services/'
headers={'Content-Type': 'application/json'}
link.request("POST", web_hook_url, slack_msg, headers)
resp = link.getresponse()
ack = resp.read()
