import os


def open_console_with_connection(ssh_command: str):
    os.system(f"konsole -e {ssh_command} &")


def create_command_from_record(record: str):
    return f"ssh {record['user']}@{record['host']} -p {record['port']}"
