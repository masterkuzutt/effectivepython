import logging
from pprint import pprint
from sys import stdout as STDOUT

# try:
#     def determin_weight(volume, density):
#         if density <= 0 :
#             raise ValueError('Density must be positive')
#     determin_weight(1, 0)
# except :
#     logging.exception('Expected')
# else:
#     assert False


class Error(Exception):
    pass

class InvalidDensityError(Error):
    pass

class my_module(object):
    Error = Error
    InvalidDensityError = InvalidDensityError

    @staticmethod
    def determin_weight(volume, density):
        if density <= 0 :
            raise InvalidDensityError('Density must be positive')

try:
    weight = my_module.determin_weight(1, -1)
    assert False

except my_module.InvalidDensityError:
    weight = 0
except my_module.Error as e:
    logging.error('Bug in the calling code: %s', e)




