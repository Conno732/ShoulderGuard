from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)
class HandleRequests(Resource):
    def get(self):
        return {"data": "sda"}
    def post(self):
        jsonData = request.get_json(force=True)
        pictureData = jsonData['picture']
        return {"data":"recieved"}

api.add_resource(HandleRequests, "/")


if __name__ == "__main__":
    app.run(debug=True)

