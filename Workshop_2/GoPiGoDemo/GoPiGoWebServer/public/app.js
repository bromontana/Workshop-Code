var socket = io();
var active = 0;
var lled = 0;
var rled = 0;
var name = "Sparky";
var status = 0

  socket.on('connect', function () {

	document.getElementById("status").innerHTML = "Socket Status: Connected";
	});
  socket.on('disconnect', function () {
	document.getElementById("status").innerHTML = "Socket Status: Disconnected";
	});

  socket.on('message', function (data) {
	if(data.online){
        	if(data.online!=status){
			         status = data.online;
			         if(status==0){document.getElementById("robotstatus").innerHTML = '<h4 class="center red-text">'+name+' is Offline</h4>';}
               else{document.getElementById("robotstatus").innerHTML = '<h4 class="center green-text">'+name+' is Online</h4>';}
		        }
    }
  });

function toggleLed(e){
	if(e=='l'){
	if(lled==0){socket.emit('message','left led on');lled=1;}
	else{socket.emit('message','left led off');lled=0;}
	}
	else if(e=='r'){
	if(rled==0){socket.emit('message','right led on');rled=1;}
	else{socket.emit('message','right led off');rled=0;}
	}
}

function changeName(){
	let d = prompt("Please enter robot name");
  	sendMessage('x');
	  name = d;
    sendMessage('x');
  	document.getElementById("robo").innerHTML = "Drive "+name;
  	document.getElementById("title").innerHTML = name+" Web Panel";
  	document.getElementById("logo-container").innerHTML = name+" Web Panel";
}
function servoTest(){
	socket.emit('message','servo test');
}

function sendMessage(command){
  let robo = name;
  if(robo!=""){
  var data = {"bot":robo, "command":command};
	socket.emit('message', data);
  }
}
function drivebot(e){
      var evtobj=window.event? event : e; //distinguish between IE's explicit event object (window.event) and Firefox's implicit.
      var unicode=evtobj.charCode? evtobj.charCode : evtobj.keyCode;
      var actualkey=String.fromCharCode(unicode);
  	var data = "Command Sent: "
  	//Forwards
  	if((evtobj.keyCode==119)&&(active!=evtobj.keyCode)){
	    active = 119;
  	    data += "Forward";
  	    sendMessage('w');
  	    document.getElementById("command").innerHTML = data;
  	}
  	//Backwards
  	else if((evtobj.keyCode==115)&&(active!=evtobj.keyCode)){
	    active = 115;
  	    data += "Backward";
  	    sendMessage('s');
		document.getElementById("command").innerHTML = data;
  	}
  	//Left
  	else if((evtobj.keyCode==97)&&(active!=evtobj.keyCode)){
	    active = 97;
  	    data += "Left";
  	    sendMessage('a');
  		document.getElementById("command").innerHTML = data;
  	}
  	//Right
  	else if((evtobj.keyCode==100)&&(active!=evtobj.keyCode)){
            active = 100;
  	    data += "Right";
  	    sendMessage('d');
  		document.getElementById("command").innerHTML = data;
  	}


}

function stopbot(e){
	active = 0;
  	var data = "Command Sent: ";
  	data += "Stop";
  	sendMessage('x');
  	document.getElementById("command").innerHTML = data;
  }

document.onkeypress=drivebot;
document.onkeyup=stopbot;
