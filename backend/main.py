from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import infrastructure

app = FastAPI(
    title='Underground Infrastructure Viewer',
    description='REST API serving geospatial infrastructure data',
    version='0.1.0'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(infrastructure.router, prefix="/api")

@app.get('/')
def root():
    return {'status': 'ok', 'message': 'Underground Infrastructure Viewer API'}

@app.get('/health')
def health():
    return {'status': 'healthy'}