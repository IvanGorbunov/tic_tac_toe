const ws = new WebSocket('ws://localhost:8000/ws')

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

function gameList(game) {
    let i = 1
    while (i <= game){
        let gameList = document.getElementById('gameList')
        let li = document.createElement('li')
        let text = document.createTextNode(`Game ${i}    `)
        let btn = document.createElement('button')
        btn.id = `${i}`
        btn.innerHTML = 'Connect'

        li.appendChild(text)
        li.appendChild(btn)
        gameList.appendChild(li)
        i++
    }
}





document.getElementById('create-game').addEventListener('click', createGame)

