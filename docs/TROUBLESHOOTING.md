# Troubleshooting

Common issues and solutions when using the surfgeo Python SDK.

## Import Errors

### "No module named 'surfgeo'"

Install the package: `pip install surfgeo`

### "No module named 'django'"

Install with Django support: `pip install surfgeo[django]`

## Tracking Not Working

### Check script_key

Ensure script_key is correct and starts with `sk_`

### Enable debug mode

```python
surfgeo_CONFIG = {
    'script_key': 'sk_your_key',
    'debug': True  # See errors in console
}
```

### Check endpoint accessibility

Verify your server can reach the tracking endpoint

## Performance Issues

### Tracking is blocking requests

This shouldn't happen - check implementation

### Too many threads

SDK uses fire-and-forget threads (one per request)

## Framework-Specific Issues

### Django: Middleware not running

Check MIDDLEWARE order in settings.py

### Flask: Extension not initialized

Ensure you called `init_app` or passed app to constructor

### FastAPI: Async issues

Verify you're using `track_async` for async frameworks

