from fastapi import FastAPI

app = FastAPI()

@app.get('/hellopage')
def HelloPage(name: str = 'Rekruto', message: str = 'Давай дружить'):
    return f'Hello, {name}! {message}!'
