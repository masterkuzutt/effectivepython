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

# 大きな内包表記にはジェネレータ式を考える
# 覚えておくこと
#     リスト内包表記は大量の入力に対してメモリを使いすぎるという問題を引き起こす
#     ジェネレータ式はイテレータとして出力を１つずつ生成するのでメモリ問題を回避する
#     ジェネレータ式はジェネレータ式から得られたイテレータを他のfor部分式に渡すことによって組み合わせることができる。
#     ジェネレータ式は連鎖的に組み合わせると非常に速く動く

# Preamble to mimick book environment
import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
import random
with open('my_file.txt', 'w') as f:
    for _ in range(10):
        f.write('a' * random.randint(0, 100))
        f.write('\n')

value = [len(x) for x in open('my_file.txt')]
print(value)


# Example 2
it = (len(x) for x in open('my_file.txt'))
print(it)


# Example 3
print(next(it))
print(next(it))


# Example 4
roots = ((x, x**0.5) for x in it)


# Example 5
print(next(roots))
