#FROM python:3.6
FROM pypy:3.6-stretch
# 使用国内源
#COPY sources.list /etc/apt/sources.list
# 安装supervisor
RUN apt-get update \
    && apt-get install -y supervisor \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# start scripts
COPY runapp.sh /usr/bin/

# supervisor config
ADD app.conf /etc/supervisor/conf.d/

# Run the chmod command to change permissions on above file in the /bin directory
RUN chmod 755 /usr/bin/runapp.sh

EXPOSE 5000

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
RUN pip install gunicorn -i https://mirrors.aliyun.com/pypi/simple/
RUN pip install gevent -i https://mirrors.aliyun.com/pypi/simple/
RUN pip install flask_migrate -i https://mirrors.aliyun.com/pypi/simple/

COPY app /app/app
COPY Makefile /app
COPY manage.py /app
#CMD gunicorn manage:app -w 8 -b 0.0.0.0:5000 -k gevent
#CMD  pypy3 manage.py run
#CMD python manage.py run
