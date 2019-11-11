import json


class MainMenuEvents:
    def __init__(self):
        options_logs = 'Actions/MenuOptions.json'

        with open(options_logs) as f:
            self.menu_log = json.load(f)

