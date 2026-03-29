import matplotlib.pyplot as plt
models = ["LR", "SVM", "RF", "CNN", "MobileNet"]
accuracy = [0.78, 0.81, 0.85, 0.90, 0.93]
plt.plot(models, accuracy, marker='o')
plt.title("Model Comparison")
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.savefig("../results/accuracy_plot.png")
plt.show()
