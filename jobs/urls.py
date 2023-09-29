from django.urls import path
from jobs.barcode.job import queue_barcode_redis_job, get_barcode_redis_job
from jobs import ocr

urlpatterns = [
    path("ocr/", ocr.queue_ocr_redis_job),
    path("ocr/<str:pk>", ocr.get_ocr_redis_job),
    path("barcode/", queue_barcode_redis_job),
    path("barcode/<str:pk>", get_barcode_redis_job),
]
