import pygame
import world_params as wp
import Actions.events as events


class Menu:
    def __init__(self, size, name):
        self.menu_screen = pygame.Surface(size)
        self.border_thickness = 5
        self.border_color = (0, 50, 255)
        self.border_rect = (self.border_thickness,
                            self.border_thickness,
                            size[0] - (2 * self.border_thickness),
                            size[1] - (2 * self.border_thickness))
        self.size = size
        self.name = name

        self.font_size = 20
        self.name_text = pygame.font.Font(wp.desired_font, self.font_size)
        self.name_text_screen = self.name_text.render(self.name, True, self.border_color, wp.background_color)
        self.name_location = (int(self.name_text_screen.get_size()[0] / 2), 0)
        self.__button_manager__()

    def __draw_border__(self):
        pygame.draw.rect(self.menu_screen, self.border_color, self.border_rect, self.border_thickness)
        self.menu_screen.blit(self.name_text_screen, self.name_location)

    def update(self):
        display = pygame.display.get_surface()
        self.__draw_border__()
        self.__draw_buttons__()
        display.blit(self.menu_screen, (0, 0))

    def __button_manager__(self):
        # Set all the features of the buttons
        option_list = events.MainMenuEvents().menu_log["Main Menu"]
        option_count = 0
        button_max_height = int(self.size[1] / len(option_list))
        button_padding = 2
        button_start = (2 * self.border_thickness, 2 * self.border_thickness)
        button_height = button_max_height - (2 * self.border_thickness) - (2 * button_padding)
        button_width = self.size[0] - (2 * self.border_thickness + 2 * button_padding)
        self.button_layout ={}
        for option_name in option_list:
            # Create a dict laying out the button positions
            button_start = (button_start[0], button_start[1] + (button_max_height * option_count))
            self.button_layout[option_name] = {'size': (button_width, button_height),
                                               'position': button_start}
            option_count += 1

    def __draw_buttons__(self):
        for name in self.button_layout:
            size = self.button_layout[name]['size']
            position = self.button_layout[name]['position']
            button_rect = pygame.Rect(size, position)
            pygame.draw.rect(self.menu_screen, self.border_color, button_rect, self.border_thickness)

            button_text_screen = self.name_text.render(name, True, self.border_color, wp.background_color)
            button_text_location = (int(self.name_text_screen.get_size()[0] / 2), 0)





