from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

class HandleRequests(Resource):
    per = 0
    def get(self):
        per += 1
        return {"data": per}
        
    

api.add_resource(HandleRequests, "/")


if __name__ == "__main__":
    app.run(debug=True)

