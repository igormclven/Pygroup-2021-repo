from django.contrib import admin
from .models import Board,Column,Task,User


BoardModels = [Board, Column, Task, User]


# Register your models here.
admin.site.register(BoardModels)