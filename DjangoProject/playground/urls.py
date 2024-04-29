from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('task/<int:pk>', views.tasks, name = 'task'),
    path('update_task/<int:pk>', views.update_task, name = 'update_task'),
    path('delete_task/<int:pk>', views.delete_task, name = 'delete_task'),
    path('add_task/', views.add_task, name = 'add_task'),
    path('view_report/', views.view_report, name = 'view_report')
]


