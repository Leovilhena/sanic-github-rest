FROM python:3.7.0-slim
LABEL maintainer="leosvilhena@icloud.com"

ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux
ENV HOST 'localhost'
ENV PORT 80
ENV USER ''

RUN mkdir app
WORKDIR /app

COPY requirements.txt ./
COPY webserver.py ./
COPY helpers.py ./

RUN set -ex \
    && apt-get update -yqq \
    && apt-get install -yqq --no-install-recommends \
        python-pip \
        python-dev \
        build-essential \
        apt-utils \
        locales \
        curl \
    && sed -i 's/^# en_US.UTF-8 UTF-8$/en_US.UTF-8 UTF-8/g' /etc/locale.gen \
    && locale-gen \
    && update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 \
    && pip install -r requirements.txt \
    && apt-get purge --auto-remove -yqq python-dev \
    && apt-get purge --auto-remove -yqq build-essential \
    && apt-get clean

RUN chmod u+x ./webserver.py
RUN chmod u+x ./helpers.py

EXPOSE 80, 42101

ENTRYPOINT ["python3.7", "webserver.py"]