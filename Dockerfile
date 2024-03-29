FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r /app/requirements.txt --no-cache-dir

COPY ../ /app

CMD ["python", "manage.py", "runserver", "0:8000"]