from flask import Flask, jsonify
from flask_cors import CORS
from google.cloud import firestore


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
db = firestore.Client()


# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sample route
@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify('hi world!')


if __name__ == '__main__':
    app.run()
