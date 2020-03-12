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


class Object:
    def __init__(self, data):
        self.data = data

    def get_center(self):
        return tuple(map(float, self.data['Point']['pos'].split()))


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


class GeoCoder(Service):
    server = Config.gc_api_server

    @classmethod
    def send_request(cls, geocode, **params):
        p = {
            'geocode': geocode,
            'apikey': Config.gc_api_key,
            'format': 'json',
            'results': 1,
            **params
        }
        objects = Response(
            requests.get(cls.server, params=p)
        ).to_json()['response']['GeoObjectCollection']['featureMember']
        if len(objects):
            return Object(objects[0]['GeoObject'])
