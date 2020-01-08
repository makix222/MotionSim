import pygame
import Actions.events as event
import world_params
import ball_motion
import Startup.start_page as start_out


pygame.init()

size_x = 800
size_y = 700
size = [size_x, size_y]

screen = pygame.display.set_mode(size)
screen.fill(world_params.background_color)

if 'segoeui' in pygame.font.get_fonts():
    world_params.desired_font = pygame.font.match_font('segoeui')
else:
    world_params.desired_font = None

clock = pygame.time.Clock()
brain = event.EventController()
done = False
while not done:
    # Were back again. Junk fills the screen. Lets be lazy and blow it away
    pygame.Surface.fill(screen, world_params.background_color)
    # On every frame, refresh should check all new events and figure out what next screen to display.
    done = brain.refresh(pygame.event.get())

    pygame.display.flip()
    clock.tick(1 / world_params.frame_rate)

pygame.display.quit()
pygame.quit()
