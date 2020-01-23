import requests
from pathlib import Path

from database import db, View

API_KEY = 'AIzaSyCwdQHf1IAIopaVPF7KefK2SZiDOyMo-_k'
def process_position(lat, lng):
  params = {
    'location': '{0},{1}'.format(lat, lng),
    'size': '600x600',
    'fov': 25,
    'heading': -20,
    'pitch': -15,
    'key': API_KEY
  }
  url = 'https://maps.googleapis.com/maps/api/streetview'
  r= requests.get(url=url, params=params).content
  with open(Path('test.png') ,'wb') as handler:
    handler.write(r)



if __name__=='__main__':
  process_position(36.6351738,-121.9263157)
