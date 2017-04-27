from rest_framework import serializers
from apps.api.models import User, Gateway, Node, Swarm, RxInfo, TxInfo, Message


class GatewaySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Gateway
        fields = '__all__'


class NodeSerializer(serializers.HyperlinkedModelSerializer):
    last_gateway = serializers.HyperlinkedRelatedField(many=True, view_name='gateways-detail', read_only=True)

    class Meta:
        model = Node
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    gateways = serializers.HyperlinkedRelatedField(many=True, view_name='gateways-detail', read_only=True)
    nodes = serializers.HyperlinkedRelatedField(many=True, view_name='nodes-detail', read_only=True)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.company = validated_data.get('company', instance.company)
        instance.gateways = validated_data.get('gateways', instance.gateways)
        instance.nodes = validated_data.get('nodes', instance.nodes)
        instance.save()
        return instance
      
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
