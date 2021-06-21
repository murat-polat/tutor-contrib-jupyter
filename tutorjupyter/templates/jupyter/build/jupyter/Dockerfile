FROM ubuntu
LABEL maintainer="MP"

USER root

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
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --upgrade setuptools pip wheel


RUN mkdir -p /src/jupyterhub/
WORKDIR /src/jupyterhub/

RUN npm install -g configurable-http-proxy
RUN python3 -m pip install jupyterhub
RUN python3 -m pip install notebook 

RUN cd /src/jupyterhub/
RUN jupyterhub --generate-config

COPY jupyterhub_config.py /src/jupyterhub/jupyterhub_config.py
COPY requirements.txt /src/jupyterhub/requirements.txt
RUN pip3 install -r requirements.txt



EXPOSE 8000

CMD ["jupyterhub -f /src/jupyterhub/jupyterhub_config.py"]
