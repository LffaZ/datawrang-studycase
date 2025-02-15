import json
from flask import Flask, jsonify, request

app = Flask(__name__)
data = {"data": [{
    "author_id": "2244994945",
    "created_at": "Wed Jan 06 18:40:40 +0000 2021",
    "id": "1346889436626259968",
    "text": "Learn how to use the user Tweet timeline, and user mention timeline endpoints in the X API v2 to explore Tweet https://t.co/56a0vZUx7i",
    "username": "XDevelopers"
}]}

@app.route('/', methods=['GET'])
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=8080)