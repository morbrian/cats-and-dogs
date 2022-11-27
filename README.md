# simple data services

This is mostly a sample from here: https://flask-restx.readthedocs.io/en/latest/scaling.html

The running services has a couple REST endpoints to view static cat or dog data, with swagger documentation.

Goal was to explore `flask_restx` and python project repository structure. 
Beyond that, it's useful to have some dummy services for other local testing.

## Run for development:

```
pip install flask_restx
flask run
```

## Access swagger docs:

```
http://127.0.0.1:5000
```

## Docker

Build image:

```
docker build -t sample-flask .
```

Run image:

```
docker run -p 8080:8080 sample-flask
```

Access running container:

```
http://localhost:8080/
```
