FROM python:alpine3.8
WORKDIR /home/python/app
COPY app /home/python/app/
RUN pip install -r requirements.txt
CMD uvicorn --host "0.0.0.0" --port 8000 app:app --reload