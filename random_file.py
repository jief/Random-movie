#!/usr/bin/env python

import os, subprocess, random

path = "/mnt/movies/"

# TODO use a recursive function
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

for subdir in dirs:
	for f in os.listdir(os.path.join(path, subdir)):
		if os.path.isfile(os.path.join(path, subdir, f)):
			files.append(os.path.join(subdir, f))

filepath = os.path.join(path, random.choice(files))

if os.name == 'mac':
    subprocess.call(('open', filepath))
elif os.name == 'nt':
    subprocess.call(('start', filepath), shell=True)
elif os.name == 'posix':
    subprocess.call(('xdg-open', filepath))