from app import locale_manager
from app.command import run_command, print_all_commands, get_func_by_id, Commands
from app.utils import clear_terminal

if __name__ == '__main__':
    clear_terminal()
    print(locale_manager.get_localized_string('greet')+'\n')

    while True:
        try:
            print_all_commands()
            command_id = int(input('> '))
            clear_terminal()
            assert command_id >= 0 and get_func_by_id(command_id)
            if run_command(get_func_by_id(command_id)) == Commands.EXIT:
                break
        except:
            print('Please write number of listed functions!')
