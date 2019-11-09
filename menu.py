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
        self.__button_manger__()

    def draw_border(self):
        pygame.draw.rect(self.menu_screen, self.border_color, self.border_rect, self.border_thickness)
        self.menu_screen.blit(self.name_text_screen, self.name_location)
        pygame.display.get_surface().blit(self.menu_screen, (0, 0))

    def __button_manger__(self):

        option_list = events.MainMenuEvents.menu_log["Main Menu"]
        option_count = len(option_list)
        button_max_height = int(self.size[1] / option_count)
        button_padding = 2
        button_start = (2 * self.border_thickness, 2 * self.border_thickness)
        button_height = button_max_height - (2 * self.border_thickness) - (2 * button_padding)
        button_width = self.size[0] - (2 * self.border_thickness + 2 * button_padding)
        for each_option in option_list:
            self.draw_button((button_width, button_height),
                             button_start + (button_max_height * option_count),
                             each_option)
        pass

    def draw_button(self, size, position, option):
        button_rect = pygame.Rect(size=size, position=position)
        pygame.draw.rect(self.menu_screen, self.border_color, button_rect, self.border_thickness)

        button_text_screen = self.name_text.render(option.name, True, self.border_color, wp.background_color)
        button_text_location = (int(self.name_text_screen.get_size()[0] / 2), 0)





