## Jupyterhub for Tutor Open edX




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









