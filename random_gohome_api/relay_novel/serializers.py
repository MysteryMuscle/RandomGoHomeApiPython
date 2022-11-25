#relay_novel/serializers.py

from rest_framework import serializers
from .models import relay_novel

class relay_novelSerializer(serializers.ModelSerializer):
    class Meta:
        model = relay_novel
        fields = '__all__'