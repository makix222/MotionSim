import json
import pygame


class MainMenuEvents:
    def __init__(self):
        options_logs = 'Actions/MenuOptions.json'

        with open(options_logs) as f:
            self.menu_log = json.load(f)


class EventController:
    def __init__(self):
        """Generate a list of events and understand all current states"""
        self.state_list = {}

    def update(self, events):
        """
        Take in all the new events.
        Check to see if any of them modify the existing states.
        If it does not modify any of the existing states, add it to the list.
        """
        for event in events:
            if event.type == pygame.QUIT:
                return True


