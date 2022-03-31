from asyncio import tasks
from multiprocessing import context
import this
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.
# GET & POST views
"""
@api_view(['GET','POST'])
def boards_list(request):
    if request.method == 'GET':
        data = Board.objects.all()
        serializer = BoardSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def tasks_list(request):
    if request.method == 'GET':
        data = Task.objects.all()
        serializer = TaskSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def columns_list(request):
    if request.method == 'GET':
        data = Column.objects.all()
        serializer = ColumnSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ColumnSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def users_list(request):
    if request.method == 'GET':
        data = User.objects.all()
        serializer = UserSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# PUT & DELETE views

@api_view(['PUT', 'DELETE'])
def boards_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = BoardSerializer(board, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT', 'DELETE'])
def tasks_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT', 'DELETE'])
def columns_detail(request, pk):
    try:
        column = Column.objects.get(pk=pk)
    except Column.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = ColumnSerializer(column, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        column.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT', 'DELETE'])
def users_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""






#Cosas

class BoardView(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()


class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class ColumnView(viewsets.ModelViewSet):
    serializer_class = ColumnSerializer
    queryset = Column.objects.all()


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
