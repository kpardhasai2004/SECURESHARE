from django.urls import path
from . import views

urlpatterns = [
    path('', views.file_list, name='file_list'),
    path('upload/', views.upload_file, name='upload_file'),
    path('access/<uuid:access_code>/', views.access_file, name='access_file'),
    path('receive/', views.receive_function, name='receive_function'),
    path('share/<uuid:access_code>/', views.share_file, name='share_file'),
]