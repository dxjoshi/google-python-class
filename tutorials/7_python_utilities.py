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
import sys
import time
import urllib.request
import subprocess

# The *commands* module is a simple way to run an external command and capture its output.
#
# (status, output) = commands.getstatusoutput(cmd) -- runs the command, waits for it to exit,
# and returns its status int and output text as a tuple. The command is run with its standard output
# and standard error combined into the one output text. The status will be non-zero if the command failed.
# Since the standard-err of the command is captured, if it fails,
# we need to print some indication of what happened.
# output = commands.getoutput(cmd) -- as above, but without the status int.
# There is a commands.getstatus() but it does something else, so don't use it --
# dumbest bit of method naming ever!
# If you want more control over the running of the sub-process, see the "popen2" module
# There is also a simple os.system(cmd) which runs the command and dumps its output onto your output
# and returns its error code. This works if you want to run the command
# but do not need to capture its output into your python data structures.
# Note: The commands module and the popen2 module are deprecated as of Python 2.6 and removed in 3.x.
# The subprocess module replaces these modules. In particular, the subprocess module discusses
# replacements for these modules in the subprocess-replacements section.

## Given a dir path, run an external 'ls -l' on it --
## shows how to call an external program
def listdir(dir):
  cmd = 'ls -l ' + dir
  print("Command to run:", cmd)   ## good to debug cmd before actually running it
  (status, output) = subprocess.getstatusoutput(cmd)
  if status:    ## Error case, print the command's output to stderr and exit
    sys.stderr.write(output)
    sys.exit(status)
  print(output)  ## Otherwise do something with the command's output


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


def copy(src_path, dest_path):
    print('Copying %s to %s' % (src_path, dest_path))
    if not os.path.exists(dest_path):
        dest_path = '../%s' % dest_path
        os.mkdir(dest_path)
        shutil.copy(src_path, os.path.abspath(dest_path))

def delete_dir(dest_path):
    # time.sleep(5)
    print('Deleting "%s" dir and all its contents' % dest_path)
    shutil.rmtree(dest_path, ignore_errors=True)

list_files('../tutorials')
src_path = '../tutorials/1_intro.py'
dest_path = 'test'
copy(src_path, dest_path)
dest_path = '../test'
delete_dir(dest_path)
# listdir(dest_path)

def exception_handling():
    try:
        ## Either of these two lines could throw an IOError, say
        ## if the file does not exist or the read() encounters a low level error.
        filename = 'incorrect_file.txt'
        f = open(filename, 'rU')
        text = f.read()
        f.close()
    except IOError:
        ## Control jumps directly to here if any of the above lines throws IOError.
        sys.stderr.write('problem reading:' + filename)
    ## In any case, the code then continues with the line after the try/except


# HTTP -- urllib and urlparse
# The module *urllib* provides url fetching -- making a url look like a file you can read from.
# The *urlparse* module can take apart and put together urls.
#
# urllib module docs
# ufile = urllib.urlopen(url) -- returns a file like object for that url
# text = ufile.read() -- can read from it, like a file (readlines() etc. also work)
# info = ufile.info() -- the meta info for that request. info.gettype() is the mime type, e.g. 'text/html'
# baseurl = ufile.geturl() -- gets the "base" url for the request,
# which may be different from the original because of redirects
# urllib.urlretrieve(url, filename) -- downloads the url data to the given file path
# urlparse.urljoin(baseurl, url) -- given a url that may or may not be full,
# and the baseurl of the page it comes from, return a full url. Use geturl() above to provide the base url.
def http_utils(url):
    response = urllib.request(url)
    text = response.read()

## Given a url, try to retrieve it. If it's text/html,
## print its base url and its text.
def wget(url):
  ufile = urllib.urlopen(url)  ## get file-like object for url
  info = ufile.info()   ## meta-info about the url content
  if info.gettype() == 'text/html':
    print('base url:' + ufile.geturl())
    text = ufile.read()  ## read all its text
    print(text)

## Version that uses try/except to print an error message if the
## urlopen() fails.
def wget2(url):
  try:
    ufile = urllib.urlopen(url)
    if ufile.info().gettype() == 'text/html':
      print(ufile.read())
  except IOError:
    print('problem reading url:', url)

