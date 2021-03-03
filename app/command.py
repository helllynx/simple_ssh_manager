class Command:
    def __init__(self, command: str, short_command: str, description: str):
        self.command = command
        self.short_command = short_command
        self.description = description

    def __str__(self):
        return f"-{self.short_command} ({self.command}) {self.description}"


COMMANDS = [
    Command('list', 'l', 'Show all'),
    Command('new', 'n', 'Add new'),
    Command('delete', 'd', 'Delete'),
    Command('connect', 'c', 'Connect'),
    Command('exit', 'e', 'Exit'),
]


# Command = Enum('Command', ['List all connections', 'Add new connection', 'Delete connection', 'Connect', 'Exit'], start=0)


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
