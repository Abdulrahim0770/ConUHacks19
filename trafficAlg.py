# Function that gets the number of cars at a certain intersection and the intersection number, and returns 
# a string specifying what intersection gets green.

#Class description
class Road:
	def __init__(self, numCars, trafficLight, waitTime, avgNumCars):
		self.numCars = numCars
		self.trafficLight = trafficLight
		self.waitTime = waitTime
		self.avgNumCars = avgNumCars

# Global variables
intersection = {}

# Algorithm that checks if we need to switch the lights at intersection or extend the green
def trafficAlg(intersection) :
	currentGreen = 1 if intersection[1].trafficLight == 'green' else 2
	currentRed = 2 if currentGreen == 1 else 1

	#if there are no cars on stopped road and hasn't been waiting for 15 seconds
	if(intersection[currentRed].numCars == 0 & intersection[currentRed].waitTime <= 1):
		return 'extend'	#extend the current green light
	else:
		return 'change'	#if the waitTime is over 1 time step or there are cars waiting we change the light

# Call arduino light function and bookeeping
def changeLight(intersection) : 
	currentGreen = intersection[1] if intersection[1].trafficLight == 'green' else intersection[2]
	currentRed = intersection[2] if currentGreen == intersection[1] else intersection[2]

	if trafficAlg(intersection) == 'extend':
		# call wael's method for arduino
		currentRed.waitTime = currentRed.waitTime+1

	elif trafficAlg(intersection) == 'change':
		# call wael's method for arduino
		currentGreen.waitTime = 0
		currentGreen.trafficLight = 'red'

		currentRed.waitTime = None
		currentRed.trafficLight = 'green'


		
def initIntersection():
	intersection = {
		1: Road(None, None, None, None),
		2: Road(None, None, None, None),
	}
	