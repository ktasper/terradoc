"""
This module deals with everything relating to the file system
"""
import os
import sys
import shutil
import git
from .helpers.outputs import debug_var

git_urls = {
    "gcp": "https://github.com/hashicorp/terraform-provider-google.git",
    "aws": "https://github.com/hashicorp/terraform-provider-aws.git"
    }

def create_provider_folder(terradoc_dir):
    """
    Creates a config folder to keep all the providers
    """
    # Check whether the specified path exists or not
    is_exist = os.path.exists(os.path.expanduser(terradoc_dir))
    if not is_exist:
        os.makedirs(os.path.expanduser(terradoc_dir))
    return terradoc_dir

def clone_provider(provider, terradoc_dir, config, force):
    """
    Foo
    """
    # Set the terradoc_dir using the provider
    path = f"{terradoc_dir}/{provider}"

    if force:
        if config.debug:
            debug_var("Force re-init:", force)
        is_exist = os.path.exists(os.path.expanduser(path))
        if is_exist:
            shutil.rmtree(os.path.expanduser(path))

    if is_git_repo(path) and force is False:
        print (f"{path} already exists")
        sys.exit(5)

    # Now we can clone down the provider
    if config.debug:
        debug_var("clone_provider: Provider ", provider)
    if config.debug:
        debug_var("Creating: ", path)

    create_provider_folder(path)

    if config.debug:
        debug_var("Cloning repo: ", git_urls[provider])

    git.Repo.clone_from(git_urls[provider], f"{terradoc_dir}/{provider}")

    if config.debug:
        debug_var("Repo cloned: ", f"{terradoc_dir}/{provider}")

def pull_provider(provider, terradoc_dir, config):
    """
    Git pulls the provider git repo
    """
    terradoc_dir = f"{terradoc_dir}/{provider}/"
    if config.debug:
        debug_var("Provider ", provider)
        debug_var("Provider path ", terradoc_dir)
    #TODO: Pull the repo so its up to date


def is_git_repo(path):
    """
    Check to see if dir is a git repo
    """
    try:
        _ = git.Repo(path).git_dir
        return True
    except git.exc.InvalidGitRepositoryError:
        return False
    except git.exc.NoSuchPathError:
        return False