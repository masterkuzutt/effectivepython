import logging
from pprint import pprint
from sys import stdout as STDOUT 




chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}

rank_dict = {rank: name for name, rank in chile_ranks.items()}
chile_len_set = { len(name) for name in rank_dict.values() }
print(rank_dict)
print(chile_len_set)