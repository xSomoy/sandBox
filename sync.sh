#!/bin/bash
git add .
msg=$(date -R)
git commit -m "$msg"
git push origin master

# Perfecto