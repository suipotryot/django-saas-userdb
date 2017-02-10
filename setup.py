from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'django-saas-userdb',
    packages = ['userdb'],
    version = __import__('userdb').__version__,
    description = 'A lightweight application to use Django as SaaS (Software as a Service). It separates users databases for the same Django instance.',
    long_description = long_description,
    author = 'Guillaume D',
    author_email = 'guillaume1.dubus@gmail.com',
    license = 'MIT',
    url = 'https://github.com/suipotryot/django-saas-userdb',
    download_url = 'https://github.com/suipotryot/django-saas-userdb/tarball/0.1',
    keywords = ['django', 'saas', 'user', 'database'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
