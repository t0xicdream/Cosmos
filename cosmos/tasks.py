from celery import shared_task

from cosmos.async_requests.executor import get_executor


@shared_task
def execute_async_requests():
    get_executor.execute()
