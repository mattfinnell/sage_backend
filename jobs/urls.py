from django.urls import path
from jobs import example

urlpatterns = [
    path("example/", example.queue_example_redis_job),
    path("example/<str:pk>", example.inspect_example_redis_job),
]
