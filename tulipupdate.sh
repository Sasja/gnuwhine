#!/usr/bin/env bash

tulippath=$1

cd "$tulippath"
./purpletulip.py > ./recipe.yaml
git add recipe.yaml
git commit -m "auto-update recipe"
git push
