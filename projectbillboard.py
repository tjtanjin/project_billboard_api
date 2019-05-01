from flask import Flask
from flask_restful import Api, Resource, request
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello():
    return "Test"

class Prediction(Resource):
    def get(self):
        args = request.args #retrieve args from query string
        return args

class haha(Resource):
    def get(self):
        return {"hehe":"hoho"}

api.add_resource(Prediction, '/predict')
api.add_resource(haha, '/laugh')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
