import os

from app import sshfs_mount_folder, system_terminal


def open_console_with_connection(ssh_command: str):
    os.system(f"{system_terminal} {ssh_command} &")


def create_ssh_command_from_record(record: list):
    if record[0]['password']:
        return f"sshpass -p {record[0]['password']} ssh -o StrictHostKeyChecking=no {record[0]['user']}@{record[0]['host']} -p {record[0]['port']}"
    else:
        return f"ssh {record[0]['user']}@{record[0]['host']} -p {record[0]['port']}"


# TODO add function to distinguish home folder
def create_sshfs_command_from_record(record: list):
    home = os.path.expanduser('~')
    mount_directory_path = f"{home}/{sshfs_mount_folder}/{record[1]}"
    os.makedirs(mount_directory_path, exist_ok=True)
    return f"sshfs {record[0]['user']}@{record[0]['host']}:/ {mount_directory_path} -p {record[0]['port']}"

