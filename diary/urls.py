from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'current', views.current_tasklist, name='active'),
    url(r'complete', views.complete_taslist, name='done'),
]