try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'The LOST Game',
    'author': 'Tim Kuhr',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'tim@kuhr.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'lost_game.py'
}

setup(**config)
