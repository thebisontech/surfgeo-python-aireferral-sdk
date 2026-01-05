from wsgiref.simple_server import make_server
from surfgeo.middleware.wsgi import surfgeoWSGIMiddleware
import os


def application(environ, start_response):
    """Simple WSGI application"""
    path = environ.get('PATH_INFO', '/')
    
    if path == '/':
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [b'Hello World']
    elif path == '/api/test':
        start_response('200 OK', [('Content-Type', 'application/json')])
        return [b'{"message": "API endpoint"}']
    else:
        start_response('404 Not Found', [('Content-Type', 'text/plain')])
        return [b'Not Found']


# Wrap with surfgeo middleware
app = surfgeoWSGIMiddleware(
    application,
    script_key=os.environ.get('SURFGEO_SCRIPT_KEY', 'sk_your_key_here')
)

if __name__ == '__main__':
    server = make_server('', 8000, app)
    print('Server running on http://localhost:8000')
    server.serve_forever()

