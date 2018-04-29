var osc = require("node-osc")

for (var i = 0; i < 5; i++) {
  var client = new osc.Client('127.0.0.1', 57120);
  client.send('/wek/inputs', 200.0, function () {
    client.kill();
  });
}
