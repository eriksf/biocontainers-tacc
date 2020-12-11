# biocontainers-tacc

To start up the service

```
  docker-compose -f docker-compose.yml up -d --build
  docker-compose -f docker-compose.yml exec web python manage.py create_db
  docker-compose -f docker-compose.yml exec web python manage.py seed_db
```

Troubleshoot using docker-compose logs

```
  docker-compose logs -f

```
Bring down all volumes:

```
  docker-compose -f docker-compose.yml down -v
```

Launch service at:

```
  https://127.0.0.1:5000

```
