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

    def get_address(self, with_index=False):
        a = self.data['metaDataProperty']['GeocoderMetaData']['Address']['formatted']
        try:
            if with_index:
                a += f", {self.data['metaDataProperty']['GeocoderMetaData']['Address']['postal_code']}"
        except Exception:
            pass
        return a


class Organization:
    def __init__(self, data):
        self.data = data

    def get_center(self):
        return tuple(self.data['geometry']['coordinates'])

    def get_address(self, with_index=False):
        return self.data['properties']['CompanyMetaData']['name'] \
               + ': ' + self.data['properties']['CompanyMetaData']['address']


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


class SearchOrganization(Service):
    server = Config.sfo_api_server

    @classmethod
    def send_request(cls, text, **params):
        p = {
            'text': text,
            'apikey': Config.sfo_api_key,
            'lang': 'ru_RU',
            'results': 1,
            'type': 'biz',
            **params
        }
        objects = Response(
            requests.get(cls.server, params=p)
        ).to_json()['features']
        if len(objects):
            return Organization(objects[0])

