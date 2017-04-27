from rest_framework import serializers
from django.contrib.auth.models import Permission
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

    def create(self, validated_data):
        if not validated_data['groups']:
            validated_data.pop('groups')
        if not validated_data['user_permissions']:
            validated_data.pop('user_permissions')
        # user = User.objects.create(is_active = validated_data['is_active'],
        #             is_superuser = validated_data['is_superuser'],
        #             password = validated_data['password'],
        #             last_name = validated_data['last_name'],
        #             email = validated_data['email'],
        #             is_staff = validated_data['is_staff'],
        #             last_login = validated_data['last_login'],
        #             first_name = validated_data['first_name'],
        #             username = validated_data['username'],
        #             company = validated_data['company'],
        #             gateways = validated_data['gateways'],
        #             nodes = validated_data['nodes'])
        return User.objects.create(**validated_data)

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
