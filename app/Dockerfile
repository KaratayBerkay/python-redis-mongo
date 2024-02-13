FROM python:3

COPY ./requirements.txt ./var/app/requirements.txt

WORKDIR /var/app

RUN pip install --no-cache-dir -r /var/app/requirements.txt

COPY . /var/app

CMD [ "python", "-m", "app" ]