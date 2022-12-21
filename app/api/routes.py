from api.endpoint import company
from api.endpoint import product
from fastapi import APIRouter
from fastapi import FastAPI

app = FastAPI(
  title="V1"
)

api_router = APIRouter()

api_router.include_router(company.router)
api_router.include_router(product.router)

app.include_router(api_router)
