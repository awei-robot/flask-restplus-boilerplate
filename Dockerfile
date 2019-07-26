FROM python:3.6

EXPOSE 5000

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY app /app/app
COPY Makefile /app
COPY manage.py /app

CMD python manage.py run
