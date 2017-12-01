import falcon
import simplejson as json
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search


class CityAutoCompleteResource:
    index_name = 'geonames'

    def __init__(self, es_client):
        self.es_client = es_client

    def on_get(self, req, resp):
        """
        :param req:
        :param resp:
        :return:
        """

        city_query = req.get_param('name', '')
        search_query_set = Search(using=self.es_client, index=self.index_name).query("match", name=city_query)

        suggestions = [{'id': result.geonameid, 'name': result.name, 'country': result.country_code3}
                       for result in search_query_set
                       ]

        resp.body = json.dumps(suggestions)
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200
