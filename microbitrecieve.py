from microbit import *
import radio
from pythonosc import osc_message_builder
from pythonosc import udp_client


radio.on()
radio.config(channel=19)        # Choose your own channel number
radio.config(power=7)           # Turn the signal up to full strength


IP = '127.0.0.1'
PORT = 6448
OSC_MESSAGE = "/wek/inputs"

# Event loop.
while True:
        
        incoming = radio.receive()
        
        tokens = incoming.split(", ")
        x=float(tokens[0])
        y=float(tokens[1])
        z=float(tokens[2])
        
    
        
        if incoming is not None:
            
              client = udp_client.SimpleUDPClient()
              client.send_message(OSC_MESSAGE, x)
              client.send_message(OSC_MESSAGE, y)
              client.send_message(OSC_MESSAGE, z)
