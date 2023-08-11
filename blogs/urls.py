from django.urls import path
from .views import home_page, gene_page,ment, travel

urlpatterns = [
    path('',home_page,name='home'),
    path('gene/', gene_page, name='gene'),
    path('travel/',travel, name= 'travel'),
    path('element/', ment,name= 'element'),
]
