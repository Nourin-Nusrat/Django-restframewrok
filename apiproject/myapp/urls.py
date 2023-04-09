from django.urls import path
from myapp import views

urlpatterns = [
    path('myapi/', views.api_list),
    path('Breed/', views.api_listB),
    path('apidetails/<int:pk>/', views.api_detail),
]