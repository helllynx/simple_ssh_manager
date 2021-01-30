import json

from app import database_path
from app.ssh import open_console_with_connection, create_command_from_record


def print_all_saved_ssh():
    data = load_all_ssh_entries()
    for i, (k, v) in enumerate(data.items()):
        print(f"{i}. {k}: {v['host']}")


def get_connection_by_id(id: int):
    data = load_all_ssh_entries()
    return data[list(data.keys())[id]]


def load_all_ssh_entries():
    with open(database_path, 'r') as file:
        data = file.read()
    try:
        return json.loads(data)
    except:
        return {}


def ask_info_for_new_ssh_entry():
    alias = input("alias: ")
    user = input("user: ")
    host_ip = input("host ip: ")
    port = input("port: ")
    password = input("password (or empty if using keys): ")
    ssh_key = input("ssh_key path: ")

    save_ssh_entry(alias, user, host_ip, port, password, ssh_key)


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


def save_ssh_entry(alias: str, user: str, host: str, port: str, password: str = None, ssh_key: str = None):
    data = load_all_ssh_entries()

    if not port:
        port = 22

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
    connection_id = int(input("> "))
    command = create_command_from_record(get_connection_by_id(connection_id))
    open_console_with_connection(command)
