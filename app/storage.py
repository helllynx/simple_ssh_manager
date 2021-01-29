import json

from app import database_path
from app.ssh import open_console_with_connection


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

def create_command_from_record(record: str):
    print(f"ssh {record['user']}@{record['host']} -p {record['port']}")
    return f"ssh {record['user']}@{record['host']} -p {record['port']}"

def ask_info_for_new_ssh_entry():
    alias = input("alias: ")
    user = input("user: ")
    host_ip = input("host ip: ")
    port = int(input("port: "))
    password = input("password (or empty if using keys): ")
    ssh_key = input("ssh_key path: ")

    save_ssh_entry(alias, user, host_ip, port, password, ssh_key)


def save_ssh_entry(alias: str, user: str, host_ip: str, port: int, password: str = None, ssh_key: str = None):
    data = load_all_ssh_entries()

    data[alias] = {
        "user": user,
        "host": host_ip,
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