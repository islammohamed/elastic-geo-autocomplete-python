from wsgiref import simple_server

import falcon
from elasticsearch import Elasticsearch

from resources import CityAutoCompleteResource

api = application = falcon.API()
api.add_route('/autocomplete', CityAutoCompleteResource(Elasticsearch()))

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, api)
    httpd.serve_forever()