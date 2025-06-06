from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Welcome to FastAPI!"})

@app.get("/predict")
def predict(value: int):
    result = value * 2  # simple logic for demo
    return {"input": value, "output": result}
