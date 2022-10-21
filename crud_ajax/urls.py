from django.urls import path
from crud_ajax import views 

urlpatterns = [
    path('',views.IndexView.as_view(),name='inicio'),
    path('crud/',views.ContaView.as_view(),name='crud_ajax'),
    path('create/', views.CreateConta.as_view(),name='create')
]