from rest_framework import serializers

from .models import HackApi


class ApiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HackApi
  #      summ = HackApi.var_a + HackApi.var_b
        fields = ('name','var_a','var_b','addd')
       # c = fields[1]+fields[2]
       # print (c)
