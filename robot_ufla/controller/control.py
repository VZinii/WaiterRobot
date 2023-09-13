from view import sense, act
import json
import random

def runRobot():
  stt = sense.speech_to_text()
  print('STT = ', stt)

  with open ('./model/dataset.json', 'r') as file:
    dataset = json.loads(file.read())
    for word in stt:
      if word in dataset['cumprimentos']:
        act.act(random.choice(dataset['resCumprimentos']))
        break
      elif word in dataset['despedidas']:
        act.act(random.choice(dataset['resDespedidas']))
        break
