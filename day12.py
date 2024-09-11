from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route

def homepage(request):
    return HTMLResponse ('<h1>hello friend</>')

def aboutpage(request):
    return HTMLResponse ('<h1>aboutpage</>')
def contactpage(request):
    return HTMLResponse('<h1>contactpage</>')

app=Starlette(debug=True,routes=[
    Route('/', homepage),
    Route('/about', aboutpage),
    Route('/contact',contactpage),
])