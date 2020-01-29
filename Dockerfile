FROM python:3

RUN mkdir /eventsapp
WORKDIR /eventsapp
RUN apt-get update && apt-get install -y software-properties-common
RUN apt-get -y install binutils libproj-dev gdal-bin
COPY requirements.txt /eventsapp/
RUN pip3 install -r requirements.txt
COPY . /eventsapp/

ENTRYPOINT ["/eventsapp/events-db.sh"]