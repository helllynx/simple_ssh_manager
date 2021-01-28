from enum import Enum


class Command(Enum):
    LIST = 0
    ADD = 1
    CONNECT = 2

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
        print('LIST')
    elif command_id == Command.ADD.value:
        print('ADD')
    elif command_id == Command.CONNECT.value:
        print('CONNECT')
