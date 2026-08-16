import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path

BASE_DIR: Path = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")

app = FastAPI()

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

@app.get('/', response_class=HTMLResponse)
async def index(request : Request):
    
    context = {
        'page_name': "Главная"
    }
    
    return templates.TemplateResponse(request=request, name="index.html", context=context)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
