import json
import os

from app import database_path, locale_manager
from app.ssh import open_console_with_connection, create_ssh_command_from_record, create_sshfs_command_from_record


def print_all_saved_ssh():
    data = load_all_entities()
    if not data:
        print(locale_manager.get_localized_string('empty'))
        return
    for i, (k, v) in enumerate(data.items()):
        print(f"{i}. {k}: {v['host']}")


def print_all_groups():
    data = load_all_entities()
    if not data:
        print(locale_manager.get_localized_string('empty'))
        return
    for i, (k, _) in enumerate(data.items()):
        print(f"{i}. {k}")


def get_connection(group_id: int, connection_id: int):
    data = load_all_entities()
    key = list(data.keys())[group_id]
    return [data[key], key]


def get_group_by_id(id: int):
    data = load_all_entities()
    key = list(data.keys())[id]
    return [data[key], key]


def load_all_entities():
    with open(database_path, 'r+') as file:
        data = file.read()
    try:
        return json.loads(data)
    except:
        return {}


def create_group():
    group_name = input('group name: ')
    if not group_name:
        return create_group()
    data = load_all_entities()
    if group_name in data.keys():
        print(locale_manager.get_localized_string('group_duplicate'))
        return create_group()
    data[group_name] = {}
    save_database(data)
    return group_name


def ask_about_group():
    print_all_groups()
    print(locale_manager.get_localized_string('break'))
    data = load_all_entities()
    if not data:
        print(locale_manager.get_localized_string('empty_group'))

    group_id = input("> ")
    if group_id == 'q':
        return
    return get_group_by_id(int(group_id))


def ask_info_for_creating_group_or_connection():
    print(locale_manager.get_localized_string('entity_type'))
    entity_type = input('> ')
    if entity_type == 's':
        group = ask_about_group()
    elif entity_type == 'g':
        group = create_group()
    else:
        return ask_info_for_creating_group_or_connection()

    alias = input("alias: ")
    user = input("user (root): ")
    host = input("host: ")
    port = input("port (22): ")
    password = input("password (or empty if using keys): ")
    ssh_key = input("ssh_key path: ")

    check_ssh_entry_input(
        alias=alias,
        group=group[1],
        user=user,
        host=host,
        port=port,
        password=password,
        ssh_key=ssh_key
    )

    save_ssh_entry(
        alias=alias,
        group=group[1],
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
    data = load_all_entities()
    key = list(data.keys())[id]
    del data[key]
    save_database(data)


def save_database(data: dict):
    with open(database_path, 'w') as file:
        file.write(json.dumps(data))


def save_ssh_entry(alias: str, group: str, host: str, port: str = 22, user: str = 'root', password: str = None,
                   ssh_key: str = None):
    data = load_all_entities()

    if data[group]:
        if alias in data.keys() or [i['host'] for i in data.values()]:
            raise Exception(f"Entry with {alias} or {host} is already exists")

    data[group][alias] = {
        "user": user,
        "host": host,
        "port": port,
        "password": password,
        "ssh_key": ssh_key
    }

    save_database(data)


def check_ssh_entry_input(alias: str, group: str, host: str, port: str, user: str, password: str,
                          ssh_key: str):
    if not alias.isalpha():
        raise Exception('alias must be alpha')
    if not host.isalpha():
        raise Exception('host must be alpha')
    port = int(port)
    if not 0 < port < 65000:
        raise Exception('port must be from 0 to 65000')
    if ' ' in user:
        raise Exception('user cant contain spaces')
    

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
