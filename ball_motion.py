import pygame
import random
import numpy as np
import math
import world_params as wp


class BallPit:
    def __init__(self):
        self.ball_count = 0
        self.ball_log = {}
        self.display = pygame.display.get_surface()
        self.ball_surface = pygame.Surface(self.display.get_size())

    def add_ball(self, position):
        self.ball_count += 1
        self.ball_log[self.ball_count] = Ball(self.ball_surface, 10, position)

    def update_all(self):
        for each_ball in self.ball_log.items():
            each_ball[1].update()
        self.__draw_surface__()

    def __draw_surface__(self):
        self.display.blit(self.ball_surface, (0, 0))
        self.ball_surface.fill(wp.background_color)


class Ball:
    def __init__(self, screen, radius, position):
        self.surface = screen
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.color = (r, g, b)
        self.radius = radius
        self.volume = math.pi * math.sqrt(radius)
        # Density is based upon iron (lb/in^3)
        self.density = 0.284
        self.mass = self.density * self.volume
        self.distance = position[0]
        self.height = position[1]
        self.velocity_height = 0
        self.velocity_height_history = []

    def update(self):
        # Should update the position of the ball when called.
        if not self.__is_stationary__():
            self.velocity_height = self.velocity_height + (wp.gravity * wp.frame_rate)
            self.height = self.height + (0.5 * self.velocity_height * wp.frame_rate)
        self.__draw__()

    def __is_stationary__(self):
        if self.height >= self.surface.get_height() - self.radius:
            self.velocity_height = 0
            return True
        else:
            return False

    def __draw__(self):
        pygame.draw.circle(
            self.surface,
            self.color,
            (int(self.distance), int(self.height)),
            self.radius,
            1,
        )

    def set_ball_position(self, position):
        self.distance = position[0]
        self.height = position[1]

    def move_ball(self, force_vector):
        if np.linalg.norm(force_vector) > 0:
            # Move Ball
            self.velocity_height = force_vector

