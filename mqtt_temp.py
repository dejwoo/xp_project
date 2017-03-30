from pprint import pprint
from time import sleep

import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print("Connected to dejwoo.com")
    client.subscribe('test/hello/1')
    client.subscribe('test/hello/2')
    client.subscribe('test/hello/3')
    client.subscribe('test/hello/4')


def messages_received(client, userdata, message):
    l = json.loads(message.payload)
    pprint(l)
    client.publish('test/hello/back', payload="Message recieved Capitain!")


client = mqtt.Client(transport="tcp")
client.on_connect = on_connect
client.username_pw_set(username="project_noe", password="arOMEtrOpOlongmArtHmarYdRAnTOp")
client.message_callback_add('test/hello/+', messages_received)
client.connect("dejwoo.com", 13881, 60)
client.loop_forever()
