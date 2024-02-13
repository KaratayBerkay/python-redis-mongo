FROM python:3.10.13

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY . /var/application

RUN pip install --no-cache-dir -r /var/application/requirements.txt

WORKDIR /var/application

RUN echo "Application started"

CMD ["python","-u","app.py"]
