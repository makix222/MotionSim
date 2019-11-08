import pygame
import world_params as wp


class Menu:
    def __init__(self, size, name):
        self.menu_screen = pygame.Surface(size)
        self.border_size = 5
        self.border_color = (0, 50, 255)
        self.border_rect = (self.border_size,
                            self.border_size,
                            size[0] - (2 * self.border_size),
                            size[1] - (2 * self.border_size))
        self.name = name

        if 'segoeui' in pygame.font.get_fonts():
            desired_font = pygame.font.match_font('segoeui')
        else:
            desired_font = None
        self.font_size = 20
        self.name_text = pygame.font.Font(desired_font, self.font_size)
        self.name_text_screen = self.name_text.render(self.name, True, self.border_color, wp.background_color)
        self.name_location = (int(self.name_text_screen.get_size()[0] / 2), 0)

    def draw_border(self):
        pygame.draw.rect(self.menu_screen, self.border_color, self.border_rect, self.border_size)
        self.menu_screen.blit(self.name_text_screen, self.name_location)
        pygame.display.get_surface().blit(self.menu_screen, (0, 0))




