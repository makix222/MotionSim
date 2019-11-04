import pygame
from collections import deque


class Graph:
    def __init__(self, name):
        self.name = name
        self.x_size = 150
        self.y_size = 80
        self.graph_size = (self.x_size, self.y_size)
        self.border_size = 3
        self.color = (10, 255, 10)
        self.history = deque([], maxlen=self.x_size)

    def __draw_border__(self, surface):
        pygame.draw.rect(surface, (125, 125, 125), ((0, 0), self.graph_size), self.border_size)
        # Add Graph Name

    def __graph_data__(self, surface):
        for position in enumerate(self.history):
            pygame.draw.circle(surface, (255, 0, 0), position, 1, 1)

    def draw(self):
        graph = pygame.Surface(self.graph_size)
        self.__draw_border__(graph)
        self.__graph_data__(graph)
        pygame.display.get_surface().blit(graph, (0, 0))

    def add_value(self, value, val_range):
        # convert value to percent in range
        if value < val_range[0]:
            value_percent = 0
        elif value > val_range[1]:
            value_percent = 1
        else:
            value_percent = (value - val_range[0]) / (val_range[1] - val_range[0])
        # Now convert the value to a point on the graph
        data_point = value_percent * self.y_size
        self.history.appendleft(int(data_point))



