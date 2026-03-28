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

# Plot class distribution
plt.figure(figsize=(10,5))
sns.barplot(x=list(class_counts.keys()), y=list(class_counts.values()))
plt.xticks(rotation=45)
plt.title("Class Distribution")
plt.xlabel("Pest Classes")
plt.ylabel("Number of Images")
plt.show()


# Show sample images
plt.figure(figsize=(12,8))

for i, cls in enumerate(classes[:6]):
    class_path = os.path.join(DATASET_PATH, cls)
    img_name = os.listdir(class_path)[0]
    img_path = os.path.join(class_path, img_name)
    img = Image.open(img_path)
    plt.subplot(2,3,i+1)
    plt.imshow(img)
    plt.title(cls)
    plt.axis("off")
plt.tight_layout()
plt.show()

# Image size analysis
widths = []
heights = []
for cls in classes:
    class_path = os.path.join(DATASET_PATH, cls)
    for img_name in os.listdir(class_path)[:20]:  # sample for speed
        img_path = os.path.join(class_path, img_name)
        img = Image.open(img_path)
        w, h = img.size
        widths.append(w)
        heights.append(h)
print("Average Width:", np.mean(widths))
print("Average Height:", np.mean(heights))


# Plot image size distribution
plt.figure(figsize=(10,5))
plt.hist(widths, bins=20, alpha=0.5, label="Width")
plt.hist(heights, bins=20, alpha=0.5, label="Height")
plt.legend()
plt.title("Image Size Distribution")
plt.show()

