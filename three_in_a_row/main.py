import os
import re

from three_in_a_row.command import Command
from three_in_a_row.data import OutputData


def add_clearing_before(func):
    # """Add clearing terminal before func call"""
    def wrapped_func(*args, **kwargs):
        os.system("cls" if os.__name__ == "nt" else "clear")
        func(*args, **kwargs)

    return wrapped_func


data = OutputData("Three in a row", 0, 0)

print(data)
cleared_print = add_clearing_before(print)

while (current_command := input("Write command to play: ").upper().strip()) != str(Command.EXIT):
    if current_command == str(Command.START):
        Command.START(data)
    elif current_command == str(Command.LOAD):
        loaded_data = Command.LOAD()
        if loaded_data:
            data = loaded_data
            data.command = "Saved game was successfully load!"
        else:
            data.command = "No save"
    elif current_command.startswith(str(Command.SWAP)):
        xy = re.findall(r"(\([1-5],[1-5]\))", current_command)
        if len(xy) != 2:
            data.command = "Incorrect args for SWAP, you need to write 2 pairs of coordinates, example of command: SWAP (1,2) (1,3)"
        else:
            data = Command.SWAP(data, eval(xy[0]), eval(xy[1]))
    elif current_command == str(Command.SAVE):
        Command.SAVE(data)
        data.command = "Game was successfully saved!"
    elif current_command == str(Command.HELP):
        data = Command.HELP(data)
    else:
        data.command = "Incorrect command!"
    cleared_print(data)
