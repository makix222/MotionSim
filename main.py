import pygame
import colors as co
import world_params as wp
import ball_motion


def draw_ball(print_screen, pos, radius):
    pygame.draw.circle(print_screen, co.green, pos, radius, 1)


pygame.init()

size_x = 800
size_y = 700
size = [size_x, size_y]

screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))

clock = pygame.time.Clock()
Steel = ball_motion.Ball(screen, 10, (int(size_x / 2), int(size_y / 2)))

done = False
while not done:
    pygame.Surface.fill(screen, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if pygame.mouse.get_pressed() == (1, 0, 0):
        Steel.set_ball_position(pygame.mouse.get_pos())

    Steel.update()

    pygame.display.flip()
    clock.tick(1 / wp.frame_rate)

pygame.display.quit()
pygame.quit()
