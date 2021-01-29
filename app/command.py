from enum import Enum

from app import locale_manager
from app.storage import ask_info_for_new_ssh_entry, print_all_saved_ssh, ask_and_open_new_connection


class Command(Enum):
    LIST = 0
    ADD = 1
    CONNECT = 2
    EXIT = 3

    @staticmethod
    def get_all_commands():
        return [name.name for name in Command]

    @staticmethod
    def print_all_commands():
        for i, cn in enumerate(Command.get_all_commands()):
            print(f'{i}. {cn}')

    @staticmethod
    def get_func_by_id(id: int):
        return Command.get_all_commands()[id]


def run_command(command_id: int):
    if command_id == Command.LIST.value:
        print_all_saved_ssh()
    elif command_id == Command.ADD.value:
        ask_info_for_new_ssh_entry()
    elif command_id == Command.CONNECT.value:
        print(locale_manager.get_localized_string('choose_ssh'))
        print_all_saved_ssh()
        ask_and_open_new_connection()
        return Command.EXIT
    elif command_id == Command.EXIT.value:
        return Command.EXIT

