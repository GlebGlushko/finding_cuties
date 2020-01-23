import numpy as np
import tensorflow as tf
from tensorflow.python import  keras
from keras.applications.resnet50 import preprocess_input, decode_predictions
from keras.preprocessing.image import load_img, img_to_array
from keras.applications import ResNet50
from pathlib import Path
import os 
import pandas as pd

os.environ['TF_CPP_MIN_LOG_LEVEL'] ='2'
tf.logging.set_verbosity(tf.logging.ERROR)

class Model:
    image_size=224
    model = ResNet50()

    def __init__(self):
        pass

    def predict(self, image_path):
        image = self.read_and_prep_image(image_path)
        predictions = self.model.predict(image)
        result = decode_predictions(predictions, top=5)
        return result
        # most_likely_labels = decode_predictions(predictions, top=5, class_list_path='../input/resnet50/imagenet_class_index.json')


    def read_and_prep_image(self, image_path, img_height=image_size, img_width=image_size):
        image = load_img(image_path, target_size=(img_height, img_width))
        img_array = np.array([img_to_array(image)])
        output = preprocess_input(img_array)
        return output



if __name__=='__main__':
  model = Model()
  image_path = Path(os.getcwd()+'/src/input/3.png')
  predictions = model.predict(image_path)
  print(predictions)
  # classes = pd.read_json(Path(os.getcwd()+'/src/input/imagenet_class_index.json'))
  # classes = classes.transpose()
  # print(classes.head(15))