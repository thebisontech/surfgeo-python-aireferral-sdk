import os
from flask import Flask, jsonify
from surfgeo import get_flask_extension

app = Flask(__name__)
app.config['SURFGEO_SCRIPT_KEY'] = os.environ.get('SURFGEO_SCRIPT_KEY')

# Initialize surfgeo
SurfGeo = get_flask_extension()
surfgeo = SurfGeo(app)


@app.route('/')
def home():
    return jsonify(message='Hello from Flask')


@app.route('/api/users')
def users():
    return jsonify(users=[])


if __name__ == '__main__':
    app.run(debug=True)

