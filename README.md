## Jupyterhub plugin for Tutor Open edX 

- Jupyterhub runs as a subdomain of Tutor
- Comes with Pandas, Bokeh, Numpy and other popular libraries.
- Allow to create multiple users, which has own kernel

Please test it before using in production !!


### Installation:

`git clone https://github.com/murat-polat/tutor-contrib-jupyter`

`pip3 install -e tutor-contrib-jupyter`

`tutor plugins list`

`tutor plugins enable jupyter`

`tutor config save`

`tutor images build jupyter`

`tutor local quickstart`


### Create multiple Notebook users (Spawners)

`docker exec -it tutor_local_jupyter_1 bash`

`adduser <username>`

![](/src/addUser.png)

You can create multiple user with same Unix command






### Open edX Studio integration:

To integrate JupyterHub plugin to the Open edX Studio, please install this XBlock( https://github.com/murat-polat/jupyterhub-xblock )


 [![](/src/youtube.jpg)](https://www.youtube.com/watch?v=f-tsGIxYq7c)

