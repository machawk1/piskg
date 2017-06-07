#!/usr/bin/env python

from setuptools import setup
from piskg import __version__

long_description = open('README.rst').read()
desc = """Python IPFS Swarm Key Generator"""

setup(
    name='piskg',
    version=__version__,
    url='https://github.com/machawk1/piskg',
    download_url="https://github.com/machawk1/piskg",
    author='Mat Kelly',
    author_email='mkelly@cs.odu.edu',
    description=desc,
    packages=['piskg'],
    license='MIT',
    long_description=long_description,
    provides=[
        'piskg'
    ],
    entry_points="""
        [console_scripts]
        piskg = piskg.__main__:main
    """,
    package_data={},
    keywords='ipfs keygen',
    classifiers=[
        'Topic :: Utilities',
    ]
)

# Publish to pypi: rm -rf dist; python setup.py sdist bdist_wheel; twine upload dist/*
