import sys
import os
import pygame
import Config
import Services
import Map
import Input
import Objects

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


def what_is_it(position: tuple, zoom: int, coord: tuple):
    x, y = position
    a, b = coord
    c = 360.0 / 2 ** (zoom + 8)
    w, h = x - Config.width // 2, Config.height // 2 - y
    wg, hg = w * c, h * c
    a += wg
    b += hg
    return a, b


def clear_results(map_instance: Map.Map, search_field: Input.TextInput):
    map_instance.last_found_object = {}
    Objects.InfoBuffer.button_group.set_address('')
    search_field.clear_text()
    map_instance.point = ()
    map_instance.reload_image()
