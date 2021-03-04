#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess
import zipfile

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def zipdir(path, ziph):
  # ziph is zipfile handle
  print('Selecting files in [%s] to zip' % path)
  for root, dirs, files in os.walk(path):
    for file in files:
      if re.search(r'__[\w]+__', file):
        print(os.path.join(root, file))
        print(os.path.relpath(os.path.join(root, file), os.path.join(path, '..')))
        ziph.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(path, '..')))


def list_file(dir):
  list_of_files = []
  print('Finding special files in %s' % dir)
  filenames = os.listdir(dir)
  for filename in filenames:
    if re.search(r'__[\w]+__', filename):
      list_of_files.append(os.path.join(dir, filename))
  return list_of_files


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    print(todir)
    dest_path = '../%s' % todir
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)

    fromdir = args[2]
    for filename in list_file(fromdir):
      print(filename)
      shutil.copy(filename, os.path.abspath(dest_path))
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    fromdir = args[2]
    zipf = zipfile.ZipFile(tozip, 'w', zipfile.ZIP_DEFLATED)
    zipdir(fromdir+'/', zipf)
    zipf.close()
    # cmd = 'zip -j %s %s' % ( tozip, ' '.join(list_file(fromdir)))
    # print(cmd)
    # subprocess.run(["ls", "-l"], shell=True)
    # shutil.make_archive(tozip, 'zip', )
    del args[0:2]

  if tozip == '' and todir == '':
    # print(args)
    dir = args[0]
    for filename in list_file(dir):
      print(os.path.abspath(filename))

  if len(args) == 0:
    print("error: must specify one or more dirs")
    sys.exit(1)

  # +++your code here+++
  # Call your functions

if __name__ == "__main__":
  main()
