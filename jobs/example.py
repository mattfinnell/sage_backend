from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django_rq import job, get_connection
from django_rq.jobs import Job
from rq import exceptions

import time

@job
def example_redis_job(name):
    time.sleep(15.0)
    return f"Hello World, {name}"


@api_view(['POST'])
def queue_example_redis_job(request):
    job = example_redis_job.delay(request.data["name"])

    return Response(job.id)

@api_view(['GET'])
def inspect_example_redis_job(request, *args, **kwargs):
    job_id = kwargs.get("pk")
    if not job_id:
        return Response("Could Not get Job ID", status=status.HTTP_400_BAD_REQUEST)

    try:
        job = Job.fetch(id=job_id, connection=get_connection())
    except exceptions.NoSuchJobError:
        return Response("Job Not Found / Expired", status=status.HTTP_404_NOT_FOUND)

    return Response(
        {
            "job_id": job_id,
            "job_result": job.result + " from functional views!!!",
        }
    )
