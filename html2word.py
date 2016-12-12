# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Create a dictionary which maps word to article id and position of word."""
import argparse
import glob
from HTMLParser import HTMLParser
import sys


class MyHTMLParser(HTMLParser):
  """Html parser for word extraction."""

  def __init__(self):
    HTMLParser.__init__(self)
    self.word2id = {}
    self.article_id = None
    self.word_pos = None

  def handle_starttag(self, tag, attrs):
    if tag == 'doc':
      self.article_id = attrs[0][1]
      self.word_pos = 0

  def handle_data(self, data):
    l = data.strip().split()
    for word in l:
      w = word.strip("\'\",.():?!-`;")
      if w and w not in self.word2id:
        self.word2id[w] = (self.article_id, self.word_pos)
      self.word_pos += 1


def main():
  arg_parser = argparse.ArgumentParser()
  arg_parser.add_argument('html_file', help='the html filenames as input',
                          type=str)
  arg_parser.add_argument('dict_file', help='the dict filename as output',
                          type=str)
  args = arg_parser.parse_args()

  # Parse the html files that contain all the texts
  html_parser = MyHTMLParser()
  # Wants to make sure the input files are in the same order
  text_htmls = sorted(glob.glob(args.html_file))

  if not text_htmls:
    print 'No input html files found'
    sys.exit(1)

  for text_html in text_htmls:
    print 'processing %s' % text_html
    s = open(text_html)
    for sl in s:
      html_parser.feed(sl)

  with open(args.dict_file, 'w') as out_dict:
    for k in html_parser.word2id:
      out_dict.write(
          '%s\t%s\t%s\n'%(k, html_parser.word2id[k][0],
                          html_parser.word2id[k][1]))


if __name__ == '__main__':
  main()
