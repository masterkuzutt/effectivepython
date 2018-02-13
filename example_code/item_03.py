#!/usr/bin/env python3

# Copyright 2014 Brett Slatkin, Pearson Education Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# 覚えておくこと
# python3ではbytesは8ビット値の列を含みstrはunicode文字列を含む。bytesとstrとのインスタンスは（<や⁺のような）演算子で一緒に使うことができない
# python2ではstrは8ビット値の列だけを含みUnicodeはUnicode文字列を含む。strとUnicodeとはstrが7ビットASCII文字だけを含むなら演算で一緒に扱うことができる。
# ヘルパー関数を使って操作する入力が期待している（8ビット値、UTF-8符号化文字、Unicode文字など）文字列型になっていることを確かめる。
# ファイルにバイナリデータを読み書きするには常に（'rb'または'wb'のような）バイナリモードでオープンする


# Preamble to mimick book environment
import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of str

print(repr(to_str(b'foo')))
print(repr(to_str('foo')))


# Example 2
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of bytes

print(repr(to_bytes(b'foo')))
print(repr(to_bytes('foo')))


# Example 5
try:
    import os
    with open('random.bin', 'w') as f:
        f.write(os.urandom(10))
except:
    logging.exception('Expected')
else:
    assert False


# Example 6
with open('random.bin', 'wb') as f:
    f.write(os.urandom(10))
