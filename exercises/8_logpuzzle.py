#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib.request
import os
import errno



"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  # print(filename)
  server = re.match(r'[\S.]+_([\S.]+)', filename).group(1)
  # print(server)
  file = open(filename, 'r')
  slices = ['http://%s%s' % (server, url[0]) for url in sorted(re.findall(r'.*GET\s([\w\S]+puzzle[\w\S]+)\s(HTTP[\d\S.]+)', file.read()))]
  # for url in slices:
  #   print(url)
  return slices
  # slices = sorted(re.findall(r'.*GET\s([\w\S]+puzzle[\w\S]+)\s(HTTP[\d\S.]+)', file.read()))
  # for url in slices:
  #   print('http://%s%s' % (server, url[0]))


def func(item):
  # print(item)
  # print(re.match(r'[\S.]+-([\S.]+)', item).group(1))
  return re.match(r'[\S.]+-([\S.]+)', item).group(1)


def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++

  img_tags = []
  if not os.path.exists(os.path.dirname(dest_dir)):
    try:
      os.makedirs(os.path.dirname(dest_dir))
    except OSError as exc:  # Guard against race condition
      if exc.errno != errno.EEXIST:
        raise
  img_urls = sorted(img_urls, key=func)
  for i in range(len(img_urls)):
     print(img_urls[i])
     filename = dest_dir + '/img%s' % i
     img_tags.append('<img src="%s">' % filename)
     print('Fetching image slice from [%s] to file "%s" ' % (img_urls[i], filename))
     urllib.request.urlretrieve(img_urls[i], filename)

  index_data = []
  index_data.append('<verbatim>\n<html>\n<body>')
  index_data.append(''.join(img_tags))
  index_data.append('\n</body>\n</html>')
  filename = dest_dir + '/index.html'
  print('Writing img data into %s' % filename)
  with open(filename, 'w') as f:
    for line in index_data:
      f.write(line)

  # print(name)
  

def main():
  args = sys.argv[1:]

  if not args:
    print('usage: [--todir dir] logfile ')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print('no to dir')
    #  print('\n'.join(img_urls))

if __name__ == '__main__':
  main()
