from fastapi import FastAPI, APIRouter
from router.router import sms

app = FastAPI()
app.include_router(sms)

routes_product = APIRouter()
fake_db = []
