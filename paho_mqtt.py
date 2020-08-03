import paho.mqtt.client as mqtt #import the client1
import time
#from pimux import Sensors
#v = function.misc()
#s = Sensors.sensor()
#AK09918C
#"values"
############
def on_message(client, userdata, message):
    #print("message received " ,str(message.payload.decode("utf-8")))
    #print(str(message.payload.decode("utf-8")))
    if (str(message.payload.decode("utf-8"))=='on'):
        print("on")
        #v.viberate(100)
    #print("message topic=",message.topic)
    #print("message qos=",message.qos)
    #print("message retain flag=",message.retain)

########################################
broker_address="192.168.43.126"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
#print("Subscribing to topic","sub")
client.subscribe("sub")
#while True:
#    print("Publishing message to topic","pub")
#    client.publish("pub",'hello')
#    time.sleep(4) # wait
#client.loop_stop() #stop the loop
