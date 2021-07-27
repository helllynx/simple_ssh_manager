import json
import os

from app import database_path, locale_manager
from app.ssh import open_console_with_connection, create_ssh_command_from_record, create_sshfs_command_from_record


def print_all_saved_ssh():
    data = load_all_ssh_entries()
    for i, (k, v) in enumerate(data.items()):
        print(f"{i}. {k}: {v['host']}")


def get_connection_by_id(id: int):
    data = load_all_ssh_entries()
    key = list(data.keys())[id]
    return [data[key], key]


def load_all_ssh_entries():
    with open(database_path, 'r') as file:
        data = file.read()
    try:
        return json.loads(data)
    except:
        return {}


def ask_info_for_new_ssh_entry():
    alias = input("alias: ")
    user = input("user (root): ")
    host = input("host: ")
    port = input("port (22): ")
    password = input("password (or empty if using keys): ")
    ssh_key = input("ssh_key path: ")

    save_ssh_entry(
        alias=alias,
        user=user,
        host=host,
        port=port,
        password=password,
        ssh_key=ssh_key
    )


# def ask_info_for_edit_ssh_entry():
#     user = input("user: ")
#     host_ip = input("host ip: ")
#     port = int(input("port: "))
#     password = input("password (or empty if using keys): ")
#     ssh_key = input("ssh_key path: ")
#
#     save_ssh_entry(alias, user, host_ip, port, password, ssh_key)


def delete_ssh_entry():
    id = int(input("id > "))
    data = load_all_ssh_entries()
    key = list(data.keys())[id]
    del data[key]

    with open(database_path, 'w') as file:
        file.write(json.dumps(data))


def save_ssh_entry(alias: str, host: str, port: str = 22, user: str = 'root', password: str = None,
                   ssh_key: str = None):
    data = load_all_ssh_entries()

    if alias in data.keys():
        raise Exception(f"Entry {alias} already exists")

    data[alias] = {
        "user": user,
        "host": host,
        "port": port,
        "password": password,
        "ssh_key": ssh_key
    }

    with open(database_path, 'w') as file:
        file.write(json.dumps(data))


def ask_and_open_new_connection():
    print(locale_manager.get_localized_string('break'))
    connection_id = input("> ")
    if connection_id == 'q':
        return
    command = create_ssh_command_from_record(get_connection_by_id(int(connection_id)))
    open_console_with_connection(command)


def ask_and_mount_sshfs():
    print(locale_manager.get_localized_string('break'))
    connection_id = input("> ")
    if connection_id == 'q':
        return
    command = create_sshfs_command_from_record(get_connection_by_id(int(connection_id)))
    os.system(f'{command} &')
