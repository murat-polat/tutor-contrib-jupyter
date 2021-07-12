FROM ubuntu:20.04
LABEL maintainer="MP"

#USER root

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update \
 && apt-get install -yq --no-install-recommends \
    build-essential \
    ca-certificates \
    locales \
    python3-dev \
    python3-pip \
    python3-pycurl \
    nodejs \
    npm \
    nano \
    vim \
    r-base \
    r-base-dev \ 
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --upgrade setuptools pip wheel


RUN mkdir -p /src/jupyterhub/
WORKDIR /src/jupyterhub/

RUN npm install -g configurable-http-proxy
RUN python3 -m pip install jupyterhub
RUN python3 -m pip install notebook 
RUN pip3 install jupyterlab

RUN cd /src/jupyterhub/
RUN jupyterhub --generate-config

COPY jupyterhub_config.py /src/jupyterhub/jupyterhub_config.py
COPY requirements.txt /src/jupyterhub/requirements.txt
RUN pip3 install -r requirements.txt
RUN apt-get update


EXPOSE 8000
## Create user and administrator

RUN useradd -ms  /bin/bash student 
RUN echo 'student:solo' | chpasswd
RUN usermod -aG sudo student
RUN useradd -ms   /bin/bash teacher
RUN echo 'teacher:soloadmin' | chpasswd
RUN usermod -aG sudo teacher

#COPY demo.ipynb /home/student/


CMD ["jupyterhub -f /src/jupyterhub/jupyterhub_config.py"]
