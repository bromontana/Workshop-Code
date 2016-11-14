var ready = 0;
//var Publisher = require('cote').Publisher;
var Publisher = require('cote')({'broadcast': '10.0.255.255'}).Publisher;
var express = require('express');
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var coteList = [];
app.use(express.static('public'));

// Instantiate a new Publisher component. 
var randomPublisher = new Publisher({
    name: 'webServer', 
    broadcasts: ['robot']
});

// Wait for the publisher to find an open port and listen on it. 
randomPublisher.on('ready', function() {
    ready = 1;
});

app.get('/', function(req, res){
  res.sendfile('index.html');
});

io.on('connection', function(socket){
  console.log('a user connected');
  socket.on('message', function(msg,socket){
	let bot = "drive"+msg.bot;
	if(isOnline(msg.bot,socket)==1){
	  io.emit('message', { online : '1' });	
	}
	else{
	  io.emit('message', { online : '0' });	
	}
	console.log("Command : "+msg.command+"("+bot+")");
	if(ready = 1){
	randomPublisher.publish(bot, msg.command);
	}
   });
});

http.listen(3000, function(){
  console.log('listening on *:3000');
});

function isOnline(bot,socket){
	for (i = 0; i < coteList.length; i++) { 
    		if(coteList[i]==bot){ return 1;}
	}
	return 0;
}

function coteMembers() {
    setTimeout(function () {
        var ids = Object.keys(randomPublisher.discovery.nodes);
	coteList = [];
	let status = 0;
	for (i = 0; i < ids.length; i++) { 
    		coteList.push(randomPublisher.discovery.nodes[ids[i]].advertisement.name);
	}
        coteMembers();
    }, 500);
}

coteMembers();
