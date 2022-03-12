from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

class HandleRequests(Resource):
    def get(self):
        return {"data": "Hello World"}

api.add_resource(HandleRequests, "/")


if __name__ == "__main__":
    app.run(debug=True)

