#!/usr/bin/env python

from sys import argv, stdout, stderr, exit
from os import listdir
from os.path import isdir, join, getsize, getctime
import time

from plumbum.cmd import tar, rm, mkdir, gunzip
from plumbum import cli, local, TF


srcDir = argv[1]

if len(srcDir) < 5:
    print("Dangerous source directory (too short)", srcDir, "Exiting...", file = stderr)
    exit(1)

# change working directory
local.cwd.chdir(srcDir)

# create dir for archived backup files (if not exists)
archiveDir = "_archived"
mkdir("-p", archiveDir)

for f in listdir(srcDir):
    # just in case
    if f == "" or f == '/': continue
    if isdir(f) and f != archiveDir and f != "_processed":
        # define archive file name
        datePrefix = time.strftime("%Y-%m-%d-", time.localtime(getctime(f)))
        archivedFileName = datePrefix + 'upsource-backup.tar.gz'
        archivePath = join(archiveDir, archivedFileName)

        # try to archive
        tarOk = tar["zcf", archivePath, f] & TF
        # check if archiving completed ok
        if tarOk:
            testOk = gunzip["-t", archivePath] & TF

        # remove processed directory if it's allright
        if tarOk and testOk:
            print("archive ok, removing directory...", f)
            rm("-rf", f)
        else:
            print("ERROR during archiving upsource backup directory:", f, file = stderr)
