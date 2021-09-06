## Jupyterhub plugin for Tutor Open edX 

- Jupyterhub and JupyterLab runs as a subdomain of Tutor
- Comes with Pandas, Bokeh, Numpy and other popular libraries.
- Allow to create multiple users, which has own kernel


### Installation:

`git clone https://github.com/murat-polat/tutor-contrib-jupyter`

`pip3 install -e tutor-contrib-jupyter`

`tutor plugins list`

`tutor plugins enable jupyter`

`tutor config save`

Rebuild your edX platform with plugin and Jupyterhub-XBlock


`tutor images build openedx`

`tutor local quickstart`


### Create multiple Notebook users (Spawners)

Login as a teacher(password: soloadmin) => clik to Control Panel then => Admin

![](/src/adminPanel.jpg)

Here you can add multiple user which is pre installed via the Dockerfile (https://github.com/murat-polat/tutor-contrib-jupyter/blob/master/tutorjupyter/templates/jupyter/build/jupyter/Dockerfile).. By default can be added 100 users(edx0,edx1, edx2..... edx100), which can be populated in user_list.txt file (https://github.com/murat-polat/tutor-contrib-jupyter/blob/master/tutorjupyter/templates/jupyter/build/jupyter/user_list.txt)

Exampel: 
We want to add 10 new JupyterLab users. To do that, click to => Add Users button, usernames sparated by lines, then => Add Users. 

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

Jupyterhub XBlock comes with to main users " student (password: solo) " and " teacher (password: soloadmin) ". You can change password and create mulitable users and administrators, which will be explained soon.

- login to studio as a staff or superuser
- Create a course, than settings=>advanced settings=> Advanced Module List add  `"jupyterhub"` and save

![](/src/advanced_module.jpg)
- Now you can use JupyterHub as a Unit, for every type of course. But first, you need to edit your JupyterHub (Name, ButtonText, JupyterHub URL, JupyterNotebook URL(you will create this later) and JupyterLab URL )

![](/src/edit_studio.jpg)

- You need to create a notebook for students view in your course. To do that click  " `Start JupyterHub in new tab`" login as " student " password is "solo". Then New => Python3(ipykernel). dobbel click to "Untitled" and rename it whatever you want.

### JupyterLab:

JupyterLab is next-generations, great advanced tools for everyone. Not just a notebook,that comes with text editor, console, terminal, Jitsi-Meet and much more. For more information please visit https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html

To start JupyterLab just click the " Start JupyterLab in new tab " Now all lab ready for every Hub users.


Now you can write your entire course with Jupyter tools :)

![](/src/Lab.png)

 Copy the URL of your notebook and paste in " Edit=> JupyterHub or Lab URL" save and refresh your page. Now your notebook is ready to publish.


![](/src/XblockOverview.jpg)

https://github.com/murat-polat/jupyterhub-xblock

