import typing

from starlette.endpoints import WebSocketEndpoint
from starlette.websockets import WebSocket
from .game import Game


class WSGame(WebSocketEndpoint):
    encoding = 'json'
    actions = [
        'create',
        'new',
    ]
    games = []

    async def create_game(self, ws: WebSocket) -> None:
        game = await Game.create(ws)
        self.games.append(game)

    async def on_connect(self, websocket: WebSocket) -> None:
        await websocket.accept()

    async def on_receive(self, websocket: WebSocket, data: typing.Any) -> None:
        if data['action'] in self.actions:
            if data['action'] == 'new':
                content = {
                    'action': 'new',
                    'games': len(self.games)
                }
                await websocket.send_json(content)
            elif data['action'] == 'create':
                await self.create_game(websocket)
                await websocket.send_json({'action': 'create'})

