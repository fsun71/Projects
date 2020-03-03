import numpy as np 
from scipy.stats import expon

def cargoSim(iterations):
	cargoLambda1 = 0.556828051
	cargoLambda2 = 0.308918849
	cargoTimesArray = []

	for i in range(iterations):
		cargoDrops = []
		for cargoDrop in range(7):
			cargoTime1 = np.random.exponential(cargoLambda1)
			cargoTime2 = np.random.exponential(cargoLambda2)

			cargoDropTimes = [(cargoTime1 + cargoTime1), (cargoTime1 + cargoTime1), (cargoTime1 + cargoTime1 + cargoTime2), (cargoTime2 + cargoTime1 + cargoTime2), (cargoTime2 + cargoTime2 + cargoTime2), (cargoTime2 + cargoTime2 + cargoTime2)]

			cargoDrop = cargoDropTimes[int(np.random.uniform(0,len(cargoDropTimes)))]
			cargoDrops.append(cargoDrop)

		cargoTimesArray.append(np.mean(cargoDrops))

	return np.mean(cargoTimesArray)

iterMaster = 10000

propulsionReliability = 0.9914
commsReliability = 0.9875
powerReliability = 0.9313
navReliability = 0.9496

planeSystemReliability = propulsionReliability * commsReliability * powerReliability * navReliability
cargoFailureRate = 0.837

overallReliability = cargoFailureRate * planeSystemReliability

print(planeSystemReliability)
print(planeSystemReliability * cargoFailureRate)


