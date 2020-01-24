import requests
from PIL import Image
from pathlib import Path
from io import BytesIO
from database import db, View
import numpy as np


API_KEY = 'AIzaSyCwdQHf1IAIopaVPF7KefK2SZiDOyMo-_k'
MAPS_API_URL = 'https://maps.googleapis.com/maps/api'
def is_image(lat, lng):
  params= {
    'location': '{0},{1}'.format(lat, lng),
    'key': API_KEY
  }
  
  print(r)
  return False

def process_all_view(lat,lng):
  for heading in np.arange(0, 361, 60):
    for pitch in np.arange(-90, 91, 60):
      print('kek')
      params = {
        'location': '{0},{1}'.format(lat, lng),
        'size': '600x600',
        # 'fov': 25,
        'heading': heading,
        'pitch': pitch,
        'key': API_KEY
      }
      image = Image.open(BytesIO(requests.get(url=MAPS_API_URL+'/streetview', params=params).content))
      image.show()

def process_position(lat, lng):
  params = {
    'location': '{0},{1}'.format(lat, lng),
    'key': API_KEY
  }
  r = requests.get(url=MAPS_API_URL+'/streetview/metadata', params=params).json()
  if r['status'] != 'OK':
    pass
  process_all_view(lat,lng)


if __name__=='__main__':
  process_position(36.6351738,-121.9263157)
