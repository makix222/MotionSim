import pygame
import world_params as wp


class Menu:
    def __init__(self, size, name):
        self.menu_screen = pygame.Surface()
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
        self.name_text_screen = pygame.font.Font(desired_font, 4 * self.border_size)

    def draw_border(self):
        pygame.draw.rect(self.menu_screen, self.border_color, self.border_rect, self.border_size)
        self.name_text_screen.render(self.name, True, self.border_color, background=wp.background_color)
        name_location = (self.border_size, int(self.name_text_screen.size()[0] / 2))
        self.menu_screen.blit(self.name_text_screen, name_location)




