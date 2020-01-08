import pygame
import random
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
        new_ball = Ball(self.ball_surface, 10, position)
        new_ball.apply_force((random.randint(-100, 100), random.randint(-100, 100)))
        self.ball_log[self.ball_count] = new_ball

    def update_all(self):
        for each_ball in self.ball_log.items():
            each_ball[1].refresh()
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
        self.x_pos, self.y_pos = position
        self.y_vel = 0
        self.x_vel = 0

    def update(self):
        # Should update the position of the ball when called.
        if not self.__is_stationary__():
            self.y_vel += (wp.gravity * wp.frame_rate)
            self.y_pos += (0.5 * self.y_vel * wp.frame_rate)
            self.x_pos += self.x_vel * wp.frame_rate
        self.__draw__()

    def __is_stationary__(self):
        if self.y_pos >= self.surface.get_height() - self.radius:
            self.y_vel, self.x_vel = (0, 0)
            return True
        else:
            return False

    def __draw__(self):
        pygame.draw.circle(
            self.surface,
            self.color,
            (int(self.x_pos), int(self.y_pos)),
            self.radius,
            1,
        )

    def set_ball_position(self, position):
        self.x_pos, self.y_pos = position

    def apply_force(self, force_vector):
        self.x_vel, self.y_vel = force_vector

