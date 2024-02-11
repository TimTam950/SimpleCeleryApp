from fastapi import FastAPI

from app.tasks.tasks import add

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/add")
def add_handler():
    result = add.delay(4, 4)
    return result.id
