from view import sense, act
import json
import random

def runRobot():
  # O robo pergunta qual o pedido
  act.act("Informe qual o seu pedido.") 
  pedido = sense.speech_to_text()
  print('Pedido = ', pedido)
  
  # Agora o robo da meia volta e anda ate o cozinheiro
  
  # O robo informa qual o pedido para o cozinheiro
  act.act("O pedido é: ", pedido)
  
  # O robo da meia volta e retorna ao cliente

  #
  #with open ('./model/dataset.json', 'r') as file:
  #  dataset = json.loads(file.read())
  #  for word in stt:
  #    if word in dataset['cardapio']:
  #      act.act(random.choice(dataset['resCumprimentos']))
  #      break
  #    elif word in dataset['despedidas']:
  #      act.act(random.choice(dataset['resDespedidas']))
  #      break
