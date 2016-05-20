#!/bin/sh

docker build -t jb .

docker run --rm --volumes-from upsource jb archive-upsource-backups.py /data/backups/
