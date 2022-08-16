from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import models, serializers


class NotesViewSet(viewsets.ModelViewSet):
    queryset = models.Notes.objects.all()
    serializer_class = serializers.NotesSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        notes = models.Notes.objects.all().filter(user=request.user)
        serializer = serializers.NotesSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = serializers.NotesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        note = models.Notes.objects.filter(id=pk)
        serializer = serializers.NotesSerializer(instance=note, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        note = models.Notes.objects.get(id=pk)
        note_data = request.data
        serializer = serializers.NotesSerializer(instance=note, data=note_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        note = models.Notes.objects.get(id=pk)
        note.delete()
        resp = {"message": "Note deleted"}
        return Response(resp, status=status.HTTP_202_ACCEPTED)
