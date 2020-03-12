import os
import Config
import Utils
import Services


class Map:
    def __init__(self):
        self._type = 'map'
        self._coord = (49.613829, 54.214371)
        self._zoom = 10
        self._point = ()
        self._index = False
        self._image = 0
        self.last_found_object = {}

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
    def point(self):
        return self._point

    @point.setter
    def point(self, value):
        self._point = value

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    def reload_image(self):
        params = {}
        if self.point:
            params['pt'] = f'{",".join(map(str, self.point))},vkbkm'
        Services.StaticAPI.send_request(
            map_type=self.type,
            coord=self.coord,
            z=self.zoom,
            **params
        ).to_file(Config.map_filename)
        self.image = Utils.load_image(os.path.join(Config.maps_dir, Config.map_filename))

    def offset(self, a, b):
        x, y = self.coord
        self.coord = (
            x + a * Config.width // 5 * (360.0 / 2 ** (self.zoom + 8)),
            y + b * Config.height // 5 * (360.0 / 2 ** (self.zoom + 8))
        )
