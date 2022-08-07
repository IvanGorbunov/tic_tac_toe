from starlette.websockets import WebSocket


class Player:

    def __init__(self, ws: WebSocket, state: str = 'X') -> None:
        self.ws = ws
        self.__state = state

    async def get_state(self):
        return self.get_state()


class Game:

    players = []
    current_player = ''
    active_game = False

    @classmethod
    async def create(cls, ws: WebSocket):
        self = cls()
        player = await self.create_player(ws)
        self.players.append(player)
        self.current_player = await player.get_state()
        return self

    async def create_player(self, ws: WebSocket):
        return Player(ws, 'X')




