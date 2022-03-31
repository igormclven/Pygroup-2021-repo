"""KanBack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from boards import views

"""
router = routers.DefaultRouter()
router.register(r'boards', views.boards_list, 'board')
router.register(r'boards', views.boards_detail, 'board')
router.register(r'columns', views.columns_list, 'column')
router.register(r'columns', views.columns_detail, 'column')
router.register(r'users', views.users_list, 'user')
router.register(r'users', views.users_detail, 'user')
router.register(r'tasks', views.tasks_list, 'task')
router.register(r'tasks', views.tasks_detail, 'task')
"""
router = routers.DefaultRouter()
router.register(r'boards', views.BoardView, 'board')
router.register(r'columns', views.ColumnView, 'column')
router.register(r'tasks', views.TaskView, 'task')
router.register(r'users', views.UserView, 'user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]


"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/boards/', views.boards_list),
    path('api/tasks/', views.tasks_list),
    path('api/columns/', views.columns_list),
    path('api/users/', views.users_list),
    path('api/tasks/<int:pk>/', views.tasks_detail),
    path('api/columns/<int:pk>/', views.columns_detail),
    path('api/boards/<int:pk>/', views.boards_detail),
    path('api/users/<int:pk>/', views.users_detail),
]
"""
