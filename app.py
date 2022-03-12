from urllib import request
from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)
parser = reqparse.RequestParser()
parser.add_argument('data')
class HandleRequests(Resource):
    def get(self):
        return {"data": "sda"}
    def post(self):
        
        return {"data": "asdsad"}

api.add_resource(HandleRequests, "/")


if __name__ == "__main__":
    app.run(debug=True)

