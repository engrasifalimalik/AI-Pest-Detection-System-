import tensorflow as tf
from preprocessing import load_data

_, val_ds = load_data("../data/train")

model = tf.keras.models.load_model("../models/pest_model.h5")

loss, accuracy = model.evaluate(val_ds)

print("Validation Accuracy:", accuracy)
