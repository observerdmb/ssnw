from django.conf.urls import url
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^current', views.current_tasklist, name='active'),
    url(r'^complete', views.complete_taslist, name='done'),
    url(r'^$', RedirectView.as_view(url='current'))
]