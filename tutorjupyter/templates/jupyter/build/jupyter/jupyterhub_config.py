
c.LocalAuthenticator.create_system_users = True
c.Spawner.args = ['--NotebookApp.tornado_settings={"headers":{"Content-Security-Policy": "frame-ancestors * jupyter:8000"}}']   

c.JupyterHub.tornado_settings = { 'headers': { 'Content-Security-Policy': "frame-ancestors * jupyter:8000"} }