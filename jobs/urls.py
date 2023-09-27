from django.urls import path
from jobs import example
from jobs import ocr

urlpatterns = [
    path("ocr/", ocr.queue_ocr_redis_job),
    path("ocr/<str:pk>", ocr.get_ocr_redis_job),
]
