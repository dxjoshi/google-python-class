# The *os* and *os.path* modules include many functions to interact with the file system.
# The *shutil* module can copy files.
#
# os module docs
# filenames = os.listdir(dir) -- list of filenames in that directory path (not including . and ..).
# The filenames are just the names in the directory, not their absolute paths.
# os.path.join(dir, filename) -- given a filename from the above list,
# use this to put the dir and filename together to make a path
# os.path.abspath(path) -- given a path, return an absolute form, e.g. /home/nick/foo/bar.html
# os.path.dirname(path), os.path.basename(path) -- given dir/foo/bar.html,
# return the dirname "dir/foo" and basename "bar.html"
# os.path.exists(path) -- true if it exists
# os.mkdir(dir_path) -- makes one dir, os.makedirs(dir_path) makes all the needed dirs in this path
# shutil.copy(source-path, dest-path) -- copy a file (dest path directories should exist)

import os
import os.path
import shutil

def list_files(dir):
    print('Listing files under \'%s\' dir path' % dir)
    filenames = os.listdir(dir)
    for name in filenames:
        print('File name: %s' % name)
        name = os.path.join(dir, name)
        print('Full path: %s ' % name)
    print('Absolute path: %s' % os.path.abspath(dir))
    print('Directory: %s' % os.path.dirname(dir))
    print('BaseName: %s' % os.path.basename(dir))
    print('Does path exist: %s' % os.path.exists(dir))


os.mkdir('../test')
os.makedirs()


list_files('../tutorials')