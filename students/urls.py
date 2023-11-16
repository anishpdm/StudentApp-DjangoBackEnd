from django.urls import path,include
from . import views

urlpatterns = [
    path('viewall/', views.viewAll , name="viewall" ),
    path('add/', views.addStudent,name='add')
]