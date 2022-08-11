import enum
from termcolor import colored

class Crystal(enum.Enum):
    # '''Enum for kind of crystals'''
    STAR = {'symbol':'*', 'color':'yellow'}
    PLUS = {'symbol':'+', 'color':'blue'}
    DOLLAR = {'symbol':'$', 'color':'green'}
    CROSS = {'symbol':'X', 'color':'red'}

    def __init__(self, vals):
        self.symbol = vals['symbol']
        self.color = vals['color']
        
    def __str__(self):
        return  colored(f'{self.name}: {self.value["symbol"]}', self.value['color'])