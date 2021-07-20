
c.Spawner.args = ['--NotebookApp.tornado_settings={"headers":{"Content-Security-Policy": "frame-ancestors * jupyter:8000"}}']   

c.JupyterHub.tornado_settings = { 'headers': { 'Content-Security-Policy': "frame-ancestors * jupyter:8000"} }

### User Administration ###

c.Authenticator.allowed_users = {'teacher','student'}
c.Authenticator.admin_users = {'teacher'}
c.Authenticator.load_groups = {'learner'}
c.JupyterHub.admin_access = True
c.Authenticator.create_system_users = True






# # Users
# c.Authenticator.whitelist = {'student', 'teacher'}
# # Admins
# c.Authenticator.admin_users = {'teacher'}
# # Admins can create/delete users
# c.Authenticator.create_system_users=True





#c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
# c.DummyAuthenticator.auto_login = True
#c.DummyAuthenticator.allowed_users = {}
#c.DummyAuthenticator.admin_users = {'teacher'}
#c.JupyterHub.admin_access = True
#c.DummyAuthenticator.password = "solocat"
#c.DummyAuthenticator.refresh_pre_spawn = True
#c.LocalAuthenticator.create_system_users = True

# #c.Authenticator.auto_login= True
