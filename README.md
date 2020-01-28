# EventsApp


### Run project

Install the requirements

[Geospatial libraries](https://docs.djangoproject.com/en/3.0/ref/contrib/gis/install/geolibs/)

```
pip3 install -r requirements.py
```

Create Database

```
docker run --name=postgis -d -e POSTGRES_USER=user001 -e POSTGRES_PASS=123456789 -e POSTGRES_DBNAME=gis -p 5432:5432 kartoza/postgis:9.6-2.4
```

### Run App

Make migrations and create super user
```
python3 manage.py makemigrations logic
python3 manage.py migrate
python3 manage.py createsuperuser
```


```
python3 manage.py runserver 
```

To test the REST API 

localhost:8000/api/events/

localhost:8000/api/events/construction/

(...)


Docker compose not complete

