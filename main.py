from command import Command, run_command
import configparser

from locale import LocaleManager

config = configparser.ConfigParser()
config.read('config.ini')

locale_manager = LocaleManager()

if __name__ == '__main__':
    print(locale_manager.get_localized_string('greet'))
    Command.print_all_commands()
    command_id = None
    while True:
        try:
            command_id = int(input('> '))
            assert command_id >= 0 and Command.get_func_by_id(command_id)
            break
        except:
            print('Please write number of listed functions!')
            Command.print_all_commands()

    run_command(command_id)