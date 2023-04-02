import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader
from neureal.routers import draw_router
from neureal.utils import aws, check

app = FastAPI()
app.mount("/static", StaticFiles(directory="neureal/static"), name="static")
# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('neureal/templates'))

# Define a route that renders a template
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    images = check.check_dir()
    if not images:
        aws.get_bucket_images()
    template = env.get_template('index.html')
    content = template.render(title="Neureal Tarot")
    return HTMLResponse(content=content)

app.include_router(draw_router.router)

# if __name__ == "__main__":
#     uvicorn.run(app)
