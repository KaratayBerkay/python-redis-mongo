FROM python:3

COPY ./requirements.txt ./var/application/requirements.txt

WORKDIR /var/application

RUN pip install --no-cache-dir -r /var/application/requirements.txt

COPY . /var/application

CMD [ "python", "-m", "/var/application/app" ]
