import json
import pygame
import menu


class MainMenuEvents:
    def __init__(self):
        options_logs = 'Actions/MenuOptions.json'

        with open(options_logs) as f:
            self.menu_log = json.load(f)


class EventController:
    def __init__(self):
        """Generate a list of events and understand all current states"""
        self.state_list = []
        self.main_menu = menu.Menu((300, 400), "Main Menu")
        self.KEY_ESCAPE = None

    def update(self, events):
        """
        Take in all the new events.
        Check to see if any of them modify the existing states.
        If it does not modify any of the existing states, add it to the list.
        """
        for e in events:
            if e.type == pygame.QUIT:
                return True
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    if self.KEY_ESCAPE:
                        self.state_list.remove(self.main_menu)
                        self.KEY_ESCAPE = False
                    else:
                        self.state_list.clear()
                        self.state_list.append(self.main_menu)
                        self.KEY_ESCAPE = True

        for methods in self.state_list:
            methods.update()




