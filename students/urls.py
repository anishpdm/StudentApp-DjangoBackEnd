from django.urls import path,include
from . import views

urlpatterns = [
    path('viewall/', views.viewAll , name="viewall" ),
    path('add/', views.addStudent,name='add'),
    path('search/', views.SearchStudent,name='search'),
    path('log/', views.SearchStud,name='log'),
    path('id/', views.SearchStudById,name='id'),
    path('delete/', views.DeleteStudentDetails,name='delete'),
    path('update/', views.UpdateStudentDetails,name='update'),

]