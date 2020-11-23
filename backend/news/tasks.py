from backend.celery import app
from .service import start_parsing


@app.task()
def run_parsers():
    start_parsing()
