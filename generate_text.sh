#!/bin/sh

# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

LDCDIR=""   # Path to input LDC dataset directory (LDC2011T07)
OUTDIR=""   # Path to output directory

HTML="LDC2011T07/gigaword_eng_5_d1/data/afp_eng/afp_eng_*"
DICT="afp_dict.txt"
MCAFPDIR="./data"

set -eu

if [ ! "${LDCDIR}" ]; then
  echo "Please set the LDCDIR variable to point to the location of the LDC dataset top directory (contact LDC to obtain a copy)"
  exit 1
fi
if [ ! "${MCAFPDIR}" ]; then
  echo "Please set the MCAFPDIR variable to point to the location of the MCAFP dataset directory (where you downloaded the data)"
  exit 1
fi
if [ ! "${OUTDIR}" ]; then
  echo "Please set the OUTDIR variable to point to the desired output location"
  exit 1
fi

DICTDIR="${OUTDIR}/tmp"
mkdir -p "${DICTDIR}"

if [ -e "${DICTDIR}/${DICT}" ]; then
  echo "Using existing dict: ${DICTDIR}/${DICT}"
else
  echo "Generate dict: ${DICTDIR}/${DICT}"
  python html2word_release.py "${LDCDIR}/${HTML}" "${DICTDIR}/${DICT}"
fi

for FNAME in "test" "dev" "train"; do
  IDKV="${FNAME}.mc5.kv"
  if [ ! -e "${MCAFPDIR}/${IDKV}" ]; then
    echo "Missing MC-AFP ${MCAFPDIR}/${IDKV} input file"
    exit 1
  fi
  TEXTKV="${FNAME}.mc5-text.kv"
  echo "Generate ${TEXTKV}"
  python id2text_release.py "${DICTDIR}/${DICT}" "${MCAFPDIR}/${IDKV}" "${OUTDIR}/${TEXTKV}"
done

echo "Done, see the .kv files in ${OUTDIR}"


