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

Here you can add multiple user which is pre installed via the Dockerfile (https://github.com/murat-polat/tutor-contrib-jupyter/blob/master/tutorjupyter/templates/jupyter/build/jupyter/Dockerfile).. By default can be added 100 users(edx0,edx1, edx2..... edx100), which can be populated in user_list.txt file (https://github.com/murat-polat/tutor-contrib-jupyter/blob/master/tutorjupyter/templates/jupyter/build/jupyter/user_list.txt)

Exampel: 
We want to add 10 new JupyterLab users. To do that, click to => Add Users button, usernames sparated bylines, then => Add Users. 

![](/src/add_users.png)
now you have 10 newuser. Username and password is same (e.g. Username: edx10, Password: edx10) here teacher can access all users notebook or other their files.

For courses " Student " is common user, but all users can use their own server, doesn't matter. Teacher should be uses for user administrations. Because basic user can not see or edit admin(teacher) files :)

### Video chat with Jitsi (WebRTC):
Login which user do you want, give name to your VideoChat rom, then click to "JOIN" button.
![](/src/jitsi.png)

Ask to other paticipants to join your meeting. Link will be same lab, and same rom.
(e.g https://jupyter.yourdomain/user/edx1/lab) login Join the same rom(TestRom)

![](/src/jitsi2.png)





### Open edX Studio integration:

To integrate JupyterHub plugin to the Open edX Studio, please install this XBlock( https://github.com/murat-polat/jupyterhub-xblock )


 [![](/src/youtube.jpg)](https://www.youtube.com/watch?v=f-tsGIxYq7c)

