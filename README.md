# Peakview
This is a demo project based on Django and DRF that allows to store peaks data.

## Start from docker
Run these commands to start the project:

```sh
docker-compose -f docker-compose.yml up -d --build
docker-compose -f docker-compose.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.yml exec web python manage.py collectstatic --no-input --clear
```

## Project info
The API can be browsed from your web browser or you can used the saved Postman endpoints in the `postman` folder.

## Administration
You'll need a super user for that: