from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from django.shortcuts import get_object_or_404

from .models import Project
from .serializer import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @action(detail=True, methods=['get'])
    def elements(self, request, pk=None):
        queryset = Project.objects.all()
        serializer = ProjectSerializer(queryset, many = True)
        return Response(serializer.data)