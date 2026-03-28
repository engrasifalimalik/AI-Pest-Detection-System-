# Import libraries
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import seaborn as sns


# Set dataset path
DATASET_PATH = "../data/train"  # adjust if needed
classes = os.listdir(DATASET_PATH)
print("Classes:", classes)
print("Number of classes:", len(classes))

# Count images per class
class_counts = {}
for cls in classes:
    class_path = os.path.join(DATASET_PATH, cls)
    class_counts[cls] = len(os.listdir(class_path))

print(class_counts)
