#!/bin/bash

DEPLOY="../pianomanfrazier.github.io"
DATE=$(date)
# set the path of the hugo executable
# for now use Hugo v0.46
HUGO="./hugo"

echo "building site"
rm -r public/*
$HUGO

echo "cleaning out old site"
for i in about categories post tags *.html *.png *.xml
do
	rm -r $DEPLOY/$i
done

echo "copying build to $DEPLOY"
cp -r public/* $DEPLOY

cd $DEPLOY
git add -A
git commit -m "new build on $DATE" 
git push
