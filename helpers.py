import pygame


def find_surface_center(surface):
    surface_rect = surface.get_rect()
    return surface_rect.center


def find_rect_center(rect):
    return rect.center


def corrected_center(anchor, moved):
    if isinstance(anchor, pygame.Surface):
        a = find_surface_center(anchor)
        print(anchor, "is a surface with value", a)
    elif isinstance(anchor, pygame.Rect):
        a = find_rect_center(anchor)
        print(anchor, "is a rect with value", a)
    else:
        a = (0, 0)
    if isinstance(moved, pygame.Surface):
        b = find_surface_center(moved)
    elif isinstance(moved, pygame.Rect):
        b = find_rect_center(moved)
    else:
        b = (0, 0)

    return a[0] - b[0], a[1] - b[1]
