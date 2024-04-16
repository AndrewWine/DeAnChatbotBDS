from flask import Flask, request, jsonify

from main import chatWithBot

app = Flask(__name__)


@app.route('/chat/', methods=['GET', 'POST'])
def chatBot():
    Message = request.json['Message']
    return jsonify(chatBotReply=chatWithBot(Message))


if __name__ == '__main__':
    app.run()
