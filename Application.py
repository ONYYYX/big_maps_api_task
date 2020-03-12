import pygame
import Config
import Utils
import Map


def main_screen(screen, clock):
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
                    map_instance.reload_image()
                elif pygame.key.get_pressed()[pygame.K_PAGEDOWN]:
                    map_instance.zoom -= 1
                    map_instance.reload_image()
                elif pygame.key.get_pressed()[pygame.K_RIGHT]:
                    map_instance.offset(1, 0)
                    map_instance.reload_image()
                elif pygame.key.get_pressed()[pygame.K_LEFT]:
                    map_instance.offset(-1, 0)
                    map_instance.reload_image()
                elif pygame.key.get_pressed()[pygame.K_DOWN]:
                    map_instance.offset(0, -1)
                    map_instance.reload_image()
                elif pygame.key.get_pressed()[pygame.K_UP]:
                    map_instance.offset(0, 1)
                    map_instance.reload_image()
        screen.blit(map_instance.image, (0, 0))
        pygame.display.flip()
        clock.tick(Config.fps)


def main():
    screen = Utils.init()
    clock = pygame.time.Clock()
    main_screen(screen, clock)


if __name__ == '__main__':
    main()
