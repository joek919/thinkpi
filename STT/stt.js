var TJBot = require('tjbot');
var config = require('./config');

// obtain our credentials from config.js
var credentials = config.credentials;

// these are the hardware capabilities that our TJ needs for this recipe
var hardware = ['microphone'];

// set up TJBot's configuration
var tjConfig = { 
    log: { level: 'error'},
    listen: {
        //microphoneDeviceId: "plughw:1,0", // plugged-in USB card 1, device 0; see arecord -l for a list of recording devices
        //inactivityTimeout: 10, // -1 to never timeout or break the connection. Set this to a value in seconds e.g 120 to end connection after 120 seconds of silence
        language: 'en-US' // see TJBot.prototype.languages.listen
    }};

// instantiate our TJBot!
var tj = new TJBot(hardware, tjConfig, credentials);

//
console.log("speak to me");

// listen for speech
tj.listen(function(msg) {
   console.log("["+msg+"]");
   if( msg == 'exit ' )
      tj.stopListening();
});

