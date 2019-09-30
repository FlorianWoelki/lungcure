from keras.applications.mobilenet import MobileNet
from keras.layers import GlobalAveragePooling2D, Dense, Dropout, Flatten
from keras.preprocessing import image
from keras.models import Sequential, model_from_json
from keras.applications.mobilenet import preprocess_input
import numpy as np
import json


def build_model():
  """base_mobilenet_model = MobileNet(
      input_shape=(128, 128, 3), 
      include_top=False,
      weights=None
  )
  model = Sequential()
  model.add(base_mobilenet_model)
  model.add(GlobalAveragePooling2D())
  model.add(Dropout(0.5))
  model.add(Dense(512))
  model.add(Dropout(0.5))
  model.add(Dense(14, activation='sigmoid'))"""

  with open('model_results/multi_disease_model.json', 'r') as json_file:
    architecture = json.load(json_file)
    model = model_from_json(json.dumps(architecture))

  model.load_weights('model_results/multi_disease_model_weight.h5')

  """model.compile(
      optimizer='adam',
      loss='binary_crossentropy',
      metrics=['binary_accuracy', 'mae']
  )"""
  return model


def load_image(img_path):
  img = image.load_img(img_path, target_size=(128, 128))
  img = image.img_to_array(img)
  img = np.expand_dims(img, axis=0)
  img /= 255.
  img = preprocess_input(img)
  return img


def predict_image(model, img_path, biggest_result=False):
  new_image = load_image(img_path)
  pred = model.predict(new_image)
  return (np.argmax(pred), np.max(pred)) if biggest_result else pred


if __name__ == '__main__':
  labels = ['Atelectasis', 'Cardiomegaly', 'Consolidation', 'Edema', 'Effusion',
            'Emphysema', 'Fibrosis', 'Hernia', 'Infiltration', 'Mass', 'Nodule',
            'Pleural_Thickening', 'Pneumonia', 'Pneumothorax']
  model = build_model()

  preds = predict_image(model, 'model_results/test_images/Atelectasis.png')
  print(preds)

