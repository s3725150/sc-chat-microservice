from flask import Flask, jsonify, request
from flask_cors import CORS
from google.cloud import firestore

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# Firestore init
# instantiate client
db = firestore.Client.from_service_account_json('cc-steam-chat-47d8cdf25925.json')

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# Main chatRoom route
@app.route('/chatRoom', methods=['POST'])
def add_chatRoom():
    appId = request.form.get("appId")
    doc_ref = db.collection('chatRooms').document(appId)
    doc_ref.set({
        'Game Name': request.form.get("gameName")
    })




if __name__ == '__main__':
    app.run()
