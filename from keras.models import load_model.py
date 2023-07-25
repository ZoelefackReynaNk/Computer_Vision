
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# Load the model
model = load_model('D:\\tensorflow-images\\keras_model.h5')

#load labels
with open('D:\\tensorflow-images\\labels.txt','r') as f:
  class_names = f.read().split('\n') 

  frame_width = int(cap.get(3))
  frame_height = int(cap.get(4))

  storage_size=(frame_width, frame_height)
  result=cv2.VideoWriter('', cv2.VideoWriter_fourcc(*'MJPG'), 10, storage_size)

while True:
  _,image =cap.read()    
# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# Replace this with the path to your image
# image = Image.openIMAGE_PATH>')



#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
  size = (224, 224)
# image = ImageOps.fit(image, size, Image.ANTIALIAS)
  image_small = cv2.resize(image,size)
#turn the image into a numpy array
  image_array = np.array(image_small)
# Normalize the image
  normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
# Load the image into the array
  data[0] = normalized_image_array

# run the inference
  prediction = model.predict(data)
  print(prediction)
  index = np.argmax(prediction)
  class_name = class_names[index]
  confidence_score =prediction

  print("class:", class_name)
  print("confidence score:", confidence_score)

  cv2.putText(image,str(class_name),(10,70),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0))
  cv2.imshow("nestor", image)
  key=cv2.waitKey(1)
  if key == ord('q'):
    break
image.release()
result.release()
cv2.destroyAllWindows
 