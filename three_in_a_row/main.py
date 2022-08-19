import os
from three_in_a_row.cli import CLI

from three_in_a_row.command import Command
from three_in_a_row.data import OutputData


def add_clearing_before(func):
    # """Add clearing terminal before func call"""
    def wrapped_func(*args, **kwargs):
        os.system("cls" if os.name == "nt" else "clear")
        func(*args, **kwargs)

    return wrapped_func


cleared_print = add_clearing_before(print)
data = OutputData("Three in a row", 0, 0)
CLI.add(data)
cleared_print(data)

while True:
    current_command = input("Write command to play: ").upper().strip()
    if current_command == Command.START:
        data.command = Command.START(data)
    elif current_command == Command.EXIT:
        data.command = Command.EXIT(data)
        break
    elif current_command == Command.LOAD:
        data.command = Command.LOAD(data)
    elif current_command == Command.SWAP:
        data.command = Command.SWAP(data)
    elif current_command == Command.SAVE:
        data.command = Command.SAVE(data)
    elif current_command == Command.HELP:
        data.command = Command.HELP(data)
    else:
        data.command = "Incorrect command!"
