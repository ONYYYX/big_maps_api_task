import sys
import os
import pygame
import Config
import Services

screen = 0


def init() -> pygame.Surface:
    if not pygame.get_init():
        pygame.init()
    global screen
    if not screen:
        screen = pygame.display.set_mode((Config.width, Config.height))
    return screen


def terminate() -> None:
    pygame.quit()
    sys.exit()


def load_image(name: str, convert: bool = True) -> pygame.Surface:
    init()  # Fix uninitialized display
    image = pygame.image.load(os.path.join(Config.media_dir, name))
    return image.convert_alpha() if convert else image


def clamp(min_value, x, max_value):
    return sorted((min_value, x, max_value))[1]


def search(text: str):
    if text:
        obj = Services.GeoCoder.send_request(text)
        return obj
