from typing_extensions import Required
from urllib import request
from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

taskArgs = reqparse.RequestParser()
taskArgs.add_arguement("data", type=str, requiered = True)

class HandleRequests(Resource):
    def get(self):
        return {"data": "sda"}
    def post(self):
        reqData = taskArgs.parse_args()
        return reqData

api.add_resource(HandleRequests, "/")


if __name__ == "__main__":
    app.run(debug=True)

