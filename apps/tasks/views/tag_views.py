from rest_framework.response import Response
from rest_framework.views import Request
from rest_framework.views import APIView
from rest_framework import status

from ..models.tag import Tag
from ..serializers.tag_serializers import TagSerializer
from ..models import *


class TagApi(APIView):

    def get_one(self, request, pk):
        tag = Tag.objects.get(pk=pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        tag = Tag.objects.get(pk=pk)
        serializer = TagSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tag = Tag.objects.get(pk=pk)
        tag.delete()
        return Response(data={'message': f'Tag {pk} deleted.'}, status=status.HTTP_200_OK)


class TagListApi(APIView):
    def get_all(self, request):
        tag = Tag.objects.all()
        serializer = TagSerializer(tag, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
