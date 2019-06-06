from django.conf.urls import url
from backend.views import *

app_name = 'backend'
urlpatterns = [
    url(r'^detail$', AmountDetailView.as_view()),
    url(r'^total$', AmountTotalView.as_view()),
]
