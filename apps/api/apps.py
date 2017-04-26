from django.apps import AppConfig
from django.dispatch import receiver
from apps.api.signals import MqttClient
from django.dispatch import Signal

# dispatch_uid="dd5e8bfe-ea9b-42a3-a595-4810d0987650"

class ApiConfig(AppConfig):
    name = 'apps.api'
    verbose_name = 'Project Noe API app'

    def ready(self):
        self.mqtt = MqttClient()
        self.Message = self.get_model('Message')
        self.TxInfo = self.get_model('TxInfo')
        self.RxInfo = self.get_model('RxInfo')
        Signal.connect(self.mqtt.getSignal(),receiver=self.on_message_recieved, weak=False, dispatch_uid="dd5e8bfe-ea9b-42a3-a595-4810d0987650")
        return

    def on_message_recieved(self, sender, message, txInfo, rxInfo, **kwargs):
        dataRate = txInfo.pop('dataRate', None)
        newTxInfo = self.TxInfo(*txInfo)
        newRxInfo = self.RxInfo(*rxInfo)
        newMessage = self.Message(
            applicationName = message['applicationName'],
            applicationID = message['applicationID'],
            devEUI = message['devEUI'],
            nodeName = message['nodeName'],
            data = message['data'],
            fCnt = message['fCnt'],
            fPort = message['fPort'],
            gateway = message['gateway'],
            node = message['node'],
            timestamp = message['timestamp'],
            rxInfo = message['rxInfo'],
            txInfo = message['txInfo'])
        print("Message", newMessage)
        # print("Message data", message['data'])
        # print("txInfo", newTxInfo)
        # print("rxInfo", newRxInfo)
