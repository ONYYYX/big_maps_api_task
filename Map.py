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
        self.type = value

    @property
    def coord(self):
        return self._coord

    @coord.setter
    def coord(self, value):
        self.coord = Utils.clamp(-180.0, value, 180.0)

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
