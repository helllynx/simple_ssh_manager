from enum import Enum
from app import locale_manager
from app.storage import print_all_saved_ssh, ask_info_for_new_ssh_entry, delete_ssh_entry, ask_and_open_new_connection, \
    ask_and_mount_sshfs


class Commands(Enum):
    NEW = 'new'
    DELETE = 'delete'
    SSHFS = 'sshfs'
    CONNECT = 'connect'
    EXIT = 'exit'

    @staticmethod
    def get_localized_descriptions_dict():
        commands_locale = locale_manager.get_localized_commands()
        return [commands_locale[c.value] for c in list(Commands)]



def print_all_commands():
    for i, cn in enumerate(Commands.get_localized_descriptions_dict()):
        print(f'{i}. {cn}')


def get_func_by_id(id: int):
    return list(Commands)[id]


def run_command(command_name: str):
    if command_name == Commands.NEW:
        ask_info_for_new_ssh_entry()
    elif command_name == Commands.DELETE:
        delete_ssh_entry()
    elif command_name == Commands.SSHFS:
        print(locale_manager.get_localized_string('choose_ssh'))
        print_all_saved_ssh()
        ask_and_mount_sshfs()
    elif command_name == Commands.CONNECT:
        print(locale_manager.get_localized_string('choose_ssh'))
        print_all_saved_ssh()
        ask_and_open_new_connection()
    elif command_name == Commands.EXIT:
        return Commands.EXIT

