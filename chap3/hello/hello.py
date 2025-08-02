from fastapi import FastAPI, Body, Header

app = FastAPI()

@app.get("/hi")
def greet():
    return "Hello? World?"

# path variable
@app.get("/hi/{who}")
def greet2(who):
    return f"Hello? {who}?"

# request parameter
@app.get("/hi3")
def greet3(who):
    return f"Hello? {who}?"

# request body
@app.post("/hi")
def greet4(who: str = Body(embed=True)):
    return f"Hello? {who}?"

# request header
@app.get("/hi4")
def greet5(who: str = Header()):
    return f"Hello? {who}?"

# user-agent
@app.get("/agent")
def greet6(user_agent: str = Header()):
    return user_agent

# status code
@app.get("/happy")
def happy(status_code=200):
    return ":)"
