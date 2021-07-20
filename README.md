## Jupyterhub plugin for Tutor Open edX 

- Jupyterhub runs as a subdomain of Tutor
- Comes with Pandas, Bokeh, Numpy and other popular libraries.
- Allow to create multiple users, which has own kernel

![](/src/Lab.png)


### Installation:

`git clone https://github.com/murat-polat/tutor-contrib-jupyter`

`pip3 install -e tutor-contrib-jupyter`

`tutor plugins list`

`tutor plugins enable jupyter`

`tutor config save`

`tutor images build jupyter`

`tutor local quickstart`


### Create multiple Notebook users (Spawners)

Login as a teacher(password: soloadmin) => clik to Control Panel then => Admin

![](/src/adminPanel.jpg)

Here you can add multiple user which is pre installed via the Dockerfile (https://github.com/murat-polat/tutor-contrib-jupyter/blob/master/tutorjupyter/templates/jupyter/build/jupyter/Dockerfile).. By default can be added 100 users(edx0,edx1, edx2..... edx100), which can be populated in user_list.txt file ()






### Open edX Studio integration:

To integrate JupyterHub plugin to the Open edX Studio, please install this XBlock( https://github.com/murat-polat/jupyterhub-xblock )


 [![](/src/youtube.jpg)](https://www.youtube.com/watch?v=f-tsGIxYq7c)

