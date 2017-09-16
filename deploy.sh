#!/bin/bash

DEPLOY="../pianomanfrazier.github.io"
DATE=$(date)

echo "building site"
rm -r public/*
hugo

echo "copying build to $DEPLOY"
cp -r public/* $DEPLOY

cd $DEPLOY
git add -A
git commit -m "new build on $DATE" 
git push
