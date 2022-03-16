from itertools import count
from flask import Flask
from flask_restful import Resource, Api, reqparse
# 'Resource' is a base class that can define the routing for one or more HTTP methods for a given URL
# 'reqparse' is a parsing interface for HTTP request

app = Flask(__name__)
api = Api(app)

COUNTRIES = {
    '1': {'name': 'Austria', 'capital': 'Vienna'},
    '2': {'name': 'Bulgaria', 'capital': 'Sofia'},
    '3': {'name': 'Canada', 'capital': 'Ottawa'},
    '4': {'name': 'Fiji', 'capital': 'Suva'},
    '5': {'name': 'Germany', 'capital': 'Berlin'},
}

# GET method is used to request data from a specified resource
# POST method is used to send data to a server to create/update a resource

parser = reqparse.RequestParser()

class CountriesList(Resource):
    def get(self):
        return COUNTRIES

    def post(self):
        parser.add_argument('name')
        parser.add_argument('capital')
        args = parser.parse_args()
        new_country_id = int(max(COUNTRIES.keys())) + 1
        new_country_id = '%i' % new_country_id
        COUNTRIES[new_country_id] = {
            'name': args['name'],
            'capital': args['capital']
        }
        return COUNTRIES[new_country_id], 201 # 201 is HTTP status code that indicates that request has been fulfilled and has resulted in one or more resources being created 

class Country(Resource):
    def get(self, country_id):
        if country_id not in COUNTRIES:
            return 'Not found', 404
        else:
            return COUNTRIES[country_id]

    def put(self, country_id):
        parser.add_argument('name')
        parser.add_argument('capital')
        args = parser.parse_args()
        if country_id not in COUNTRIES:
            return 'Record not found', 404
        else:
            country = COUNTRIES[country_id]
            country['name'] = args['name'] if args['name'] is not None else country['name']
            country['capital'] = args['capital'] if args['capital'] is not None else country['capital']
            return country, 200

    def delete(self, country_id):
        if country_id not in COUNTRIES:
            return 'Not found', 404
        else:
            del COUNTRIES[country_id]
            return '', 204


# Adding a route
api.add_resource(CountriesList, '/countries')

# Adding a second route
api.add_resource(Country, '/countries/<country_id>')

# GET, PUT, POST and DELETE methods used in Postman to perform CRUD operations
