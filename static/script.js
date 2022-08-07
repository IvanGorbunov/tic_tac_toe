const ws = new WebSocket('ws://localhost:8000/ws')

ws.onopen = function (event){
    console.log(event)
}

ws.onmessage = function (event){
    console.log(event)
}

function send(data){
    ws.send(JSON.stringify(data))
}

function createGame(event){
    send({action: 'create'})
}

document.getElementById('create-game').addEventListener('click', createGame)

