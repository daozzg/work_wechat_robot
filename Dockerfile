FROM python:3.6.8-stretch

WORKDIR /usr/src/app/

RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list && \
    sed -i 's/security.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
RUN  apt-get -y update && apt-get install -y default-libmysqlclient-dev curl vim
COPY ./requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
COPY . /usr/src/app/

EXPOSE 8080

CMD ["python", "/usr/src/app/app.py"]

