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

# クラス属性をメタクラスで注釈する
# どの項だったかはっきりしないが、ディスクリプタの例でweakrefを使っていた例よりも
# インスタンスごとの値の保存は簡単に見える。

# 覚えておくこと
# メタクラスはクラスが完全に定義される前にクラス属性を修正することを可能にする
# →よくわからない
# ディスクリプタとメタクラスとは宣言的なふるまいと実行時イントロスペクションのための強力なコンビだ
# メタクラスをディスクリプタと一緒に使うことでメモリリークとweakrefモジュールの両方を避けることができる
# →最初にいえや

# Preamble to mimick book environment
import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
class Field(object):
    def __init__(self, name):
        self.name = name
        self.internal_name = '_' + self.name

    def __get__(self, instance, instance_type):
        if instance is None: return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


# Example 2
class Customer(object):
    # Class attributes
    first_name = Field('first_name')
    last_name = Field('last_name')
    prefix = Field('prefix')
    suffix = Field('suffix')


# Example 3
foo = Customer()
print('Before:', repr(foo.first_name), foo.__dict__)
foo.first_name = 'Euclid'
print('After: ', repr(foo.first_name), foo.__dict__)


# Example 4
class Meta(type):
    def __new__(meta, name, bases, class_dict):
        # keyにfirst_nameが入って、valueにField()が格納される感じ？ 
        for key, value in class_dict.items():
            if isinstance(value, Field):
                value.name = key
                value.internal_name = '_' + key
        # これの意味が分からない
        cls = type.__new__(meta, name, bases, class_dict)
        return cls


# Example 5
class DatabaseRow(object, metaclass=Meta):
    pass


# Example 6
class Field(object):
    def __init__(self):
        # These will be assigned by the metaclass.
        self.name = None
        self.internal_name = None
    def __get__(self, instance, instance_type):
        if instance is None: return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


# Example 7
class BetterCustomer(DatabaseRow):
    first_name = Field()
    last_name = Field()
    prefix = Field()
    suffix = Field()


# Example 8
foo = BetterCustomer()
print('Before:', repr(foo.first_name), foo.__dict__)
foo.first_name = 'Euler'
print('After: ', repr(foo.first_name), foo.__dict__)
