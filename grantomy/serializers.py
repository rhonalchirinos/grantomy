# todo/todo_api/serializers.py
from rest_framework import serializers

from .models import Zeus, ZeusDni, ZeusDocument
from django.contrib.auth.hashers import make_password

class ZeusSerializer(serializers.ModelSerializer):

    def __init__(self, data, organizer):
        super().__init__(data=data)
        self.organizer = organizer

    class Meta:
        model = Zeus
        fields = ["identifier", "email", "phone", "external_identifier", "notes", "locale", "title", "edad", "password"]

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        zeus = Zeus.objects.create(organizer=self.organizer, **validated_data)
        return zeus


class ZeusDniSerializer(serializers.ModelSerializer):

    class Meta:
        model = ZeusDni
        fields = ["title", "front", "backend"]

    def create(self, validated_data):
        zeus = ZeusDni.objects.create(**validated_data)
        return zeus


class ZeusDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ZeusDocument
        fields = ["document"]

    def create(self, validated_data):
        print("+++++++++++++++++++++++++++++++++++")
        print(validated_data["document"])
        document = validated_data["document"].file.read()
      
        print("+++++++++++++++++++++++++++++++++++")

        #   data = { "document": validated_data['document'].file}

        zeus = ZeusDocument.objects.create(**{ "document": document})
        return zeus
