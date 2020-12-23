from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name = 'index'),
    path('create/',views.create,name = 'create'),
    path('show/<str:pk>',views.show_cv,name = 'show'),
    path('show1/<str:pk>',views.show_cv_for_pdf,name = 'show1'),
    path('delete/<str:pk>',views.deletecv,name = 'delete'),
    # path('show/<str:pk>/pdf',views.generate_PDF,name = 'pdf'),    
    ]