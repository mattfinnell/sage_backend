from jobs.barcode.barcode_handler import BarcodeHandler, BarcodeHandlerFactory
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django_rq import job, get_connection
from django_rq.jobs import Job
from rq import exceptions

@job
def barcode_redis_job(image_url):
    return BarcodeHandlerFactory().get().handle(image_url)


@api_view(["POST"])
def queue_barcode_redis_job(request):
    job = barcode_redis_job.delay(request.data["image_url"])

    return Response(job.id)


@api_view(["GET"])
def get_barcode_redis_job(request, *args, **kwargs):
    job_id = kwargs.get("pk")
    if not job_id:
        return Response("Could Not get Job ID", status=status.HTTP_400_BAD_REQUEST)

    try:
        job = Job.fetch(id=job_id, connection=get_connection())
    except exceptions.NoSuchJobError:
        return Response("Job Not Found / Expired", status=status.HTTP_404_NOT_FOUND)

    return Response({"result": job.result}, status=status.HTTP_201_CREATED)
