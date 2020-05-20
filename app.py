from flask import Flask, jsonify, request
from flask_cors import CORS
from google.cloud import firestore
import time

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)

app.config.from_object(__name__)

# Firestore init
# instantiate client
db = firestore.Client.from_service_account_json('cc-steam-chat-47d8cdf25925.json')

# enable CORS
CORS(app)
cors = CORS(app, resources={r'/*': {'origins': '*'}})


# Main chatRoom route
@app.route('/add_chatRoom', methods=['POST'])
def add_chatRoom():
    appId = request.form.get("appId")
    doc_ref = db.collection('chatRooms').document(appId)
    doc_ref.set({
        'Game Name': request.form.get("gameName")
    })
    return jsonify({'test': 'no change'})


# add message to database
@app.route('/sendMessage', methods=['POST'])
def sendMessage():
    appId = request.form.get("appId")
    steamId = request.form.get("steamId")
    message = request.form.get("message")
    room_ref = db.collection('chatRooms').document(appId)
    ts = str(int(time.time()))
    message_ref = room_ref.collection('messages').document(ts)
    message_ref.set({
        'SteamId': steamId,
        'message': message,
        'timestamp': ts,
        'displayTime': firestore.SERVER_TIMESTAMP
    })
    return jsonify({'test': 'no change'})

if __name__ == '__main__':
    app.run()



