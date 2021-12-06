from rest_framework import viewsets
from rest_framework.decorators import action
from .serializers import ApiSerializer
from .models import HackApi
from django.http import HttpResponse

class ApiViewSet(viewsets.ModelViewSet):
    queryset = HackApi.objects.all().order_by('name')
    serializer_class = ApiSerializer
    

    # @action(methods=['get'],detail=True)
    # def add_summ(self,request,pk=None):
    #     num = HackApi.objects.get(pk=pk)
    #     summ= HackApi.var_a+HackApi.var_b
    #     return HttpResponse(content=summ,status=200)
