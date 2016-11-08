var Gopigo   = require('./libs').Gopigo;
var Commands = Gopigo.commands;
var Robot = Gopigo.robot;
var robot;
var ready = 0;
var readline = require('readline');

var express = require('express');
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);
app.use(express.static('public'));

//var Subscriber = require('cote').Subscriber;
//Initialize Batman Subscriber using correct subnet
var Subscriber = require('cote')({'broadcast':'10.0.255.255'}).Subscriber;
var channels = ['driveJames'];

var ultrasonicPin = 15;
//var irreceiverPin = 8

var rl = readline.createInterface({
  input : process.stdin,
  output: process.stdout
});

robot = new Robot({
  minVoltage: 5.5,
  criticalVoltage: 1.2,
  debug: true,
  ultrasonicSensorPin: ultrasonicPin,
  //IRReceiverSensorPin: irreceiverPin
})
robot.on('init', function onInit(res) {
  if (res) {
    console.log('GoPiGo Ready!')
    ready = 1;
  } else {
    console.log('Something went wrong during the init.')
  }
})
robot.on('error', function onError(err) {
  console.log('Something went wrong')
  console.log(err)
})
robot.on('free', function onFree() {
  console.log('GoPiGo is free to go')
})
robot.on('halt', function onHalt() {
  console.log('GoPiGo is halted')
})
robot.on('close', function onClose() {
  console.log('GoPiGo is going to sleep')
})
robot.on('reset', function onReset() {
  console.log('GoPiGo is resetting')
})
robot.on('normalVoltage', function onNormalVoltage(voltage) {
  console.log('Voltage is ok ['+voltage+']')
})
robot.on('lowVoltage', function onLowVoltage(voltage) {
  console.log('(!!) Voltage is low ['+voltage+']')
})
robot.on('criticalVoltage', function onCriticalVoltage(voltage) {
  console.log('(!!!) Voltage is critical ['+voltage+']')
})
robot.init()

function handleAnswer(answer) {
  var message = ''
  switch (answer) {
    case 'reset':
      robot.reset()
    break
    case 'left led on':
      var res = robot.ledLeft.on()
      console.log('Left led on::'+res)
    break
    case 'left led off':
      var res = robot.ledLeft.off()
      console.log('Left led off::'+res)
    break
    case 'right led on':
      var res = robot.ledRight.on()
      console.log('Right led on::'+res)
    break
    case 'right led off':
      var res = robot.ledRight.off()
      console.log('Right led off::'+res)
    break
    case 'w':
      var res = robot.motion.forward(false)
      console.log('Moving forward::' + res)
    break
    case 'a':
      var res = robot.motion.left()
      console.log('Turning left::' + res)
    break
    case 'd':
      var res = robot.motion.right()
      console.log('Turning right::' + res)
    break
    case 's':
      var res = robot.motion.backward(false)
      console.log('Moving backward::' + res)
    break
    case 'stop':
    case 'x':
      var res = robot.motion.stop()
      console.log('Stop::' + res)
    break
    case 'increase speed':
    case 't':
      var res = robot.motion.increaseSpeed()
      console.log('Increasing speed::' + res)
    break
    case 'decrease speed':
    case 'g':
      var res = robot.motion.decreaseSpeed()
      console.log('Decreasing speed::' + res)
    break
    case 'voltage':
    case 'v':
      var res = robot.board.getVoltage()
      console.log('Voltage::' + res + ' V')
    break
    case 'servo test':
    case 'b':
      robot.servo.move(0)
      console.log('Servo in position 0')

      robot.board.wait(1000)
      robot.servo.move(180)
      console.log('Servo in position 180')

      robot.board.wait(1000)
      robot.servo.move(90)
      console.log('Servo in position 90')
    break
    case 'ultrasonic distance':
    case 'u':
      var res = robot.ultraSonicSensor.getDistance()
      console.log('Ultrasonic Distance::' + res + ' cm')
    break
    case 'ir receive':
      var res = robot.IRReceiverSensor.read()
      console.log('IR Receiver data::')
      console.log(res)
    break
    case 'l':
      // TODO
    break
    case 'move forward with pid':
    case 'i':
      var res = robot.motion.forward(true)
      console.log('Moving forward::' + res)
    break
    case 'move backward with pid':
    case 'k':
      var res = robot.motion.backward(true)
      console.log('Moving backward::' + res)
    break
    case 'rotate left':
    case 'n':
      var res = robot.motion.leftWithRotation()
      console.log('Rotating left::' + res)
    break
    case 'rotate right':
    case 'm':
      var res = robot.motion.rightWithRotation()
      console.log('Rotating right::' + res)
    break
    case 'set encoder targeting':
    case 'y':
      var res = robot.encoders.targeting(1, 1, 18)
      console.log('Setting encoder targeting:1:1:18::' + res)
    break
  }
  ready = 1;
}

var batSubscriber = new Subscriber({
    name: 'James',
    subscribesTo: channels
});

batSubscriber.on('**', function(req) {
	if(ready = 1){
	ready = 0;
	handleAnswer(req);
	}
});

function checkStatus() {
    setTimeout(function () {
        var ids = Object.keys(batSubscriber.discovery.nodes);
	var coteList = [];
	let status = 0;
	for (i = 0; i < ids.length; i++) { 
    		coteList.push(batSubscriber.discovery.nodes[ids[i]].advertisement.name);
	}
	for (i = 0; i < coteList.length; i++) { 
    		if(coteList[i]=="webServer"){ status = 1; }
	}
	if(status==0){
		if(ready!=0){
		console.log("webServer is offline");
      		var res = robot.motion.stop();
      		console.log('Stop::' + res);
		}
		ready = 0;
	}
	else{
		ready = 1;	
	}
        checkStatus();
    }, 100);
}

checkStatus();







