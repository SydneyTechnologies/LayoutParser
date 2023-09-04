from fastapi import FastAPI, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request


app = FastAPI()

# mounting the static directory 
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# def processDocument(file: UploadFile):

