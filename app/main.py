from api import app as v1
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.mount(path="/v1", app=v1, name="v1")

# app.mount(path=settings.API_V1_STR, app=app_v1, name="v1")
# app.mount(path=settings.API_V2_STR, app=app_v2, name="v2")

@app.get("/")
async def read_root():
    return "OK"


# import sys

# from fastapi import FastAPI

# version = f"{sys.version_info.major}.{sys.version_info.minor}"

# app = FastAPI()


# @app.get("/")
# async def read_root():
#     message = f"Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python {version}"
#     return {"message": message}



