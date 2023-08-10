from django.urls import path
from .views import home_page, gene_page,ment

urlpatterns = [
    path('',home_page,name='home'),
    path('gene', gene_page, name='story'),
    path('element', ment,name= 'element')
]
