import pygame
import Config
import Utils
import Map
import Objects
import Input


def main_screen(screen, clock):
    Objects.TypeSwitch('map', (Config.width - 50, 50), is_pressed=True)
    Objects.TypeSwitch('sat', (Config.width - 50, 100))
    Objects.TypeSwitch('sat,skl', (Config.width - 50, 150))

    search_field = Input.TextInput()
    Objects.CancelButton((450, Config.height - 20))
    Objects.IndexButton((450, Config.height - 40))
    Objects.InfoBuffer((10, 10))

    map_instance = Map.Map()
    map_instance.reload_image()

    # Main Loop
    while True:
        events = pygame.event.get()
        for event in events:
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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                button_pressed = False
                for sprite in Objects.TypeSwitch.button_group.sprites():
                    if sprite.rect.collidepoint(x, y):
                        map_instance.type = sprite.type
                        map_instance.reload_image()
                        sprite.keydown()
                        button_pressed = True
                for sprite in Objects.CancelButton.button_group.sprites():
                    if sprite.rect.collidepoint(x, y):
                        Utils.clear_results(map_instance, search_field)
                        button_pressed = True
                for sprite in Objects.IndexButton.button_group.sprites():
                    if sprite.rect.collidepoint(x, y):
                        map_instance.index = not map_instance.index
                        map_instance.reload_image()
                        if map_instance.last_found_object:
                            Objects.InfoBuffer.button_group.set_address(
                                map_instance.last_found_object.get_address(with_index=map_instance.index)
                            )
                        button_pressed = True
                if not button_pressed:
                    if event.button == 1:
                        Utils.clear_results(map_instance, search_field)
                        coord = Utils.what_is_it((x, y), map_instance.zoom, map_instance.coord)
                        obj = Utils.search(','.join(map(str, coord)))
                        if obj:
                            map_instance.last_found_object = obj
                            Objects.InfoBuffer.button_group.set_address(obj.get_address(with_index=map_instance.index))
                        map_instance.point = coord
                        map_instance.reload_image()

        if search_field.update(events):
            obj = Utils.search(search_field.get_text())
            if obj:
                map_instance.last_found_object = obj
                Objects.InfoBuffer.button_group.set_address(obj.get_address(with_index=map_instance.index))
                map_instance.coord = obj.get_center()
                map_instance.point = obj.get_center()
                map_instance.reload_image()

        screen.blit(map_instance.image, (0, 0))
        Objects.TypeSwitch.button_group.draw(screen)
        Objects.CancelButton.button_group.draw(screen)
        Objects.IndexButton.button_group.draw(screen)
        Objects.InfoBuffer.button_group.draw(screen)
        screen.blit(search_field.get_surface(), (10, Config.height - 30))

        pygame.display.flip()
        clock.tick(Config.fps)


def main():
    screen = Utils.init()
    clock = pygame.time.Clock()
    main_screen(screen, clock)


if __name__ == '__main__':
    main()
