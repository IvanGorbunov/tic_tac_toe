const ws = new WebSocket('ws://localhost:8000/ws')
let iPlayer
let otherPlayer


ws.onopen = function (event){
    console.log(event)
    newUser()
}

ws.onmessage = function (event){
    console.log(event)
    let data = JSON.parse(event.data)
    switch (data.action){
        case 'new' :
            gameList(data.games)
            break
        case 'join' :
            startGame(data.action, data.player, data.other_player)
            break
        default:
            break
    }
}

function send(data){
    ws.send(JSON.stringify(data))
}

function newUser(){
    send({action: 'new'})
}

function createGame(event){
    send({action: 'create'})
}

function joinGame(event){
    let btn = event.target
    send({action: 'join', game: btn.id})
}

function startGame(action, player, other_player){
    iPlayer = player
    otherPlayer = other_player

    document.getElementById('game').className = 'game-off'
    let state = document.getElementById('player')
    state.className = 'game-on'
    state.innerHTML = `You are player ${iPlayer}`
}

function gameList(game) {
    let i = 1
    while (i <= game){
        let gameList = document.getElementById('gameList')
        let li = document.createElement('li')
        let text = document.createTextNode(`Game ${i}    `)
        let btn = document.createElement('button')
        btn.id = `${i}`
        btn.innerHTML = 'Connect'
        btn.addEventListener('click', joinGame)
        li.appendChild(text)
        li.appendChild(btn)
        gameList.appendChild(li)
        i++
    }
}





document.getElementById('create-game').addEventListener('click', createGame)

