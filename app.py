from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import face_count

app = Flask(__name__)
api = Api(app)
CORS(app)

class HandleRequests(Resource):
    def get(self):
        return {"data": "sda"}
    def post(self):
        jsonData = request.get_json(force=True)
        pictureData = jsonData['picture']
        single_face = face_count.check_image(pictureData)
        print(single_face)
        return {"data":single_face}

api.add_resource(HandleRequests, "/")


if __name__ == "__main__":
    app.run(debug=True)

