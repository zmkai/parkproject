from django.conf.urls import url

from company.company_views import CompanyView
from company.views import CompaniesView

urlpatterns = [
    url(r'^companies/$', CompaniesView.as_view()),
    url(r'^company/$',CompanyView.as_view())
]