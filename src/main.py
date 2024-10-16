from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import Config
from src.modules.bootstrap import bootstrap_di
from src.routers import configure_routers


C = Config()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

bootstrap_di(C)
configure_routers(app)
