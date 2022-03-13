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
        data = request.data
        print(request.method)
        print(request.args.values())
        return {"data":"recieved"}

api.add_resource(HandleRequests, "/")


if __name__ == "__main__":
    app.run(debug=True)

