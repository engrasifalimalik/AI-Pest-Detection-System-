import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from decision_support import get_recommendation
import os

# Load model
model = tf.keras.models.load_model("../models/pest_model.h5")

# Class names (IMPORTANT: match dataset folders)
class_names = os.listdir("../data/train")

# Load image
img_path = "sample.jpg"

img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

# Prediction
prediction = model.predict(img_array)
predicted_class = class_names[np.argmax(prediction)]
confidence = np.max(prediction)

# Recommendation
recommendation = get_recommendation(predicted_class)

print(f"Detected Pest: {predicted_class}")
print(f"Confidence: {confidence:.2f}")
print(f"Suggested Action: {recommendation}")
