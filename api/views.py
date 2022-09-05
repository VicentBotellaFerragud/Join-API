from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

# Create your views here.

@api_view(['GET'])
def apiOverview():
    api_urls = {
        'Task List':'/task-list/',
        'Task Detail View':'task-detail/<str:pk>/',
        'Task Create':'/task-create/',
        'Task Update':'task-update/<str:pk>/',
        'Task Delete':'task-delete/<str:pk>/',
    }

    return Response(api_urls)

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
    task = Task.objects.get(id = pk)
    serializer = TaskSerializer(task, many = False)

    return Response(serializer.data)  

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return getAlltasks(request)  

@api_view(['PUT'])
def taskUpdate(request, pk):
    task = Task.objects.get(id = pk)
    serializer = TaskSerializer(instance = task, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return getAlltasks(request)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id = pk)
    task.delete()

    return getAlltasks(request)    
