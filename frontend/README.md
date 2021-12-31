# Lab8 - Fibonacci - frontend

This is frontend part of dockerized Fibonacci calculator app.

## Running the container

First, build it:

```bash
docker build -t fibo_frontend .
```

And the you can check the app out by running the container in interactive mode:

```bash
docker run -it -p 80:8000 fibo_frontend
```
