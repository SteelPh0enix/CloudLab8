# Lab8 - Fibonacci - backend

This is backend part of dockerized Fibonacci calculator app.

## Running the container

First, build it:

```bash
docker build -t fibo_backend .
```

And the you can check the app out by running the container in interactive mode:

```bash
docker run -it -p 8080:8080 fibo_backend
```
