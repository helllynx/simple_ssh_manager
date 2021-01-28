from main import config
import json

def print_all_ssh_records():
    with open(config['DATABASE']['DatabasePath'], 'r') as file:
        data = file.read()
    return json.loads(data)