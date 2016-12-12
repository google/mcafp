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

"""Convert text id and word id to texts."""
# -*- coding: utf-8 -*-
import argparse


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('dict_file', help='the dict filename as input',
                      type=str)
  parser.add_argument('id_kv_file', help='the id kv filename as input',
                      type=str)
  parser.add_argument('text_kv_file', help='the text kv filename as output',
                      type=str)
  args = parser.parse_args()

  print 'Prepare the dict'
  id2word = {}
  dict_file = open(args.dict_file)
  for l in dict_file:
    ll = l.split('\t')
    id2word['(%s+%s)' % (ll[1].strip(), ll[2].strip())] = ll[0].strip()

  print 'Processing kv'
  id_kv = open(args.id_kv_file)
  text_kv = open(args.text_kv_file, 'w')

  for sl in id_kv:
    kvs = sl.strip().split('\t')
    out_kvs = ''
    for kv in kvs:
      kv_sp = kv.split('=')
      if len(kv_sp) > 2:
        for s in kv_sp[2:]:
          kv_sp[1] += '=' + s
      if (kv_sp[0].startswith('answer') and
          not kv_sp[0].endswith('score')) or kv_sp[0] == 'background':
        sentence = ''
        word_ids = kv_sp[1].split()
        for w in word_ids:
          if w in id2word:
            sentence += id2word[w] + ' '
          else:
            if w == '@-@':
              sentence += '- '
            else:
              sentence += w + ' '

        if kv_sp[0] == 'background':
          out_kvs += '%s=%s\t'%(kv_sp[0], sentence)
        else:
          out_kvs += '%s=%s\t'%(kv_sp[0], sentence.strip())
      else:
        out_kvs += '%s\t'%(kv)

    text_kv.write('%s\n'%(out_kvs.strip()))


if __name__ == '__main__':
  main()
