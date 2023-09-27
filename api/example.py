from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import serializers
from django.db import models
from django.contrib import admin

# IMPORTANT: Make sure to add new views to api/urls.py


# Split into api/models.py
class ExampleModel(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=10000, null=True, blank=True, default="")

    class Meta:
        verbose_name = "Example"
        verbose_name_plural = "Examples"


# Split into api/serializers.py
class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = "__all__"


# Split into api/views.py
class ExampleListView(ListCreateAPIView):
    authentication_classes = []
    permission_classes = []

    queryset = ExampleModel.objects.all()
    serializer_class = ExampleSerializer


class ExampleDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    permission_classes = []

    queryset = ExampleModel.objects.all()
    serializer_class = ExampleSerializer


# Split into api/admin.py
admin.site.register(ExampleModel)
