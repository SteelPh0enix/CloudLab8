FROM python:3.9-alpine

WORKDIR /backend_app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=fibonacci
ENV FLASK_ENV=development

CMD ["python", "-m", "flask", "run", "--no-debugger", "--host", "0.0.0.0", "--port", "8080"]
