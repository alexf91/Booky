#!/usr/bin/env python

from setuptools import setup

setup(name='booky',
    version='0.1',
    description='Manage bookmarks for directories on the command line',
    author='Alexander Fasching',
    author_email='fasching.a91@gmail.com',
    maintainer='Alexander Fasching',
    maintainer_email='fasching.a91@gmail.com',
    url='https://github.com/alexf91/booky',
    license='GPL',
    packages=['booky'],
    entry_points={
        'console_scripts': ['booky = booky.__main__:main']
    },
    install_requires=[
    ],
)
