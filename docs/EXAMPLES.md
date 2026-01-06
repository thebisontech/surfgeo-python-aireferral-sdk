# Examples Guide

Complete examples for using the surfgeo Python SDK with various frameworks.

## Django

### Basic Setup

```python
# settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # ... other middleware
    'surfgeo.middleware.django.surfgeoMiddleware',
]

surfgeo_CONFIG = {
    'script_key': os.environ.get('surfgeo_SCRIPT_KEY'),
    'debug': DEBUG,
    'enabled': not DEBUG
}
```

## Flask

### Direct Initialization

```python
from flask import Flask
from surfgeo import get_flask_extension

app = Flask(__name__)
app.config['surfgeo_SCRIPT_KEY'] = os.environ.get('surfgeo_SCRIPT_KEY')

surfgeo = get_flask_extension()
surfgeo = surfgeo(app)
```

### Factory Pattern

```python
from flask import Flask
from surfgeo import get_flask_extension

surfgeo = get_flask_extension()()

def create_app():
    app = Flask(__name__)
    app.config['surfgeo_SCRIPT_KEY'] = os.environ.get('surfgeo_SCRIPT_KEY')
    surfgeo.init_app(app)
    return app
```

## FastAPI

### Basic Setup

```python
from fastapi import FastAPI
from surfgeo.middleware.fastapi import surfgeoMiddleware

app = FastAPI()

app.add_middleware(
    surfgeoMiddleware,
    script_key=os.environ.get('surfgeo_SCRIPT_KEY'),
    debug=True
)

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

## Generic WSGI

```python
from wsgiref.simple_server import make_server
from surfgeo.middleware.wsgi import surfgeoWSGIMiddleware

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b'Hello World']

app = surfgeoWSGIMiddleware(application, script_key='sk_your_key')

server = make_server('', 8000, app)
server.serve_forever()
```

## Generic ASGI

```python
from starlette.applications import Starlette
from surfgeo.middleware.asgi import surfgeoASGIMiddleware

async def app(scope, receive, send):
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [[b'content-type', b'text/plain']],
    })
    await send({
        'type': 'http.response.body',
        'body': b'Hello World',
    })

app = surfgeoASGIMiddleware(app, script_key='sk_your_key')
```

