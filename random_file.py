#!/usr/bin/env python

import os, subprocess, random

path = "/mnt/movies/"
filepath = path + random.choice(os.listdir(path))

if os.name == 'mac':
    subprocess.call(('open', filepath))
elif os.name == 'nt':
    subprocess.call(('start', filepath), shell=True)
elif os.name == 'posix':
    subprocess.call(('xdg-open', filepath))
