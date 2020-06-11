try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'My Project',
    'autor' : 'My Name',
    'url' : 'URL to get it at',
    'download_url' : 'Where to download',
    'author_email' : 'My email',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'package' : ['NAME'],
    'sctipt' : [],
    'name' : 'projectname'
}

setup(**config)