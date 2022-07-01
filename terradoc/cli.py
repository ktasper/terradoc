"""
Sets up the CLI
"""
import click
from .helpers.outputs import debug_var

class Config(): # pylint: disable=too-few-public-methods
    """
    Create a helper class to allow us to pass top level config
    (Verbose Mode, Other Settings down into our other functions (sub commands)
    """
    def __init__(self):
        self.verbose = False

# Create a decorator we can use to pass our config down
pass_config = click.make_pass_decorator(Config, ensure=True)

# Init the cli group (root command and sub commands)
@click.group()
# Flags by default are disabled
@click.option("--verbose", "-v", help="enable versbose output", is_flag=True)
@click.option("--debug", "-d", help="enable debug mode to aid in development", is_flag=True)
# Pass our config from the helper function
@pass_config
def cli(config, verbose, debug):
    """
    Assign the click options to the top level cli
    """
    config.verbose = verbose
    config.debug = debug

@cli.command()
# Pass our config from the helper function
@click.argument('provider', type=click.Choice(['aws','gcp'], case_sensitive=False), required=True)
@pass_config
# Set up the logic
def init(config, provider) :
    # Add a docstring for help info
    """
    A cli command, inits the git repo so we can run other
    fuctions on it
    """
    if config.debug:
        debug_var("Terraform provider", provider)
        click.echo(f"TODO: Downloading provider repo for {provider}")
    clone_provider(provider, custom_path)











@cli.command()
# Pass our config from the helper function
@click.argument('search-string', required=True)
@pass_config
# Set up the logic
def search(config, search_string) :
    # Add a docstring for help info
    """
    A cli command, will search for a terraform doc
    """
    if config.debug:
        debug_var("Search String", search_string)


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
