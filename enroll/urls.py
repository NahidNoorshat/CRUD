from django.urls import path

from . import views


urlpatterns = [
    path('', views.addhere, name='add'),
    path('delete/<int:id>/', views.delet_data, name='deletedate'),
    path('/<int:id>/', views.update, name='update'),
]