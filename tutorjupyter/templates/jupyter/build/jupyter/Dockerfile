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

EXPOSE 8000

CMD ["jupyterhub"]















# FROM debian

# LABEL MAINTAINER=MP
# RUN apt-get update && apt-get -y upgrade

# RUN apt-get -y install python3-pip  git curl 
# RUN mkdir /openedx  openedx/jupyter

# WORKDIR /openedx/jupyter

# RUN apt-get -y install node-gyp nodejs npm && npm install npm@latest -g

# RUN npm install -g configurable-http-proxy
# RUN pip3 install --upgrade pip
# #RUN pip3 install Rust >=1.41.0
# RUN pip3 install jupyterhub
# RUN pip3 install --upgrade notebook

# EXPOSE 8000

# CMD [ "jupyterhub" ]

