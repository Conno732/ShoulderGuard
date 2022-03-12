from urllib import request
from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)
class HandleRequests(Resource):
    def get(self):
        return {"data": "sda"}
    def post(self):
        reqData = request.get_json()
        return reqData

api.add_resource(HandleRequests, "/")


if __name__ == "__main__":
    app.run(debug=True)

