from rest_framework import serializers
from apps.api.models import User, Gateway, Node, Swarm, RxInfo, TxInfo, Message


class GatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        fields = ('id','gps_lat', 'gps_lon', 'last_seen', 'mac', 'serial')


class NodeSerializer(serializers.ModelSerializer):
    last_gateway = serializers.PrimaryKeyRelatedField(many=True, queryset=Gateway.objects.all())

    class Meta:
        model = Node
        fields = ('app_eui', 'app_key', 'dev_addr', 'dev_eui', 'last_gateway', 'last_seen', 'name', 'type')

class UserSerializer(serializers.ModelSerializer):
    gateways = serializers.PrimaryKeyRelatedField(many=True, queryset=Gateway.objects.all())
    nodes = serializers.PrimaryKeyRelatedField(many=True, queryset=Node.objects.all())

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.company = validated_data.get('company', instance.company)
        instance.gateways = validated_data.get('gateways', instance.gateways)
        instance.nodes = validated_data.get('nodes', instance.nodes)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = '__all__'
        gateways = GatewaySerializer(required=False)
        nodes = NodeSerializer(required=False)



class SwarmSerializer(serializers.ModelSerializer):
    nodes = serializers.PrimaryKeyRelatedField(many=True, queryset=Node.objects.all())

    class Meta:
        model = Swarm


class MessageSerializer(serializers.ModelSerializer):
    node = serializers.PrimaryKeyRelatedField(many=True, queryset=Node.objects.all())
    rxInfo = serializers.PrimaryKeyRelatedField(many=True, queryset=RxInfo.objects.all())
    txInfo = serializers.PrimaryKeyRelatedField(many=True, queryset=TxInfo.objects.all())

    class Meta:
        model = Message


class RxInfoSerializer(serializers.ModelSerializer):
    gateway = serializers.PrimaryKeyRelatedField(many=True, queryset=Gateway.objects.all())

    class Meta:
        model = RxInfo


class TxInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TxInfo
