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

# イテレータを並列に処理するにはzipを使う
# 覚えておくこと
    # 組み込み関数zipが複数のイテレータを並列に処理するのに使える
    # python３ではzipはタプルを生成する遅延評価ジェネレータである。python２ではzipはすべての結果をタプルのリストとして返す
    # 異なる長さのイテレータを与えるとzipはなにもいわずに出力を最短で止める
    # 組み込みモジュールintetoolsのzip_longest関数が複数のイテレータの長さが異なるときに使える。

# Preamble to mimick book environment
import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]
print(letters)


# Example 2
longest_name = None
max_letters = 0

for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count

print(longest_name)


# Example 3
longest_name = None
max_letters = 0
for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = name
        max_letters = count
print(longest_name)


# Example 4
longest_name = None
max_letters = 0
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count
print(longest_name)


# Example 5
names.append('Rosalind')
for name, count in zip(names, letters):
    print(name)
