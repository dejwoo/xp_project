from rest_framework import serializers
from django.contrib.auth.models import Permission
from apps.api.models import User, Gateway, Node, Swarm, RxInfo, TxInfo, Message
from  datetime import datetime

class GatewaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gateway
        fields = '__all__'


class NodeSerializer(serializers.HyperlinkedModelSerializer):
    last_gateway = serializers.HyperlinkedRelatedField(many=True, view_name='gateways-detail', read_only=True)
    user = serializers.SerializerMethodField()
    def get_user(self, obj):
        return self.context['request'].user.id
    class Meta:
        model = Node
        fields = ('app_eui','app_key','dev_addr','dev_eui','last_gateway','last_seen','name','type', 'user')
    def update(self, instance, validated_data):
        instance.app_eui = validated_data.get('app_eui', instance.app_eui)
        instance.app_key = validated_data.get('app_key', instance.app_key)
        instance.dev_addr = validated_data.get('dev_addr', instance.dev_addr)
        instance.dev_eui = validated_data.get('dev_eui', instance.dev_eui)
        instance.type = validated_data.get('type', instance.type)
        instance.name = validated_data.get('name', instance.name)
        instance.last_gateway = None
        instance.last_seen = datetime.now()
        instance.user = User.objects.get(id=self.context['request'].user.id)
        instance.save()
        return instance

    def create(self, validated_data):
        print("CREATE NODE", validated_data)
        print("CREATE NODE CONTEXT", self.context)
        validated_data['user'] = User.objects.get(id=self.context['request'].user.id)
        return Node.objects.create(**validated_data)


class UserSerializer(serializers.HyperlinkedModelSerializer):

    def update(self, instance, validated_data):
        instance.company = validated_data.get('company', instance.company)
        instance.save()
        return instance

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
        fields = (
        'url', 'last_login', 'username', 'first_name', 'last_name', 'email', 'last_login',
        'date_joined', 'company', 'groups')


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
