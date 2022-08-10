from service.celery import app


@app.task
def perform_task():
    print("Task is performing")