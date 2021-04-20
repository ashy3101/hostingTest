from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns=[
    path('', views.myFirstClass.as_view(), name="Form submit"),
    path('display',views.variable_template.as_view(template_name='home.html'), name="can define variable template in URLs"),
    path('home',views.variable_template.as_view(template_name='index.html'), name="can define variable template in URLs"),
]