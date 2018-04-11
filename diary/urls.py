from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'current', views.current_tasklist)
]