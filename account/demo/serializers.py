from django.contrib.auth.models import User, Group
from rest_framework import serializers
from demo.models import tableData


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class tableDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = tableData
        fields = ['url', 'thName', 'tableName', 'TD_data']
