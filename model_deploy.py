from keras.applications.mobilenet import MobileNet
from keras.layers import GlobalAveragePooling2D, Dense, Dropout, Flatten
from keras.preprocessing import image
from keras.models import Sequential, model_from_json
from keras.applications.mobilenet import preprocess_input
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import json


def build_model():
  with open('model_results/multi_disease_model.json', 'r') as json_file:
    architecture = json.load(json_file)
    model = model_from_json(json.dumps(architecture))

  model.load_weights('model_results/multi_disease_model_weight.h5')
  model._make_predict_function()
  return model


def load_image(img_path):
  img = image.load_img(img_path, target_size=(128, 128, 3))
  img = image.img_to_array(img)
  img = np.expand_dims(img, axis=0)
  img /= 255.
  return img


def predict_image(model, img_path, biggest_result=False, show_result=False):
  new_image = load_image(img_path)
  pred = model.predict(new_image)

  if show_result:
    img = mpimg.imread(img_path)
    imgplot = plt.imshow(img, cmap='bone')
    plt.title(pred)
    plt.show()

  return (np.argmax(pred), np.max(pred)) if biggest_result else pred


if __name__ == '__main__':
  labels = ['Atelectasis', 'Cardiomegaly', 'Consolidation', 'Edema', 'Effusion',
            'Emphysema', 'Fibrosis', 'Hernia', 'Infiltration', 'Mass', 'Nodule',
            'Pleural_Thickening', 'Pneumonia', 'Pneumothorax']
  model = build_model()

  preds = predict_image(model, 'model_results/test_images/00024720_000.png')
  print(preds)

  preds = predict_image(model, 'model_results/test_images/00028173_010.png')
  print(preds)

  preds = predict_image(model, 'model_results/test_images/00028173_012.png')
  print(preds)

  preds = predict_image(model, 'model_results/test_images/Cardiomegaly.jpeg')
  print(preds)
