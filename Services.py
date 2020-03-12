import os
import requests
import Config


class Response:
    def __init__(self, data):
        self.data = data

    def to_json(self):
        return self.data.json()

    def to_file(self, filename):
        with open(os.path.join(Config.media_dir, Config.maps_dir, filename), 'wb') as f:
            f.write(self.data.content)


class Service:
    server = ''

    @classmethod
    def send_request(cls, **params):
        return Response(requests.get(cls.server, params=params))


class StaticAPI(Service):
    server = Config.maps_api_server

    @classmethod
    def send_request(cls, map_type, coord, **params):
        p = {
            'l': map_type,
            'll': ','.join(map(str, coord)),
            'size': ','.join(map(str, (Config.width, Config.height))),
            **params
        }
        return Response(requests.get(cls.server, params=p))
