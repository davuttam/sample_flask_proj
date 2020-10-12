from flask import request
from flask_api import FlaskAPI

app = FlaskAPI(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return {
            'hello': 'world'
        }
    return {
        'hello': str(request.data.get('name', ''))
    }
