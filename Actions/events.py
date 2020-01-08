import json
import pygame
import menu
import Startup.start_page as start


class MainMenuEvents:
    def __init__(self):
        options_logs = 'Actions/MenuOptions.json'

        with open(options_logs) as f:
            self.menu_log = json.load(f)


class EventList:
    """ Class which contains a list of each new display or screen that will need to be drawn on each refresh """
    def __init__(self):
        self.master_list = []

    def add_event(self, new_object):
        if new_object not in self.master_list:
            self.master_list.append(new_object)

    def refresh(self):
        for each in self.master_list:
            each.refresh()

    def pop_event(self, busted_object):
        if busted_object in self.master_list:
            self.master_list.pop(self.master_list.index(busted_object))

    def clear(self):
        self.master_list = []


class EventController:
    def __init__(self):
        """ Starts everything off. Begins with the title page and will continue to keep track of which screen should
            be displayed next.

            Consists of a major top level loop which checks for events and based upon events, will manage the global
            list of screen refreshes.

            Generate a list of events and understand all current states"""
        # state_list should be the ordered list of what needs to happen next. Will be populated with new menus later
        self.event_list = EventList()
        self.event_list.add_event(start.LaunchWindow())
        # I guess I need to define some basic parameters for each menu? Im not sure on this one yet.
        self.main_menu = menu.Menu((300, 400), "Main Menu")
        # I guess there are global key variables that need to be preserved. This likely does not belong here.
        self.KEY_ESCAPE = None

    def refresh(self, events):
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
                        self.event_list.pop_event(self.main_menu)
                        self.KEY_ESCAPE = False
                    else:
                        self.event_list.clear()
                        self.event_list.add_event(self.main_menu)
                        self.KEY_ESCAPE = True

        self.event_list.refresh()




