import logging
from pprint import pprint
from sys import stdout as STDOUT


from threading import Lock
lock = Lock()
with lock:
    print('Lock is held')


lock.acquire()
try:
    print('lock is held')
finally:
    lock.release()


import logging 
logging.getLogger().setLevel(logging.WARNING)
def my_function():
    logging.debug("Some debug data")
    logging.debug("Error log here")
    logging.debug("More debug data")


my_function()