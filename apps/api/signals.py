from django.dispatch import Signal
import paho.mqtt.client as mqtt
import os
import json


class MqttClient(object):
    """docstring for MqttClient"""

    def __init__(self):
        super(MqttClient, self).__init__()
        self.signal = Signal(providing_args=["message", "txInfo", "rxInfo", "signalCount"])
        self.client = mqtt.Client(transport="tcp")
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.signal_count = False
        self.client.username_pw_set(username=os.environ.get("MQTT_USERNAME"), password=os.environ.get("MQTT_PASSWORD"))
        self.client.connect(os.environ.get("MQTT_HOST"), int(os.environ.get("MQTT_PORT")),
                            int(os.environ.get("MQTT_KEEPALIVE")))
        self.client.loop_start()

    def getSignal(self):
        return self.signal

    def on_connect(self, client, userdata, flags, rc):
        print("Connected to dejwoo.com")
        client.subscribe('data')

    def on_message(self, client, userdata, message):
        try:
            payload = json.loads(message.payload.decode('utf-8'))
            txInfo = payload['txInfo']
            rxInfo = payload['rxInfo']
            message = dict((key, value) for key, value in payload.items() if key not in ['txInfo', 'rxInfo'])
            self.signal_count = not self.signal_count
            self.signal.send(sender=self.__class__, message=message, txInfo=txInfo, rxInfo=rxInfo,
                             signalCount=self.signal_count)
            client.publish('response', payload="Message recieved Capitain!")
        except (ValueError, KeyError, TypeError) as e:
            print("JSON format error:\n", message, "\t->\t", e, )

    def exit(self):
        self.loop_end()

    def reset(self):
        self.client.loop_stop()

    def __exit__(self, exc_type, exc_value, traceback):
        self.package_obj.cleanup()

    def signalRecieved(self, parity):
        if parity == self.signal_count:
            self.signal_count = not self.signal_count
            return True
        return False
