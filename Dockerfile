FROM python:3.6.12-alpine3.12

COPY . ./ntuhBodyTemperature

WORKDIR ntuhBodyTemperature

RUN apk add --update tzdata

RUN pip install -r requirements.txt

RUN crontab resource/crontab

CMD ["crond", "-f"]
