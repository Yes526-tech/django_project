from os import stat
from django.http.response import JsonResponse
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from rest_framework import status
from rest_framework.serializers import Serializer


from todo_app.serializers import TodoSerializer

class TodoAPIView(APIView):
    serializer_class = TodoSerializer
    
    
    def get(self,request, pk=None, format=None):
        with open('todos.json') as json_file:
            data = json.load(json_file)
        if pk:
            todo = [item for item in data['items'] if item['id'] == pk]
            return Response({'data': todo})
        return Response({'data': data})
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            id = serializer.validated_data.get('id')
            uuid = serializer.validated_data.get('uuid')
            subject = serializer.validated_data.get('subject')
            projects = serializer.validated_data.get('projects')
            due = serializer.validated_data.get('due')
            completed = serializer.validated_data.get('completed')
            completedDate = serializer.validated_data.get('completedDate')
            archived = serializer.validated_data.get('archived')
            isPriority = serializer.validated_data.get('isPriority')
            notes = serializer.validated_data.get('notes')
            new_todo = { "id": id,
       "uuid": uuid,
       "subject": subject,
       "projects": projects,
       "due": due,
       "completed": completed,
       "completedDate": completedDate,
       "archived": archived,
       "isPriority": isPriority,
       "notes": notes}
            with open('todos.json', 'r+') as file:
                file_data = json.load(file)
                file_data["items"].append(new_todo)
                file.seek(0)
                json.dump(file_data, file, indent=4)
            return Response(new_todo, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                