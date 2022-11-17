from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def HelloPage(name: str, message: str):
    return f'Hello, {name}! {message}!'
