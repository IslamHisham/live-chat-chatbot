from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/order', methods=['GET', 'POST'])
def login():
    server_token = "sulumelprinceYN@hop8"
    challenge = request.args.get('challenge')
    token = request.args.get('token')

    if not token or server_token != token:
        return jsonify({'message': 'Token is invalid!'}), 403
    # the bot expects to see an array of objects called response 'bot response' of type 'text'
    return challenge


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7777, debug=True)
