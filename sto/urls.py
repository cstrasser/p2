from django.conf.urls import patterns, url
from sto import views

urlpatterns = (
    
    url(r'^$', 'sto.views.sto_list', name='sto_list'),
    
)