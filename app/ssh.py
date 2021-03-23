import os

from app import sshfs_mount_folder


def open_console_with_connection(ssh_command: str):
    os.system(f"konsole -e {ssh_command} &")


def create_ssh_command_from_record(record: str):
    return f"ssh {record['user']}@{record['host']} -p {record['port']}"


# TODO add function to distinguish home folder
def create_sshfs_command_from_record(record: str):
    home = "/home/helllynx"
    mount_directory_path = f"{home}/{sshfs_mount_folder}/{record['']}"
    return f"sshfs {record['user']}@{record['host']}:/ {mount_directory_path} -p {record['port']}"