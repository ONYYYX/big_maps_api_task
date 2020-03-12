import os
import Config
import Utils
import Services


class Map:
    def __init__(self):
        self._type = 'map'
        self._coord = (49.613829, 54.214371)
        self._zoom = 10
        self._image = 0

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def coord(self):
        return self._coord

    @coord.setter
    def coord(self, value):
        x, y = value
        x = Utils.clamp(-180.0, x, 180.0)
        y = Utils.clamp(-90.0, y, 90.0)
        self._coord = x, y

    @property
    def zoom(self):
        return self._zoom

    @zoom.setter
    def zoom(self, value):
        self._zoom = Utils.clamp(0, value, 17)

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    def reload_image(self):
        Services.StaticAPI.send_request(
            map_type=self.type,
            coord=self.coord,
            z=self.zoom
        ).to_file(Config.map_filename)
        self.image = Utils.load_image(os.path.join(Config.maps_dir, Config.map_filename))

    def offset(self, a, b):
        x, y = self.coord
        print(Config.width * (360.0 / 2 ** (self.zoom + 8)))
        self.coord = (
            x + a * Config.width * (360.0 / 2 ** (self.zoom + 8)),
            y + b * Config.height * (360.0 / 2 ** (self.zoom + 8))
        )
