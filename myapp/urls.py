from django.urls import path
from . import views

urlpatterns = [
    path('', views.holaMundo),
    path('name/<str:username>', views.names),
    path('projects/', views.projects),
    path('task/<int:id>', views.tasks)
]