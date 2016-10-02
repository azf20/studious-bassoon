from slackclient import SlackClient
import requests
import json

token = "xoxp-86428459589-86428459653-86424392214-3cccbe148dfa807dc9d6704ce94b8e73"      # found at https://api.slack.com/web#authentication
sc = SlackClient(token)
print(sc.api_call("api.test"))
#print(sc.api_call("channels.info", channel="general"))
'''sc.api_call(
        "chat.postMessage", channel="#api_testing", text="Hello from Python! :tada:",
        username='pybot', icon_emoji=':robot_face:',
        attachments = '[{"title": "Try these - ",\
                        "text": " Text ",\
                        "image_url": "http://pix.iemoji.com/images/emoji/apple/ios-9/256/white-waving-hand-sign.png"}]'
)'''

f = open('mario.png', 'rb')

print(sc.api_call(
"files.upload", file=f, title = 'swagger', channels = "#api_testing", initial_comment = 'This is a picture of Mario'
)
)
