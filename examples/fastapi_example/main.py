import os
from fastapi import FastAPI
from surfgeo.middleware.fastapi import surfgeoMiddleware

app = FastAPI()

# Add surfgeo middleware
app.add_middleware(
    surfgeoMiddleware,
    script_key=os.environ.get('surfgeo_SCRIPT_KEY'),
    debug=True
)


@app.get("/")
async def root():
    return {"message": "Hello from FastAPI"}


@app.get("/api/users")
async def users():
    return {"users": []}

