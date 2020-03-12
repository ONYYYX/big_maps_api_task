import pygame
import Config
import Utils
import Map
import Objects


def main_screen(screen, clock):
    Objects.TypeSwitch('map', (Config.width - 50, 50), is_pressed=True)
    Objects.TypeSwitch('sat', (Config.width - 50, 100))
    Objects.TypeSwitch('sat,skl', (Config.width - 50, 150))

    map_instance = Map.Map()
    map_instance.reload_image()

    # Main Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Utils.terminate()
            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_PAGEUP]:
                    map_instance.zoom += 1
                elif pygame.key.get_pressed()[pygame.K_PAGEDOWN]:
                    map_instance.zoom -= 1
                elif pygame.key.get_pressed()[pygame.K_RIGHT]:
                    map_instance.offset(1, 0)
                elif pygame.key.get_pressed()[pygame.K_LEFT]:
                    map_instance.offset(-1, 0)
                elif pygame.key.get_pressed()[pygame.K_DOWN]:
                    map_instance.offset(0, -1)
                elif pygame.key.get_pressed()[pygame.K_UP]:
                    map_instance.offset(0, 1)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for sprite in Objects.TypeSwitch.button_group.sprites():
                    if sprite.rect.collidepoint(x, y):
                        map_instance.type = sprite.type
                        sprite.keydown()
        screen.blit(map_instance.image, (0, 0))
        Objects.TypeSwitch.button_group.draw(screen)
        pygame.display.flip()
        clock.tick(Config.fps)


def main():
    screen = Utils.init()
    clock = pygame.time.Clock()
    main_screen(screen, clock)


if __name__ == '__main__':
    main()
