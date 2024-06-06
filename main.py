from fastapi import FastAPI
import uvicorn

from routers import router

app = FastAPI()
app.include_router(router=router)

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)