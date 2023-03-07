import time
from fastapi import FastAPI, Request

from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel

app = FastAPI(title="FastAPI Hello World", docs_url="/api/docs", openapi_url="/api")

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


class ResponseModel(BaseModel):
    server_ip: str
    server_port: int
    client_ip: str
    client_port: int
    host: str


@app.get("/whats_my_ip", response_model=ResponseModel)
def whats_my_ip(request: Request):
    print(request["headers"])
    return {
        "server_ip": request["server"][0],
        "server_port": request["server"][1],
        "client_ip": request["client"][0],
        "client_port": request["client"][1],
        "host": request["headers"][0][1],
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=80, workers=2)
