#!/bin/bash

git checkout master
git pull

# Update version in project
PYVAR="__version__ = "
VERSION_STRING=`date -u +0.%Y.%m.%d.%H%M`
FILE_NAME='__init__.py'

# Update piskg version
echo $PYVAR\'$VERSION_STRING\'>'piskg/'$FILE_NAME

# Push to GitHub
git add 'piskg/'$FILE_NAME
git commit -m "RELEASE: Bump version for pypi to "$VERSION_STRING

# Create a tag in repo
TAG_NAME='v'$VERSION_STRING
git tag $TAG_NAME
git push
git push origin $TAG_NAME

# Push to pypi
rm -rf dist; python setup.py sdist bdist_wheel; twine upload dist/*
