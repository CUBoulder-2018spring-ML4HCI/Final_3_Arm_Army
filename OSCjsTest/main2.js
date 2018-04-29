var OSC = require("osc-js")
var dgram = require("dgram")

const osc = new OSC()
const socket = dgram.createSocket('udp4')

osc.open({ port: 57120 })
const message = new OSC.Message('/wek/inputs', 100.02)
osc.send(message)
osc.close()
