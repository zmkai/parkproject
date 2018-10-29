import json
import re
from datetime import datetime

from django.http import HttpResponse, QueryDict
from django.shortcuts import render
from django.views.generic import View
from company.models import Company
from django.core import  serializers

from park.models import Park


class CompanyView(View):

    '''
        创建一个公司，添加公司到公司表
    '''
    def post(self,request):
        print('post')
        result = request.POST
        company_name = result.get('company_name')
        company_register = datetime.strptime(result.get('company_register'),'%Y-%m-%d')
        company_address = result.get('company_address')
        company_count = int(result.get('company_count'))
        company = Company()
        company.company_count = company_count
        company.company_name = company_name
        company.company_address = company_address
        company.company_register = company_register
        company.save()
        return HttpResponse('添加成功')
    '''
        通过一个公司id获得一个公司对象，并返回
    '''
    def get(self, request):
        print('get')
        result = request.GET
        company_id = result.get('id')

        company = Company.objects.get(id=company_id)
        # parks = company.park_set.all()
        # # parks = Park.objects.filter(park_company_id = company_id)
        # Company.objects._
        # for park in parks:
        #     print(park.park_name)
        print(company)
        # print(company)
        # json_str = serializers.serialize('json',company)
        # print(json_str)
        # company_dict =  dict(company)
        # mydict = {'name':'admin'}
        json_str = company.company_name +'---------->'+company.company_address
        json_str = serializers.serialize("json", [company])
        # json_str = json.dumps()
        return HttpResponse(json_str)

    def delete(self,request):
        print('delete')
        result = request.GET
        company_id = result.get('id')
        company = Company.objects.get(id=company_id)
        company.delete()
        return HttpResponse('删除成功')

    def put(self , request):
        print('put')
        str1 = request.body.decode()
        str1 = re.sub('\'', '\"', str1)
        # print(str1)
        result = json.loads(str1)
        company_id= result.get('company_id')
        company_name = result.get('company_name')
        company_register = datetime.strptime(result.get('company_register'), '%Y-%m-%d')
        company_address = result.get('company_address')
        company_count = int(result.get('company_count'))
        company = Company.objects.get(id = company_id)
        company.company_count = company_count
        company.company_name = company_name
        company.company_address = company_address
        company.company_register = company_register
        company.save()
        return HttpResponse('修改成功')