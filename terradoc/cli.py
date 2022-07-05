"""
Sets up the CLI
"""
import os
import click
from .file import clone_provider, pull_provider

class Config(): # pylint: disable=too-few-public-methods
    """
    Create a helper class to allow us to pass top level config
    (Verbose Mode, Other Settings down into our other functions (sub commands)
    """
    def __init__(self):
        self.verbose = False

pass_config = click.make_pass_decorator(Config, ensure=True)

terradoc_dir = os.path.expanduser("~/.terradoc")
@click.group()
@click.option("--verbose", "-v", help="enable versbose output", is_flag=True)
@click.option("--debug", "-d", help="enable debug mode to aid in development", is_flag=True)
@pass_config
def cli(config, verbose, debug):
    """
    Assign the click options to the top level cli
    """
    config.verbose = verbose
    config.debug = debug

@cli.command()
@click.argument('provider', type=click.Choice(['aws','gcp', 'terradoc'], case_sensitive=False), required=True)
@click.option("--force", "-f", help="Force re-init of terradoc provider", is_flag=True)
@pass_config
def init(config, provider, force) :
    """
    A cli command, inits the git repo so we can run other
    fuctions on it
    """
    clone_provider(provider, terradoc_dir, config, force)

@cli.command()
@click.argument('provider', type=click.Choice(['aws','gcp','terradoc'], case_sensitive=False), required=True)
@pass_config
def update_provider(config, provider) :
    """
    A cli command, updates the git repo
    """
    pull_provider(provider, terradoc_dir, config)





# @cli.command()
# @click.argument('search-string', required=True)
# @pass_config
# def search(config, search_string) :
#     """
#     A cli command, will search for a terraform doc
#     """
#     if config.debug:
#         debug_var("Search String", search_string)


# @cli.command()
# @click.argument('output-file', type=click.File('w'), default='terradoc.md', required=False)
# # Pass our config from the helper function
# @pass_config
# # Set up the logic
# def save(config, output_file) :
#     # Add a docstring for help info
#     """
#     A cli command, will save a found terraform doc to the system
#     """
#     if config.verbose:
#         click.echo("Verbose")
#     click.echo("Hello", file=output_file)
