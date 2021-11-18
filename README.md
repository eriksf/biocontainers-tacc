# BioContainers @ TACC 
# git commit
Search the BioContainers modules that are installed on TACC's compute resources at: [BioContainers @ TACC](https://biocontainers.tacc.utexas.edu/search)


## To start up the service

```
  docker-compose -f docker-compose.yml up -d --build
  docker-compose -f docker-compose.yml exec web python manage.py create_db
  docker-compose -f docker-compose.yml exec web python manage.py seed_db
```

- Troubleshoot using docker-compose logs

```
  docker-compose logs -f

```
- Bring down all volumes:

```
  docker-compose -f docker-compose.yml down -v
```

- Launch service at:

```
  https://localhost:5000

```
