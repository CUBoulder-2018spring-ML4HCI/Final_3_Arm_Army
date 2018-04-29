var osc = require("osc")

var udpPort = new osc.UDPPort({
  localAddress: "127.0.0.1",
  localPort: 8081,

  remoteAddress: "127.0.0.1",
  remotePort: 57120,
  metadata: true
})
udpPort.open()


// var oscPort = new osc.WebSocketPort({
//     url: "ws://localhost:8081", // URL to your Web Socket server.
//     metadata: true
// });
//
// oscPort.open()

udpPort.on("ready", function () {
    udpPort.send({
        address: "/wek/inputs",
        args: [
            {
                type: "f",
                value: Math.random()
            }
        ]
    });
});
