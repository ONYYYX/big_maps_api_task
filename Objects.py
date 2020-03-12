import pygame


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
