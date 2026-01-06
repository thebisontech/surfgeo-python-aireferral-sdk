# API Reference

Complete API documentation for the surfgeo Python SDK.

## Core Client

### `surfgeoClient`

The core tracking client class.

#### Constructor

```python
from surfgeo import surfgeoClient, surfgeoConfig

config = surfgeoConfig(
    script_key='sk_your_key_here',
    endpoint=None,  # Optional
    timeout=0.05,   # Optional, default 50ms
    debug=False,    # Optional
    enabled=True    # Optional
)

client = surfgeoClient(config)
```

#### Methods

##### `track(payload: dict) -> None`

Sends a tracking event to the surfgeo API (synchronous, non-blocking).

**Parameters:**
- `payload` (dict): Tracking payload object

**Returns:**
- `None`: Returns immediately (fire-and-forget)

**Example:**
```python
client.track({
    'timestamp': int(time.time()),
    'path': '/api/users',
    'method': 'GET',
    'user_agent': 'Mozilla/5.0',
    'status_code': 200
})
```

##### `track_async(payload: dict) -> None`

Sends a tracking event asynchronously (for async frameworks).

**Parameters:**
- `payload` (dict): Tracking payload object

**Returns:**
- `None`: Returns immediately (fire-and-forget)

**Example:**
```python
await client.track_async({
    'timestamp': int(time.time()),
    'path': '/api/users',
    'method': 'GET',
    'user_agent': 'Mozilla/5.0',
    'status_code': 200
})
```

## Django Middleware

### `surfgeoMiddleware`

Django middleware for tracking requests.

**Usage:**
```python
# settings.py
MIDDLEWARE = [
    'surfgeo.middleware.django.surfgeoMiddleware',
]

surfgeo_CONFIG = {
    'script_key': 'sk_your_key_here'
}
```

## Flask Extension

### `surfgeo`

Flask extension for tracking requests.

**Usage:**
```python
from surfgeo import get_flask_extension

surfgeo = get_flask_extension()
surfgeo = surfgeo(app, script_key='sk_your_key_here')
```

## FastAPI Middleware

### `surfgeoMiddleware`

FastAPI/Starlette middleware for tracking requests.

**Usage:**
```python
from surfgeo.middleware.fastapi import surfgeoMiddleware

app.add_middleware(
    surfgeoMiddleware,
    script_key='sk_your_key_here'
)
```

## Types

### `surfgeoConfig`

Configuration dataclass.

```python
@dataclass
class surfgeoConfig:
    script_key: str
    endpoint: Optional[str] = None
    timeout: float = 0.05
    debug: bool = False
    enabled: bool = True
```

### `TrackingPayload`

Tracking payload type.

```python
class TrackingPayload(TypedDict, total=False):
    timestamp: int
    path: str
    method: str
    status_code: Optional[int]
    user_agent: str
    referrer: Optional[str]
    headers: Optional[Dict[str, str]]
    request_id: Optional[str]
    script_key: Optional[str]
    source: Optional[str]
```

