from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.api import infrastructure
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

ALLOWED_ORIGINS = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
]

app = FastAPI(
    title='Underground Infrastructure Viewer',
    description='REST API serving geospatial infrastructure data',
    version='0.1.0'
)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error("Unhandled exception on %s: %s", request.url, exc, exc_info=True)
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=False,
    allow_methods=['GET'],
    allow_headers=['*'],
)

app.include_router(infrastructure.router, prefix="/api")

@app.get('/')
def root():
    return {'status': 'ok', 'message': 'Underground Infrastructure Viewer API'}

@app.get('/health')
def health():
    return {'status': 'healthy'}