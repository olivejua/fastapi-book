from fastapi import FastAPI, Response

app = FastAPI()

# response header
@app.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response):
    response.headers[name] = value
    return "normal body"

