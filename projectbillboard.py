from flask import Flask, request, render_template
from flask_restful import Api, Resource
from flask_jsonpify import jsonify
from flask_cors import CORS
from submodules.predictor import predict_popularity

app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('test.html')

class Prediction(Resource):
    def get(self, songname):
        popularity = predict_popularity(songname)
        return {"popularity": popularity}

class haha(Resource):
    def get(self):
        return {"hehe":"hoho"}

api.add_resource(Prediction, '/predict/<songname>')
api.add_resource(haha, '/laugh')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
