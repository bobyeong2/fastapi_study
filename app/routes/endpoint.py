import os
from fastapi.responses import HTMLResponse
from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates
from app.library.helpers import openfile
from dotenv import load_dotenv
load_dotenv()

router = APIRouter()

templates = Jinja2Templates(directory="/root/01_study/templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = openfile("home.md")
    return templates.TemplateResponse("page.html", {"request": request, "data": data})
    
@router.get("/page/{page_name}", response_class=HTMLResponse)
async def show_page(request: Request, page_name: str):
    data = openfile(page_name+".md")
    return templates.TemplateResponse("page.html", {"request": request, "data": data})

@router.get("/unsplash", response_class=HTMLResponse)
async def unsplash_home(request: Request):
    key = os.getenv("unsplash_key")
    print(key)
    return templates.TemplateResponse("unsplash.html", {"request": request})

@router.get("/twoforms", response_class=HTMLResponse)
def form_get(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('twoforms.html', context={'request': request, 'result': result})


@router.post("/form1", response_class=HTMLResponse)
def form_post1(request: Request, number: int = Form(...)):
    result = number + 2
    return templates.TemplateResponse('twoforms.html', context={'request': request, 'result': result, 'yournum': number})


@router.post("/form2", response_class=HTMLResponse)
def form_post2(request: Request, number: int = Form(...)):
    result = number + 100
    return templates.TemplateResponse('twoforms.html', context={'request': request, 'result': result, 'yournum': number})

@router.get("/accordion", response_class=HTMLResponse)
def get_accordion(request: Request):
    tag = "flower"
    result = "Type a number"
    return templates.TemplateResponse('accordion.html', context={'request': request, 'result': result, 'tag': tag})


@router.post("/accordion", response_class=HTMLResponse)
def post_accordion(request: Request, tag: str = Form(...)):

    return templates.TemplateResponse('accordion.html', context={'request': request, 'tag': tag})
