#relay_novel/serializers.py

from rest_framework import serializers
from relay_novel.models import relay_novel

class relay_novelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = relay_novel
        fields = '__all__'