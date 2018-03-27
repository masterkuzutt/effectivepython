import logging
from pprint import pprint
from sys import stdout as STDOUT

def normalize(numbers):
    total = sum(numbers)
    result = []

    for value in numbers:
        percent = 100 * value / total 
        result.append(percent)
    return result 

visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)

path = 'my_numbers.txt'
with open(path, 'w') as f:
    for i in (15, 35, 80):
        f.write('%d\n' % i)

def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line) 

it = read_visits('my_numbers.txt')
percentages = normalize(it)
print(":",percentages)

it = read_visits('my_numbers.txt')
print(list(it))
print(list(it))  # Already exhausted

def normalize_copy(numbers):
    numbers = list(numbers)
    total = sum(numbers)
    result = []
    for value in numbers:
        percent  = 100 * value / total 
        result.append(percent)
    return result


it = read_visits('my_numbers.txt')
percentages = normalize_copy(it)
print(percentages)

def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100 * value / total 
        result.append(percent)
    return result 

percentages = normalize_func(lambda: read_visits(path))

print(percentages)

class ReadVisits (object):
    def __init__(self, data_path):
        super().__init__()
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line  in f:
                yield int(line)


visits = ReadVisits(path)
percentages = normalize(visits)
print(percentages)


class test:
    def __init__(self):
        self.data = 1
    def __iter__(self):
        self.data += 1
        yield self.data


def test2():
    l = [x for x in range(10)]
    for i in l:
        yield i