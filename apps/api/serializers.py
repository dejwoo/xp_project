from rest_framework import serializers

from apps.api.models import Profile, Gateway, Node, Swarm, RxInfo, TxInfo, Message


class ProfileSerializer(serializers.ModelSerializer):
    gateways = serializers.PrimaryKeyRelatedField(many=True, queryset=Gateway.objects.all())
    nodes = serializers.PrimaryKeyRelatedField(many=True, queryset=Node.objects.all())

    class Meta:
        model = Profile
        fields = ('user', 'company', 'gateways', 'nodes')


class GatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        fields = ('gps_lat', 'gps_lon', 'last_seen', 'mac', 'serial')


class NodeSerializer(serializers.ModelSerializer):
    last_gateway = serializers.PrimaryKeyRelatedField(many=True, queryset=Gateway.objects.all())

    class Meta:
        model = Node
        fields = ('app_eui', 'app_key', 'dev_addr', 'dev_eui', 'last_gateway', 'last_seen', 'name', 'type')


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
