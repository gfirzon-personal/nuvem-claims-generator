### Build Docker image and prune orpans so not to have to deelete old image
```sh
docker build -t nuvem-claims-generator-image . && docker image prune -f
```

### Run the docker container using the image with volume
Note: make sure to create docker volume named 'test-volume' prior to running this
```sh
docker run -it -v test-volume:/app/data --name nuvem-claims-generator -p 8503:8000 nuvem-claims-generator-image:latest
```

### Run the docker container using the image and specified docker network (UNUSED for now)
```sh
docker run --name claims-injestion-container --network kafka-net -p 8000:8000 claims-injestion-image
```