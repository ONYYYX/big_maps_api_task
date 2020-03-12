import pygame
import Map

pygame.font.init()


class SwitchGroup(pygame.sprite.Group):
    def keyup(self):
        for sprite in self.sprites():
            sprite.keyup()


class TypeSwitch(pygame.sprite.Sprite):
    button_group = SwitchGroup()
    button_image = pygame.Surface((25, 25))
    button_image.fill((109, 109, 109))
    button_image_pressed = pygame.Surface((25, 25))
    button_image_pressed.fill((152, 152, 152))

    def __init__(self, map_type, position, is_pressed=False):
        super().__init__(self.button_group)
        self.image = TypeSwitch.button_image if not is_pressed else TypeSwitch.button_image_pressed
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.type = map_type
        self.is_pressed = is_pressed

    def keydown(self):
        self.button_group.keyup()
        self.is_pressed = True
        self.image = self.button_image_pressed

    def keyup(self):
        self.is_pressed = False
        self.image = self.button_image


class CancelGroup(pygame.sprite.Group):
    pass


class CancelButton(pygame.sprite.Sprite):
    button_group = CancelGroup()
    button_image = pygame.Surface((60, 10))
    button_image.fill((109, 109, 109))
    button_text = pygame.font.Font(None, 12).render('Сброс', True, (0, 0, 0), (109, 109, 109))
    button_image.blit(button_text, (0, 0))

    def __init__(self, position):
        super().__init__(self.button_group)
        self.image = CancelButton.button_image
        self.rect = self.image.get_rect()
        self.rect.topleft = position


class IndexGroup(pygame.sprite.Group):
    pass


class IndexButton(pygame.sprite.Sprite):
    button_group = IndexGroup()
    button_image = pygame.Surface((60, 10))
    button_image.fill((109, 109, 109))
    button_text = pygame.font.Font(None, 12).render('Индекс', True, (0, 0, 0), (109, 109, 109))
    button_image.blit(button_text, (0, 0))

    def __init__(self, position):
        super().__init__(self.button_group)
        self.image = IndexButton.button_image
        self.rect = self.image.get_rect()
        self.rect.topleft = position


class InfoGroup(pygame.sprite.Group):
    def set_address(self, address):
        for sprite in self.sprites():
            sprite.set_address(address)


class InfoBuffer(pygame.sprite.Sprite):
    button_group = InfoGroup()
    button_image = pygame.Surface((600, 25))
    button_image.fill((255, 255, 255))

    def __init__(self, position):
        super().__init__(self.button_group)
        self.image = InfoBuffer.button_image
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def set_address(self, address):
        button_text = pygame.font.Font(None, 16).render(address, True, (0, 0, 0), (255, 255, 255))
        self.image.fill((255, 255, 255))
        self.image.blit(button_text, (0, 0))

