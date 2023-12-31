from view import sense, act
import json
import random
import time
import serial

def runRobot():
  # O robo pergunta qual o pedido

  act.speak("Bom dia. Posso anotar seu pedido?") 
  pedido = sense.speech_to_text()
  escolhas = []

  while "não" not in pedido:
    escolhas.append(pedido)
    print('Pedido = ', pedido)
    act.speak("Mais alguma coisa?")
    pedido = sense.speech_to_text()
  act.speak("Vou levar seu pedido para a cozinha.")
  
  # Agora o robo vai até a cozinha
  act.walkFront()

  # O robo informa qual o pedido para o cozinheiro
  if escolhas != []:
    act.speak(f"O cliente pediu os itens: {escolhas}. Quando eu puder voltar com os pedidos diga, pronto.")

  res = []
  while "pronto" not in res:
    res = sense.speech_to_text()

  act.speak("Voltando para entregar o pedido ao cliente.")
  # O robo da meia volta e retorna ao cliente
  act.turnaround()
  act.walkFront()

  # Robo chega no cliente e pede para que peguem os pedidos
  act.speak("Aqui está seu pedido. Peço que retire os pedidos e diga pronto quando tudo tiver sido retirado.")
  res = []
  res = sense.speech_to_text()
  while "pronto" not in res:
    res = sense.speech_to_text()
    print(res)
  act.speak("Bom apetite.")
