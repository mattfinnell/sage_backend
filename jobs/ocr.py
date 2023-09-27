from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django_rq import job, get_connection
from django_rq.jobs import Job
from rq import exceptions

import easyocr
import hashlib
import urllib.request

@job
def ocr_redis_job(image_url):
    hash = hashlib.new('sha256')
    hash.update(image_url.encode())

    local_image_path = f"/workspaces/backend/.data/{hash.hexdigest()[:8]}"
    urllib.request.urlretrieve(image_url, local_image_path)

    reader = easyocr.Reader(["en"], gpu=False)
    return " ".join([annotation for (_, annotation, confidence) in reader.readtext(local_image_path) if confidence > 0.3])

@api_view(["POST"])
def queue_ocr_redis_job(request):
    job = ocr_redis_job.delay(request.data["image_url"])

    return Response(job.id)


@api_view(["GET"])
def get_ocr_redis_job(request, *args, **kwargs):
    job_id = kwargs.get("pk")
    if not job_id:
        return Response("Could Not get Job ID", status=status.HTTP_400_BAD_REQUEST)

    try:
        job = Job.fetch(id=job_id, connection=get_connection())
    except exceptions.NoSuchJobError:
        return Response("Job Not Found / Expired", status=status.HTTP_404_NOT_FOUND)

    return Response({"parsed_text": job.result}, status=status.HTTP_201_CREATED)
