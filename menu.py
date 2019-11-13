import pygame
import world_params as wp
import Actions.events as events
import helpers


class Menu:
    def __init__(self, size, name):
        """Creates most of the initial parameters to lay out a menu screen"""
        self.menu_screen = pygame.Surface(size)
        self.border_thickness = 5
        self.padding = 5
        self.border_color = (0, 50, 255)
        self.border_rect = self.menu_screen.get_rect().inflate(-2 * self.border_thickness,
                                                               -2 * self.border_thickness)
        self.working_size = self.border_rect.inflate(-2 * self.padding, -2 * self.padding)

        # Text section
        self.name = name
        self.font_size = 20
        self.name_text = pygame.font.Font(wp.desired_font, self.font_size)
        self.name_text_screen = self.name_text.render(self.name, True, self.border_color, wp.background_color)
        self.name_location = (helpers.find_center(self.name_text_screen)[0], self.working_size.left)

        # Define some values for where the buttons go
        self.button_area = (self.working_size.width,
                            self.working_size.height - self.name_text_screen.get_height() - self.padding)
        self.button_start_pos = (self.working_size.top,
                                 self.name_location[1] + self.name_text_screen.get_height() + self.padding)
        # Button area = size - start position

        self.button_screen = pygame.Surface(self.button_area)
        self.__button_manager__()

    def __draw_border__(self):
        pygame.draw.rect(self.menu_screen, self.border_color, self.border_rect, self.border_thickness)
        self.menu_screen.blit(self.name_text_screen, self.name_location)

    def update(self):
        """Run every frame to draw the menu"""

        self.__draw_border__()
        self.__draw_buttons__()
        self.__check_mouse__()

        # Now that we have added everything to the menu screen, lets put it on the main window
        display = pygame.display.get_surface()
        display_center = helpers.corrected_center(display, self.menu_screen)
        display.blit(self.menu_screen, display_center)

    def __check_mouse__(self):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed():
            pass

    def __position_is_menu(self, position):
        # check if position is over menu selection. If yes, return which selection
        a = self.button_layout
        pass


    def __button_manager__(self):
        # Set all the features of the buttons
        button_size = self.button_area
        option_list = events.MainMenuEvents().menu_log["Main Menu"]
        button_max_height = int(button_size[1] / len(option_list))
        button_start = (0, 0)
        button_height = button_max_height - (2 * self.padding)
        button_width = button_size[0]
        self.button_layout = {}
        for option_name in option_list:
            # Create a dict laying out the button positions
            self.button_layout[option_name] = pygame.Rect(button_start, (button_width, button_height))
            button_start = (button_start[0], button_start[1] + button_max_height)

    def __draw_buttons__(self):
        for name in self.button_layout:
            button_rect = self.button_layout[name]
            pygame.draw.rect(self.button_screen, self.border_color, button_rect, self.border_thickness)

            # Now lets create the text in the middle
            button_text_screen = self.name_text.render(name, True, self.border_color, wp.background_color)
            # We have a font screen. Now we need to get the centers of the button and font.
            # ToDo: Get the helper function to work with a RECT or a Surface to get the text location working
            button_text_location = helpers.corrected_center(button_rect, button_text_screen)
            # Add the text to the screen
            self.button_screen.blit(button_text_screen, button_text_location)
        # Add the buttons to the menu screen
        self.menu_screen.blit(self.button_screen, self.button_start_pos)






