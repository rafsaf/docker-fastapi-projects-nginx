from fastapi import FastAPI

my_fastapi_app = FastAPI()


@my_fastapi_app.get("/")
async def root():
    return {"Nginx": "I'm alive"}