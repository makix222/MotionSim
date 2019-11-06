import pygame
import world_params as wp
import ball_motion


pygame.init()

size_x = 800
size_y = 700
size = [size_x, size_y]

screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))

clock = pygame.time.Clock()
balls = ball_motion.BallPit()

pressed = False
done = False
while not done:
    pygame.Surface.fill(screen, wp.background_color)
    for event in pygame.event.get():
        e = event.type
        if e == pygame.QUIT:
            done = True
        elif e == pygame.MOUSEBUTTONUP:
            if pressed:
                pressed = False

    if pygame.mouse.get_pressed() == (1, 0, 0):
        if not pressed:
            pressed = True
            balls.add_ball(pygame.mouse.get_pos())

    balls.update_all()

    pygame.display.flip()
    clock.tick(1 / wp.frame_rate)

pygame.display.quit()
pygame.quit()
