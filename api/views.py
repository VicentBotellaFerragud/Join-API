from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from django.contrib.auth.models import User
from .serializers import UserSerializer, TaskSerializer

# Create your views here.

@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'User List':'/user-list/',
        'User Detail View':'user-detail/<str:pk>/',
        'User Create':'/user-create/',
        'User Update':'user-update/<str:pk>/',
        'User Delete':'user-delete/<str:pk>/',
        'Task List':'/task-list/',
        'Task Detail View':'task-detail/<str:pk>/',
        'Task Create':'/task-create/',
        'Task Update':'task-update/<str:pk>/',
        'Task Delete':'task-delete/<str:pk>/'
    }

    return Response(api_urls)

# CRUD operations for the User objects.

def getAllUsers(request):

    users = User.objects.all()

    if not users:
        return Response("The user list is empty.")

    else:
        serializer = UserSerializer(users, many = True)

    return Response(serializer.data)

@api_view(['GET'])
def userList(request):

    return getAllUsers(request)

@api_view(['GET'])
def userDetail(request, pk):

    try: 
        user = User.objects.get(id = pk)
        serializer = UserSerializer(user, many = False) 

    except User.DoesNotExist: 
        return Response("There is no user with id '" + pk + "'.")

    return Response(serializer.data)  

@api_view(['POST'])
def userCreate(request):

    try: 
        user = User.objects.get(username = request.data.get('username'))
        return Response("There is already one user with the username '" + user.username + "'.")

    except User.DoesNotExist: 
        data = {'username': request.data.get('username'), 'password': request.data.get('password')}
        serializer = UserSerializer(data = data)

        if serializer.is_valid():
            serializer.save()

    return getAllUsers(request) 

@api_view(['PUT'])
def userUpdate(request, pk):

    try: 
        user = User.objects.get(id = pk)
        data = {'username': request.data.get('username'), 'password': request.data.get('password')}
        serializer = UserSerializer(instance = user, data = data)

        if serializer.is_valid():
            serializer.save()

    except User.DoesNotExist: 
        return Response("It is not possible to update the passed-in user because there is no user with id '" + pk + "'.")

    return getAllUsers(request) 

@api_view(['DELETE'])
def userDelete(request, pk):

    try: 
        user = User.objects.get(id = pk)
        user.delete()

    except User.DoesNotExist: 
        return Response("It is not possible to delete the passed-in user because there is no user with id '" + pk + "'.")

    return getAllUsers(request)   

# CRUD operations for the Task objects.

def getAlltasks(request):

    tasks = Task.objects.all()

    if not tasks:
        return Response('The task list is empty.')
    
    else:
        serializer = TaskSerializer(tasks, many = True)

    return Response(serializer.data)

@api_view(['GET'])
def taskList(request):

    return getAlltasks(request)

@api_view(['GET'])
def taskDetail(request, pk):

    try: 
        task = Task.objects.get(id = pk)
        serializer = TaskSerializer(task, many = False)

    except Task.DoesNotExist: 
        return Response("There is no task with id '" + pk + "'.")

    return Response(serializer.data) 

@api_view(['POST'])
def taskCreate(request):

    try:
        assignee = User.objects.get(username = request.data.get('assignee'))
        creator = User.objects.get(username = request.data.get('creator'))

        data = {
            'title': request.data.get('title'), 
            'description': request.data.get('description'), 
            'priority': request.data.get('priority'), 
            'state': request.data.get('state'), 
            'creation_date': request.data.get('creation_date'), 
            'completion_date': request.data.get('completion_date'), 
            'assignee': assignee.id,
            'creator': creator.id
        }

        serializer = TaskSerializer(data = data)

        if serializer.is_valid():
            serializer.save()

    except User.DoesNotExist:
        return Response("Both the assignee and the task creator must be existing users.")

    return getAlltasks(request)  

@api_view(['PUT'])
def taskUpdate(request, pk):

    try:
        task = Task.objects.get(id = pk)

        assignee = User.objects.get(username = request.data.get('assignee'))
        creator = User.objects.get(username = request.data.get('creator'))

        data = {
            'title': request.data.get('title'), 
            'description': request.data.get('description'), 
            'priority': request.data.get('priority'), 
            'state': request.data.get('state'), 
            'creation_date': request.data.get('creation_date'), 
            'completion_date': request.data.get('completion_date'), 
            'assignee': assignee.id,
            'creator': creator.id
        }

        serializer = TaskSerializer(instance = task, data = data)

        if serializer.is_valid():
            serializer.save()

    except Task.DoesNotExist:
        return Response("It is not possible to update the passed-in task because there is no task with id '" + pk + "'.")

    return getAlltasks(request)

@api_view(['DELETE'])
def taskDelete(request, pk):

    try:
        task = Task.objects.get(id = pk)
        task.delete()

    except Task.DoesNotExist:
        return Response("It is not possible to delete the passed-in task because there is no task with id '" + pk + "'.")

    return getAlltasks(request)    
