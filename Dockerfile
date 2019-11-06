FROM		python:3.7-alpine3.9

RUN			echo 'http://dl-cdn.alpinelinux.org/alpine/v3.9/main' >> /etc/apk/repositories
RUN			echo 'http://dl-cdn.alpinelinux.org/alpine/v3.9/community' >> /etc/apk/repositories
RUN			apk add --no-cache mongodb
RUN			mkdir /app && mkdir /db
WORKDIR		/app
ADD			requirements.txt /app
RUN			pip install -r requirements.txt
ADD			mongod.conf mongod.conf
ADD			oms /app/oms

ENTRYPOINT	["python", "-m", "oms.mongodb.app"]
