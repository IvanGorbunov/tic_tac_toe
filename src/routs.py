from starlette.routing import Route

from .endpoints import HomePage

routes = [
    Route('/', HomePage)
]


