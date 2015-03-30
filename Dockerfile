FROM aexea/aexea-base
MAINTAINER Aexea Carpentry

RUN apt-get install g++
RUN pip3 install wagtail

ADD project/requirements.txt /opt/code/requirements.txt
WORKDIR /opt/code
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn django-extensions

ADD project /opt/code

RUN chown -R uid1000: .
RUN mkdir /log
RUN chown -R uid1000: /log
RUN mkdir -p static
RUN chown -R uid1000: static
RUN mkdir -p media
RUN chown -R uid1000: media

EXPOSE 8000

ENTRYPOINT ./start.sh
CMD web
