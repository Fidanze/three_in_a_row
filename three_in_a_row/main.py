import os
from crystal import Crystal
import random
import time

def add_clearing_before(func):
    '''Add clearing terminal before func call'''
    def wrapped_func(*args, **kwargs):
        os.system('cls' if os.name=='nt' else 'clear')
        func(*args, **kwargs)
    return  wrapped_func

cleared_print = add_clearing_before(print)
for i in range(10**5):
    a = random.choice(list(Crystal))
    cleared_print(str(a))
    time.sleep(0.05)