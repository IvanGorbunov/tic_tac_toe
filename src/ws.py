import typing

from starlette.endpoints import WebSocketEndpoint
from starlette.websockets import WebSocket
from .game import Game


class GameActions:
    """
    Type of action
    """
    CREATE = 'create'
    NEW = 'new'
    JOIN = 'join'

    ITEMS = (
        'create',
        'new',
        'join',
    )

    CHOICES = (
        (CREATE, 'create'),
        (NEW, 'new'),
        (JOIN, 'join'),
    )


class WSGame(WebSocketEndpoint):
    encoding = 'json'
    games = []
    current_games = []

    async def create_game(self, ws: WebSocket) -> None:
        game = await Game.create(ws)
        self.games.append(game)

    async def join_game(self, ws: WebSocket, number: int) -> Game:
        game = self.games.pop(number - 1)
        self.current_games.append(game)
        await game.join_player(ws)
        return game

    async def on_connect(self, websocket: WebSocket) -> None:
        await websocket.accept()

    async def on_receive(self, websocket: WebSocket, data: typing.Any) -> None:
        if data['action'] in GameActions.ITEMS:
            if data['action'] == GameActions.NEW:
                content = {
                    'action': GameActions.NEW,
                    'games': len(self.games)
                }
                await websocket.send_json(content)

            elif data['action'] == GameActions.CREATE:
                await self.create_game(websocket)
                await websocket.send_json({'action': GameActions.CREATE})

            elif data['action'] == GameActions.JOIN:
                game = await self.join_game(websocket, int(data['game']))
                await websocket.send_json(
                    {
                        'action': GameActions.JOIN,
                        'other_player': await game.player_1.get_state(),
                        'player': await game.player_2.get_state(),
                    }
                )

                ws = await game.player_1.get_ws()
                await ws.send_json(
                    {
                        'action': GameActions.JOIN,
                        'other_player': await game.player_2.get_state(),
                        'player': await game.player_1.get_state(),
                    }
                )



    async def on_disconnect(self, websocket: WebSocket, close_code: int) -> None:
        pass

