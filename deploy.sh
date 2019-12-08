#!/bin/sh

# If a command fails then the deploy stops
set -e

printf "Converting notebooks to markdown...\033[0m\n"

python from_notebook_to_post.py

printf "\033[0;32mDeploying updates to GitHub...\033[0m\n"

hugo

git add .

msg="Deploy em $(date)"
if [ -n "$*" ]; then
	msg="$*"
fi
git commit -m "$msg"

git push --force-with-lease origin master
