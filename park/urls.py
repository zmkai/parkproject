from django.conf.urls import url,include

from park.views import ParkView

urlpatterns = [
    url(r'^park/$', ParkView.as_view()),
]