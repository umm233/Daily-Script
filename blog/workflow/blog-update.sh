#!/bin/sh

if [ -z "$(git status --porcelain)" ]; then
    echo "nothing to update."
else
    git add .
    git commit -m "triggle by commit ${GITHUB_SHA}" -a
    git push origin master
fi
