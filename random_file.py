#!/usr/bin/env python

import os, subprocess, random

path = "/mnt/movies"

files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

def get_files(path, subdir):
  for f in os.listdir(os.path.join(path, subdir)):
    if os.path.isfile(os.path.join(path, subdir, f)):
      files.append(os.path.join(subdir, f))
    elif os.path.isdir(os.path.join(path, subdir, f)):
      files + get_files(path, os.path.join(subdir, f))
  return files

for subdir in dirs:
  files + get_files(path, subdir)

filepath = os.path.join(path, random.choice(files))
print filepath

if os.name == 'mac':
  subprocess.call(('open', filepath))
elif os.name == 'nt':
  subprocess.call(('start', filepath), shell=True)
elif os.name == 'posix':
  subprocess.call(('xdg-open', filepath))
