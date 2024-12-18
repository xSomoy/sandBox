#!/bin/bash
git fetch origin master
git pull origin master
git add .
msg=$(date -R)
git commit -m "$msg"
git push origin master

#Perfecto
