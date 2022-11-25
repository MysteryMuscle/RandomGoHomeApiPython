from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from relay_novel.models import relay_novel
from relay_novel.serializers import relay_novelSerializer

# Create your views here.


class RelayNovels(APIView):

    def get(self, request):
        relay_novel1 = relay_novel.objects.all()
        serializer = relay_novelSerializer(relay_novel1, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class RelayNovelDetail(APIView):

    def get(self, request, id):
        # get novel
        novel = relay_novel.objects.get(id=id)
        serializer = relay_novelSerializer(novel)
        return Response(serializer.data)

    def post(self, request, id):
        # reply novel
        prev = relay_novel.objects.get(id=id)
        new_novel = prev.reply(request)
        serializer = relay_novelSerializer(new_novel)
        return Response(serializer.data, status=201)