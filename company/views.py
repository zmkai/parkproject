from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from company.models import Company


class CompaniesView(View):
    '''
        获得所有的公司
    '''
    def get(self,request):
        companies =  Company.objects.all()
        json_str = ''
        for company in companies :
            json_str += company.company_name+"----"+company.company_address+"----------"\
            +str(company.company_register)+'------------'+str(company.company_count)+'\n'
        print(json_str)

        return HttpResponse(json_str)

    def post(self,request):
        print('post')
        result = request.POST
        print(result.__dir__)
        return HttpResponse('successful')