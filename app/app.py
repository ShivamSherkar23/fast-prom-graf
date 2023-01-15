import socket
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
hostname = socket.gethostname()

# allow http metrics to be scraped
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)

# this will run before application start
@app.on_event("startup")
async def startup():
    Instrumentator().instrument(app).expose(app)

# main application route
@app.get("/")
def read_root():
    return f"hello from {hostname}"