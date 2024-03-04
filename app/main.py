from fastapi import FastAPI

app_test = FastAPI()

@app_test.get("/")
def homepage():
    return {"message": "Hello fastapi bro!"}