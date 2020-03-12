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
        screen.blit(map_instance.image, (0, 0))
        pygame.display.flip()
        clock.tick(Config.fps)


def main():
    screen = Utils.init()
    clock = pygame.time.Clock()
    main_screen(screen, clock)


if __name__ == '__main__':
    main()
