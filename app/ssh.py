import os


def open_console_with_connection(ssh_command: str):
    os.system(f"konsole -e {ssh_command}")