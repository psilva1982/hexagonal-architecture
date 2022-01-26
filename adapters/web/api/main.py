
from fastapi.exceptions import HTTPException
from fastapi import FastAPI, Depends
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response
from starlette.status import HTTP_401_UNAUTHORIZED
from routes.router import router

app = FastAPI(title="Hexagonal Architecture", description='Ports and Adapters Sample', version='0.0.1')
app.include_router(router)
