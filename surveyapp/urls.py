from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^survey/$', views.SurveyView.as_view(), name='survey'),
]