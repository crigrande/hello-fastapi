from fastapi import FastAPI
from starlette.responses import JSONResponse


app = FastAPI()


@app.get("/{name}")
async def welcome(name: str) -> dict:
    return JSONResponse({"detail": f"Welcome, {name.capitalize()}"})
