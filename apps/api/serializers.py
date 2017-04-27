from rest_framework import serializers
from apps.api.models import User, Gateway, Node, Swarm, RxInfo, TxInfo, Message


class GatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        fields = '__all__'


class NodeSerializer(serializers.ModelSerializer):
    last_gateway = serializers.PrimaryKeyRelatedField(many=True, queryset=Gateway.objects.all())

    class Meta:
        model = Node
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        gateways = GatewaySerializer(required=False, many=True)
        nodes = NodeSerializer(required=False, many=True)



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
