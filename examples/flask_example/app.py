import os
from flask import Flask, jsonify
from surfgeo import get_flask_extension

app = Flask(__name__)
app.config['surfgeo_SCRIPT_KEY'] = os.environ.get('surfgeo_SCRIPT_KEY')

# Initialize surfgeo
surfgeo = get_flask_extension()
surfgeo = surfgeo(app)


@app.route('/')
def home():
    return jsonify(message='Hello from Flask')


@app.route('/api/users')
def users():
    return jsonify(users=[])


if __name__ == '__main__':
    app.run(debug=True)

