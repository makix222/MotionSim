import pygame
import Actions.events as ev
import world_params as wp
import ball_motion
import menu


pygame.init()

size_x = 800
size_y = 700
size = [size_x, size_y]

screen = pygame.display.set_mode(size)
screen.fill(wp.background_color)

if 'segoeui' in pygame.font.get_fonts():
    wp.desired_font = pygame.font.match_font('segoeui')
else:
    wp.desired_font = None

clock = pygame.time.Clock()
brain = ev.EventController()
done = False
while not done:
    # Were back again. Junk fills the screen. Lets be lazy and blow it away
    pygame.Surface.fill(screen, wp.background_color)
    # Now what is going on Mr. Brain?
    done = brain.update(pygame.event.get())

    pygame.display.flip()
    clock.tick(1 / wp.frame_rate)

pygame.display.quit()
pygame.quit()
