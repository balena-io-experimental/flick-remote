from flick import flicklib
import time
import requests
import os


# Attempt an http request to the endpoint specified by configuration and direction
def process(gesture, direction):
	print 'INFO: %s %s' % (gesture, direction)
	try:
		requests.get(os.environ[direction])
	except (KeyError, requests.ConnectionError) as error:
		print 'WARN: ', error


# Attempt to advertise a particular gesture and endpoint
def advertise(action, variable):
	try:
		print 'INFO:   %s - %s' % (action, os.environ[variable])
	except KeyError:
		pass


# Register handlers for some events provided by the Flick library
@flicklib.flick()
def flick(start, finish):
	process('Flicked', finish)


@flicklib.airwheel()
def wheel(delta):
	process('Wheeled', 'clockwise' if delta > 0 else 'anticlockwise')


# Advertise the gestures and their endpoints
print 'INFO: Actions are:'
advertise('Flick South', 'south')
advertise('Flick West', 'west')
advertise('Flick North', 'north')
advertise('Flick East', 'east')
advertise('Wheel Clockwise', 'clockwise')
advertise('Wheel Anti-Clockwise', 'anticlockwise')


# Keep the process ticking
while True:
	time.sleep(60)
