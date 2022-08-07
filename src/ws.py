import typing

from starlette.endpoints import WebSocketEndpoint
from starlette.websockets import WebSocket


class WSGame(WebSocketEndpoint):

    async def on_connect(self, websocket: WebSocket) -> None:
        await websocket.accept()


    async def on_receive(self, websocket: WebSocket, data: typing.Any) -> None:
        pass

