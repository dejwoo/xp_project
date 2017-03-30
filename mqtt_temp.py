from time import sleep

import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print(client.subscribe('/test/akos'))


def messages_received(client, userdata, message):
    print(message.payload)


while True:
    client = mqtt.Client(transport="tls")
    client.loop_start()
    client.message_callback_add('/test/hello', messages_received)
    client.on_connect = on_connect
    client.username_pw_set(username="project_noe", password="---")
    client.connect("url", 13888, 60)
    sleep(3)
    client.disconnect()
    client.loop_stop()
    sleep(10)
