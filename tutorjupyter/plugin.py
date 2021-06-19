from glob import glob
import os
import pkg_resources

from .__about__ import __version__

templates = pkg_resources.resource_filename(
    "tutorjupyter", "templates"
)

config = {
     "add": {
        "SECRET_KEY": "{{ 24|random_string }}"
      },
      
      "defaults": {
        "HOST": "{{ LMS_HOST }}:8000",
        "DOCKER_REGISTRY": "{{ DOCKER_REGISTRY }}",
        "DOCKER_IMAGE": "muratp/jupyter"
        
    }   
      
}

hooks = {       
  
      "build-image": {"jupyter": "muratp/jupyter"},
      "remote-image": {"jupyter": "muratp/jupyter"},
      "init": ["lms","jupyter"]  

}


def patches():
    all_patches = {}
    patches_dir = pkg_resources.resource_filename(
        "tutorjupyter", "patches"
    )
    for path in glob(os.path.join(patches_dir, "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches
