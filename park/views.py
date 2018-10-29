import json
import re
from datetime import datetime

from django.core import serializers
from django.http import HttpResponse, QueryDict
from django.shortcuts import render
from django.views.generic import View


# Create your views here.
from park.models import Park
from park.models import Park


class ParkView(View):
    '''
        添加一个停车场实例

    '''
    def post(self,request):
        print('post')
        result = request.POST
        park_name = result.get('park_name')
        park_register = datetime.strptime(result.get('park_register'), '%Y-%m-%d')
        park_park_id = result.get('park_id')
        park_count = int(result.get('park_count'))
        park = Park()
        park.park_count = park_count
        park.park_name = park_name
        park.park_park_id = park_park_id
        park.park_register = park_register
        park.save()
        return HttpResponse('添加停车场成功')

    '''
        根据一个停车场id查出停车场
    '''
    def get(self,request):
        print('get')
        result = request.GET
        park_id = result.get('park_id')
        park = Park.objects.get(id = park_id)
        park = park.objects.get(pk = park_id)
        # print(park)
        json_str = serializers.serialize("json", [park,park])
        # json_str = json.dumps()
        return HttpResponse(json_str)

    '''
        根据停车场id删除
    '''
    def delete(self,request):
        print('get')
        result = request.GET
        park_id = result.get('id')
        park = Park.objects.get(id=park_id)
        park.delete()
        return HttpResponse('删除成功')

    '''
        修改停车场信息
    '''
    def put(self,request):
        print('put')
        str1 = request.body.decode()
        str1 = re.sub('\'', '\"', str1)
        # print(str1)
        result = json.loads(str1)
        print(result.get('park_register'))
        park_id = int(result.get('park_id'))
        park_name = result.get('park_name')
        park_register = datetime.strptime(result.get('park_register'), '%Y-%m-%d')
        # park_company_id = result.get('company_id')
        park_count = int(result.get('park_count'))
        park = Park.objects.get(id = park_id)
        park.park_count = park_count
        park.park_name = park_name
        park.park_register = park_register
        park.save()
        return HttpResponse('修改成功')
