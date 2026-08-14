import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
digits = load_digits()

X = digits.data
y = digits.target
images = digits.images

# Split data
X_train, X_test, y_train, y_test, img_train, img_test = train_test_split(
    X, y, images, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save output image
plt.imshow(img_test[0], cmap='gray')
plt.title(f"Actual: {y_test[0]}  |  Predicted: {y_pred[0]}")
plt.axis('off')
plt.savefig("prediction.png")
print("Image saved as prediction.png")
