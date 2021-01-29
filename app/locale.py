import json
from enum import Enum


class Locale(Enum):
    RU = 'ru'
    US = 'us'


class LocaleManager:

    def __init__(self):
        with open('strings.json', 'r') as file:
            data = file.read()
        self.json = json.loads(data)
        self.locale = Locale.US
        self.text = self.json[self.locale.value]

    def get_localized_string(self, string_id: str):
        return self.text[string_id]


