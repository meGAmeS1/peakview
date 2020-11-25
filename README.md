# Peakview
This is a demo project based on Django and DRF that allows to store peaks data.

## Start from docker
Run these commands to start the project:

```sh
docker-compose -f docker-compose.yml up -d --build
docker-compose -f docker-compose.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.yml exec web python manage.py collectstatic --no-input --clear
```

The project will be running at http://localhost:1337/

## Project info
The API can be browsed from your web browser or you can used the saved Postman endpoints in the `postman` folder.

The docker stack is launching 3 containers: one for the database (postgreSQL), one for the application (started via gunicorn) and one for the web server (nginx).

The application is made with love and Django (with GeoDjango and Django Rest Framework)

## Endpoints
### List all peaks
Method: `GET`

URL: `/peaks/`

Info: Will list every peaks in the DB

### Filter peaks 
Method: `GET`

URL: `/peaks/`

Info: to filter peaks in a given bounding box

Query parameters:
* in_bbox : `minLon,minLat,maxLon,maxLat`

### Retrieve peak
Method: `GET`

URL: `/peaks/1/`

### Create peak
Method: `POST`

URL: `/peaks/`

Data:
```json
{
    "name": "Peak name",
    "location": {
        "type": "Point",
        "coordinates": [
            1.23046875,
            2.585444257384886
        ]
    },
    "elevation": 3300.0
}
```

### Edit peak
Method: `PUT`

URL: `/peaks/1/`

Data:
```json
{
    "name": "New peak name",
    "location": {
        "type": "Point",
        "coordinates": [
            1.23046875,
            2.585444257384886
        ]
    },
    "elevation": 3300.0
}
```

### Delete peak
Method: `DELETE`

URL: `/peaks/1/`


## Administration
You'll need a super user for that: `docker-compose -f docker-compose.yml exec web python manage.py createsuperuser`

Then go to http://localhost:1337/admin/ to get the admin panel.