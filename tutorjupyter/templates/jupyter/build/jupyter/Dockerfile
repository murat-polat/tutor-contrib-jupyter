FROM ubuntu:20.04
LABEL maintainer="MP"


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
    curl \
    vim \
    r-base \
    r-base-dev \ 
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --upgrade setuptools pip wheel
RUN curl -L https://tljh.jupyter.org/bootstrap.py 


RUN mkdir -p /src/jupyterhub/
WORKDIR /src/jupyterhub/

RUN npm install -g configurable-http-proxy
RUN python3 -m pip install jupyterhub
RUN python3 -m pip install notebook 
RUN pip3 install jupyterlab

RUN cd /src/jupyterhub/
RUN jupyterhub --generate-config
## All Jupyter eco system configuration : jupyterhub_config.py ##
COPY jupyterhub_config.py /src/jupyterhub/jupyterhub_config.py
COPY requirements.txt /src/jupyterhub/requirements.txt
COPY user_list.txt /src/jupyterhub/user_list.txt

## All packages, extantions must be added requirements.txt file ##
RUN pip3 install -r requirements.txt
RUN apt-get update

EXPOSE 8000

## Common user ##
RUN adduser  --gecos ""   student 
RUN echo 'student:solo' | chpasswd
## Admin user has Control Panel for user administrations ##
RUN adduser  --gecos ""  teacher
RUN echo 'teacher:soloadmin' | chpasswd
RUN usermod -aG sudo teacher

## User list, pre-created system users ##
RUN chmod +x user_list.txt
RUN newusers -r user_list.txt


CMD ["jupyterhub -f /src/jupyterhub/jupyterhub_config.py"]
