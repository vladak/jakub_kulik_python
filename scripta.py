#!/usr/bin/env python

import os
from pathlib import Path
from shutil import copy

tmp_file = '/tmp/some_file.txt'
Path(tmp_file).touch()
nonexistent_dir = 'not_a_dir/'
assert not os.path.exists(nonexistent_dir)
copy(tmp_file, nonexistent_dir)
