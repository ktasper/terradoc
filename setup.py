from setuptools import _install_setup_requires, setup

setup(
# The name of the pip package
    name='terradoc',
# The version
    version='0.1.0',
# The python modules to include
    py_modules=['terradoc'],
# Tell setuptools what packages we need installed
    install_requires=[
        "click"
    ],
# Define the entry points to our app or applications
    entry_points='''
        [console_scripts]
        # Tell setuptools to create the following cli executables
        # CLI Exec Name: Py Module: Function Name
        terradoc=terradoc.cli:cli
    ''',
)
