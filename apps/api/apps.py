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
        newRxInfo = self.RxInfo(loRaSNR= rxInfo['loRaSNR'],
                                latitude= rxInfo['latitude'],
                                altitude= rxInfo['altitude'],
                                longitude= rxInfo['longitude'],
                                gatwayMac= rxInfo['mac'],
                                gatwayName= rxInfo['name'],
                                time=rxInfo['time'],
                                rssi=rxInfo['rssi'])
        newTxInfo = self.TxInfo(adr=txInfo['adr'],
                                codeRate=txInfo['codeRate'],
                                bandwidth=txInfo['dataRate']['bandwidth'],
                                modulation=txInfo['dataRate']['modulation'],
                                spreadFactor=txInfo['dataRate']['spreadFactor'],
                                frequency=txInfo['frequency'])
        newMessage = self.Message(applicationName = message['applicationName'],
                                  applicationID = message['applicationID'],
                                  nodeName = message['nodeName'],
                                  devEUI = message['devEUI'],
                                  data = message['data'],
                                  fCnt = message['fCnt'],
                                  fPort = message['fPort'])
        newTxInfo.save()
        newRxInfo.save()
        newMessage.txInfo = newTxInfo
        newMessage.rxInfo = newRxInfo
        newMessage.save()
        print("Message", newMessage)
        print("TxInfo", newTxInfo)
        print("RxInfo", newRxInfo)
