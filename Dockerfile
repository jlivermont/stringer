FROM python:3.7.1-alpine

EXPOSE 8888

RUN mkdir /app
COPY . /app
RUN pip install -r /app/requirements.txt

WORKDIR /app
CMD ["gunicorn", "--access-logfile", "-", "-b", "0.0.0.0:8888", "stringer:app"]
