import pygame
import menu


class LaunchWindow:
    def __init__(self):
        surface = pygame.display.get_surface()
        self.menu = menu.Menu(surface.get_size(), 'Welcome')

    def refresh(self):
        self.menu.refresh()
