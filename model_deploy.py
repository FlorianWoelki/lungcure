from keras.applications.mobilenet import MobileNet
from keras.layers import GlobalAveragePooling2D, Dense, Dropout, Flatten
from keras.preprocessing import image
from keras.models import Sequential
import numpy as np

def setup_model_with_weights():
  base_mobilenet_model = MobileNet(
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
  model.add(Dense(14, activation='sigmoid'))

  model.load_weights('/Users/Florian/Desktop/lungcure/model_results/multi_disease_model_weight.h5')

  model.compile(
      optimizer='adam',
      loss='binary_crossentropy',
      metrics=['binary_accuracy', 'mae']
  )
  return model


def load_image(img_path):
  img = image.load_img(img_path, target_size=(128, 128))
  img_tensor = image.img_to_array(img)
  img_tensor = np.expand_dims(img_tensor, axis=0)
  img_tensor /= 255.
  return img_tensor


def predict_image(model, img_path, biggest_result=False):
  new_image = load_image(img_path)
  pred = model.predict(new_image)
  return (np.argmax(pred), np.max(pred)) if biggest_result else pred


"""
labels = ['Atelectasis', 'Cardiomegaly', 'Consolidation', 'Edema', 'Effusion',
          'Emphysema', 'Fibrosis', 'Hernia', 'Infiltration', 'Mass', 'Nodule',
          'Pleural_Thickening', 'Pneumonia', 'Pneumothorax']
model = setup_model_with_weights()
(index, value) = predict_image(model, '/Users/Florian/Desktop/lungcure/model_results/__results___files/__results___10_0.png', biggest_result=True)
print(labels[index], value)
"""
