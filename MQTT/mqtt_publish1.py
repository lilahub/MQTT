from typing import Match
import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Temperatura_Interna")


def getSensor1():
    return uniform(10.0, 20.0)


def getSensor2():
    return uniform(21.0, 30.0)


def getSensor3():
    return uniform(31.0, 40.0)


def getSensor4():
    return uniform(41.0, 50.0)


def getSensor5():
    return uniform(51.0, 60.0)


def publicar(mensagem):
    client.connect(mqttBroker)
    client.publish("TEMPERATURA", mensagem)
    print("Publicando temperatura")


def week(opcao):
    switcher = {
        1: getSensor1(),
        2: getSensor2(),
        3: getSensor3(),
        4: getSensor4(),
        5: getSensor5(),
    }

    return switcher.get(opcao, "Invalido")


while True:
    opcao = int(input(
        "Digite o numero de 1 a 5\n 1 - 10 a 20\n 2 - 21 a 30\n 3 - 31 a 40\n 4 - 41 a 50\n 5 - 51 a 60\n para gerar uma temperatura:"))
    temperaturaAtual = week(opcao)
    publicar(temperaturaAtual)


'''
switcher = {
    0: publicar(getSensor1()),
    1: publicar(getSensor2()),
    2: publicar(getSensor3()),
    3: publicar(getSensor4()),
    4: publicar(getSensor5()),
}

print("teste")
'''

'''result = week(2)
print(result)

publicar(uniform(20.0, 21.0))
'''
'''
while True:
    randNumber = uniform(20.0, 21.0)
    client.publish("TEMPERATURA", randNumber)
    print("Publicado " + str(randNumber) + " no topico TEMPERATURA")
    time.sleep(1)
'''
