# BioContainers @ TACC 

Search the BioContainers modules that are installed on TACC's compute resources at: [BioContainers @ TACC](https://biocontainers.tacc.utexas.edu/search)

## Development

Set up environment files
```
cp .env.dev.sample .env.dev
cp .env.dev.db.sample .env.dev.db
```
and edit.
- To start up the service

```
  docker-compose up -d --build
```

- Troubleshoot using docker-compose logs

```
  docker-compose logs -f

```
- Bring down all volumes:

```
  docker-compose down -v
```

- Launch service at:

```
  https://localhost:5000

```

## Production

Set up environment files
```
cp .env.prod.sample .env.prod
cp .env.prod.db.sample .env.prod.db
```
and edit.

- To start up the service

```
  docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

- Troubleshoot using docker-compose logs

```
  docker-compose logs -f

```
- Bring down all volumes:

```
  docker-compose -f docker-compose.yml -f docker-compose.prod.yml down -v
```

- Launch service at:

```
  https://localhost:5000

```
