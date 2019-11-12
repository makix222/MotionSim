import pygame


def find_center(surface):
    # Will output the center of the given screen
    size = surface.get_size()
    return int(size[0] / 2), int(size[1] / 2)


def corrected_center(anchor, moved):
    if anchor is pygame.Surface:
        a = find_center(anchor)
    elif anchor is pygame.Rect:
        a = (anchor[0] + int(anchor[3] / 2), anchor[2])
    else:
        a = (0, 0)
    if anchor is pygame.Surface:
        b = find_center(moved)
    elif anchor is pygame.Rect:
        b = (moved[0] + int(moved[3] / 2), moved[2])
    else:
        b = (0, 0)

    return a[0] - b[0], a[1] - b[1]
