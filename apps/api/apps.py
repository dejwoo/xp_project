from django.apps import AppConfig
from apps.api.signals import MqttClient
from django.dispatch import Signal
import random
from django.utils import timezone
# dispatch_uid="dd5e8bfe-ea9b-42a3-a595-4810d0987650"

class ApiConfig(AppConfig):
    name = 'apps.api'
    verbose_name = 'Project Noe API app'

    def ready(self):
        self.mqtt = MqttClient()
        self.Message = self.get_model('Message')
        self.TxInfo = self.get_model('TxInfo')
        self.RxInfo = self.get_model('RxInfo')
        self.Node = self.get_model('Node')
        self.Gateway = self.get_model('Gateway')
        self.User = self.get_model('User')
        Signal.connect(self.mqtt.getSignal(),receiver=self.on_message_recieved, weak=False, dispatch_uid="dd5e8bfe-ea9b-42a3-a595-4810d0987650")
        self.init_nodes()
        self.init_gateways()

    def init_nodes(self):
        self.node_types = ['temperature-sensor', 'wind-sensor', 'humidity-sensor']
        for uuid in ['230369c8-813b-4cf9-9fc2-59c9ec4246bf','904d546c-3506-484c-8836-d67a737e72f9','dd973483-2367-4ae5-96ff-663a94020342','60330a45-24b9-4be4-94df-7e8df2bf9dd0','d828a4a9-f1cb-4283-b16b-f35acc3bef55','52cf0c28-dd70-4f16-ace3-e447174d7e13','8700ef72-efb6-4494-b9d7-cfb1abfede8c','fa9c6e93-083e-4ab2-bf13-1e1235a3d562','b9946be6-7046-414d-9f75-1c7db7431669','c63e2b8c-3ba9-4cc8-8b2e-044e4f80a11e']:
            if not self.Node.objects.filter(dev_eui=uuid).exists():
                self.Node(
                    app_eui = 'aabbf8ac-4bab-11e7-a919-92ebcb67fe33',
                    app_key = 'tIveREleCToNSouStONEreyMAYaRTyRfIDacEnDisMERaTERic',
                    dev_addr = random.randint(1000000000000000, 9999999999999999),
                    dev_eui = uuid,
                    last_gateway = None,
                    last_seen = timezone.now(),
                    name = "Device" + uuid[0:5],
                    type = random.choice(self.node_types) ,
                    user = random.choice(self.User.objects.all())
                ).save()
    def init_gateways(self):
        for uuid in ['bf7bd09c-fe10-429b-b563-f841b683d235','f0836050-415f-43df-9ec5-3bde9718ab16','5e5b06c4-a3fb-44e2-b2e8-c577637cb632']:
            if not self.Gateway.objects.filter(mac=uuid).exists():
                self.Gateway(
                gps_lat = random.random()*190 - 90,
                gps_lon = random.random()*360 - 180,
                last_seen = timezone.now(),
                mac = uuid,
                user = random.choice(self.User.objects.all()),
                serial = uuid[1:10] + "-" + uuid[-10:-1]).save()
        Signal.connect(self.mqtt.getSignal(), receiver=self.on_message_recieved, weak=False,
                       dispatch_uid="dd5e8bfe-ea9b-42a3-a595-4810d0987650")

    def on_message_recieved(self, sender, message, txInfo, rxInfo, **kwargs):
        if not self.Gateway.objects.filter(mac=rxInfo['mac']).exists():
            print("apps.api.mqtt_client::on_message_recieved: Gateway UUID does not exists!")
            return
        else:
            current_gateway = self.Gateway.objects.get(mac=rxInfo['mac'])
            current_gateway.last_seen = timezone.now()
            current_gateway.save()
        if not self.Node.objects.filter(dev_eui=message['devEUI']).exists():
            print("apps.api.mqtt_client::on_message_recieved: Node UUID does not exists!")
            return
        else:
            current_node = self.Node.objects.get(dev_eui=message['devEUI'])
            current_node.last_seen = timezone.now()
            current_node.last_gateway = current_gateway
            current_node.save()
        newRxInfo = self.RxInfo(loRaSNR=rxInfo['loRaSNR'], latitude=rxInfo['latitude'], altitude=rxInfo['altitude'],
                                longitude=rxInfo['longitude'], gatewayMac=rxInfo['mac'], gatewayName=rxInfo['name'],
                                time=rxInfo['time'], rssi=rxInfo['rssi'])
        newTxInfo = self.TxInfo(adr=txInfo['adr'], codeRate=txInfo['codeRate'],
                                bandwidth=txInfo['dataRate']['bandwidth'],
                                modulation=txInfo['dataRate']['modulation'],
                                spreadFactor=txInfo['dataRate']['spreadFactor'],
                                frequency=txInfo['frequency'])
        newTxInfo.save()
        newRxInfo.save()
        newMessage = self.Message(**message)
        newMessage.txInfo = newTxInfo
        newMessage.rxInfo = newRxInfo
        newMessage.save()
