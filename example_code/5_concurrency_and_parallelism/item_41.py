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
# 本当の並列性のためにconcurrent.futuresを考える
# 覚えておくこと
# CPUボトルネック部分をC拡張モジュールに移すのはpythonコードへの投資を最大化しながら性能を改善する効率的な方法だ。しかしこれは高価なだけでなくバグを作りかねない。
# mulitiprocessingモジュールはある種のpython計算を最小限の努力で並列化する強力なツールを提供する
# multiprocessingの能力は組み込みモジュールconcurrent.futuresとその単純なProcessPoolExecutorクラスで活かすのが一番良い。
# mulitiprocessingモジュールの高度な機能の部分はあまりに複雑なので避けたほうがよい。


# Preamble to mimick book environment
import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


# Example 2
from time import time
numbers = [(1963309, 2265973), (2030677, 3814172),
           (1551645, 2229620), (2039045, 2020802)]
start = time()
results = list(map(gcd, numbers))
end = time()
print('Took %.3f seconds' % (end - start))


# Example 3
from concurrent.futures import ThreadPoolExecutor

start = time()
pool = ThreadPoolExecutor(max_workers=2)
results = list(pool.map(gcd, numbers))
end = time()
print('Took %.3f seconds' % (end - start))


# Example 4
from concurrent.futures import ProcessPoolExecutor

start = time()
pool = ProcessPoolExecutor(max_workers=2)  # The one change
results = list(pool.map(gcd, numbers))
end = time()
print('Took %.3f seconds' % (end - start))
