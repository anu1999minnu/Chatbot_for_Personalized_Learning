from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    response = requests.post('http://localhost:5005/webhooks/rest/webhook', json=data)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(port=5000)
