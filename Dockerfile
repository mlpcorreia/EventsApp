FROM python:3

RUN mkdir /eventsapp
WORKDIR /eventsapp
RUN apt-get update && apt-get install -y software-properties-common
#RUN add-apt-repository ppa:ubuntugis/ppa && apt-get update
RUN apt-get -y install binutils libproj-dev gdal-bin
COPY requirements.txt /eventsapp/
RUN pip3 install -r requirements.txt
COPY . /eventsapp/