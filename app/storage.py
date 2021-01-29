import json

from app import database_path


def print_all_saved_ssh():
    data = load_all_ssh_entries()
    for k, v in data.items():
        print(f"{k}: {v['host']}")


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
