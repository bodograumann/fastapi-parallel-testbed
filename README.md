# Controlling parallel requests in inboard/FastAPI

The server will sleep for a certain amount of time and then return.

Start with

```
docker build -t fastapi-parallel .
docker run -p 80:80 --rm --name fastapi-parallel fastapi-parallel
```

Run a request with (or many in parallel)

```
curl http://localhost/sleep
```

To enable concurrency use

```
curl http://localhost/asyncsleep
```

instead.

