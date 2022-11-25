from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from relay_novel.models import relay_novel
from relay_novel.serializers import relay_novelSerializer

# Create your views here.

class relay_novel_list(APIView):
    
    def get(self, request):
        relay_novel1 = relay_novel.objects.all()
        serializer = relay_novelSerializer(relay_novel1, many=True)
        return Response(serializer.data)

    def post(self):
        pass