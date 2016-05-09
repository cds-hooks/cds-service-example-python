# cds-service-example-python

Simple Python and Flask server that acts as a CDS Service

## Usage
This card service can be deployed with docker. By default, the Dockerfile exposes port 5000. Creating the docker container can be done by:

```bash
$ docker build -t <your-name>/cds-service-example-python .
Successfully built <container-id>

$ docker run -p 5000:5000 -d --rm <your-name>/cds-service-example-python
```

