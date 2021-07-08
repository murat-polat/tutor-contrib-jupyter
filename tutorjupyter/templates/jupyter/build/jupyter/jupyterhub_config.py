
c.Spawner.args = ['--NotebookApp.tornado_settings={"headers":{"Content-Security-Policy": "frame-ancestors * jupyter:8000"}}']   

c.JupyterHub.tornado_settings = { 'headers': { 'Content-Security-Policy': "frame-ancestors * jupyter:8000"} }

## Users
c.Authenticator.whitelist = {'student', 'teacher'}
## Admins
c.Authenticator.admin_users = {'teacher'}
## Admins can create/delete users
c.LocalAuthenticator.create_system_users=True
