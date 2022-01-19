#import time                             #Importamos el paquete time
from w1thermsensor import W1ThermSensor #Importamos el paquete W1ThermSensor

sensor = W1ThermSensor() #Creamos el objeto sensor

#while True:
    temperature = sensor.get_temperature()                #Obtenemos la temperatura en centígrados
    print("La temperatura es %s  grados celsius" % temperature)  #Imprimimos el resultado
    #time.sleep(5)                                         #Esperamos un segundo antes de terminar el ciclo 