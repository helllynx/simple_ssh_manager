from enum import Enum


# class Commands:
#     def __init__(self):
#         self.COMMANDS = Enum('Command', ['LIST', 'ADD', 'DELETE', 'CONNECT', 'EXIT'], start=0)
#         self._localized_commands = locale_manager.get_localized_commands()
#         self.commands =
from app import locale_manager


class Commands(Enum):
    LIST = 'list'
    ADD = 'add'
    DELETE = 'delete'
    CONNECT = 'connect'
    EXIT = 'exit'

    def __init__(self, f):
        self
        pass

    def get_localized_descriptions_list(self, id: int):
        return [cmd for cmd in locale_manager.get_localized_commands()]

Commands(1)

def get_all_commands():
    return [command.description for command in COMMANDS]


def get_short_names():
    return [command.short_command for command in COMMANDS]


def print_all_commands():
    for i, cn in enumerate(get_all_commands()):
        print(f'{i}. {cn}')


def get_func_by_id(id: int):
    return list(filter(lambda obj: obj.id == id, COMMANDS))


# def run_command(command_id: int):
#     if command_id == COMMANDS.:
#         print_all_saved_ssh()
#     elif command_id == COMMANDS.:
#         ask_info_for_new_ssh_entry()
#     elif command_id == COMMANDS.:
#         delete_ssh_entry()
#     elif command_id == COMMANDS.:
#         print(locale_manager.get_localized_string('choose_ssh'))
#         print_all_saved_ssh()
#         ask_and_open_new_connection()
#     elif command_id == COMMANDS.:
#         return COMMANDS.EXIT


print(COMMANDS)
