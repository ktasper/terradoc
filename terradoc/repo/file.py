import os
import git

def create_provider_folder(custom_path):
    # TODO: Pass in the custom path with a flag, if set otherwise deafult to ~/.terradoc (do it all on the click flag)
    """
    Creates a config folder to keep all the providers
    """
    # Check whether the specified path exists or not
    is_exist = os.path.exists(os.path.expanduser(custom_path))
    if not is_exist:
        os.makedirs(os.path.expanduser(custom_path))
    return custom_path

def clone_repo(git_url, custom_path):
    """
    Clones the repo
    """
    git.Repo.clone_from(git_url, custom_path)

def init():
    """
    Foo
    """
    pass
