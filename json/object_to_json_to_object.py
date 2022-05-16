import json

class Sensor:
    chanel = 1
    Type = 'Example'
    BCM_Pin = 0
    value = 1.1
    operational = True


exampleSensorList = []

exampleSensor1 = Sensor()
exampleSensor1.chanel = 1
exampleSensor1.Type = 'DHT22'
exampleSensor1.BCM_Pin = 6
exampleSensor1.value = 3.3
exampleSensor1.operational = True

exampleSensor2 = Sensor()
exampleSensor2.chanel = 2
exampleSensor2.Type = 'DHT22'
exampleSensor2.BCM_Pin = 10
exampleSensor2.value = 5.5
exampleSensor2.operational = False


exampleSensorList.append(exampleSensor1)
exampleSensorList.append(exampleSensor2)


# create Json String from a list ob objects
exampleSensorsJson = json.dumps(exampleSensorList, default = lambda x: x.__dict__)

print()
print ('JSon String :')
print (exampleSensorsJson)
print ()
print ()
loadedSensors = []
tmpObjects = json.loads(exampleSensorsJson)
for x in tmpObjects:
    newSensor = Sensor()
    newSensor.chanel = x['chanel']
    newSensor.Type = x['Type']
    newSensor.BCM_Pin = x['BCM_Pin']
    newSensor.value = x['value']
    newSensor.operational = x['operational']
    loadedSensors.append(newSensor)

print ('Loaded Objects :')
for x in loadedSensors:
    print ('chanel      : ', x.chanel)
    print ('Type        : ', x.Type)
    print ('BCM Pin     : ', x.BCM_Pin)
    print ('value       : ', x.value)
    print ('operational : ', x.operational)
    print ()