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

class RelayNovelReply(APIView):

    def post(self, request):
        
        # validate data
        # if data is valid, then reply
        # else, return error

        prev_id = request.data.get('prev')
        content = request.data.get('content')
        author = request.data.get('author')
        image = request.data.get('image')
        url = request.data.get('url')

        prev = relay_novel.objects.get(id=prev_id)
        new_novel = prev.reply(content, author, image, url)

        serializer = relay_novelSerializer(new_novel)
        return Response(serializer.data, status=201)
        

        