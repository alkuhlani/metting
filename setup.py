# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in metting/__init__.py
from metting import __version__ as version

setup(
	name='metting',
	version=version,
	description='met app',
	author='anas',
	author_email='eaayemen@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
