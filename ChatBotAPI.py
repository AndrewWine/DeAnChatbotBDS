from flask import Flask, request, jsonify
import json
from main import chatWithBot, preprocess_text

app = Flask(__name__)

@app.route('/chat/', methods=['GET', 'POST'])
def chatBot():
    message = request.json['Message']
    processed_message = preprocess_text(message)
    return jsonify(chatBotReply=chatWithBot(processed_message))

if __name__ == '__main__':
    app.run()
