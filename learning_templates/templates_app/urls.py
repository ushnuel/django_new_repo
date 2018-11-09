from django.conf.urls import url
from templates_app import views

#TEMPLATE TAGGING
app_name = 'templates_app'

urlpatterns = [
    url('other/', views.other, name='other'),
    url('relative', views.relative, name='relative')
]
