from fastapi import FastAPI
from app.abc import get_abc
from app.xyz import get_xyz

app = FastAPI()

@app.get("/abc")
def abc_route():
    return get_abc()

@app.get("/xyz")
def xyz_route():
    return get_xyz()
