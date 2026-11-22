import os
import matplotlib
matplotlib.use('Agg')  # Headless backend for Docker, CI, and server environments
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


def run_pipeline(output_image_path: str = "prediction.png"):
    """
    Train and evaluate a Logistic Regression classifier on the 8x8 Digits dataset.
    Saves a sample prediction visualization to `output_image_path`.
    """
    # 1. Load dataset
    digits = load_digits()
    X = digits.data
    y = digits.target
    images = digits.images

    # 2. Train-test split (80% train, 20% test)
    X_train, X_test, y_train, y_test, img_train, img_test = train_test_split(
        X, y, images, test_size=0.2, random_state=42, stratify=y
    )

    # 3. Train model with increased max_iter for full convergence
    model = LogisticRegression(max_iter=5000, solver='lbfgs')
    model.fit(X_train, y_train)

    # 4. Predict on test set
    y_pred = model.predict(X_test)

    # 5. Evaluate performance
    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc:.4f} ({acc * 100:.2f}%)")
    print("\nClassification Summary:")
    print(classification_report(y_test, y_pred, digits=4))

    # 6. Save visual output of sample prediction
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.imshow(img_test[0], cmap='gray')
    ax.set_title(f"Actual: {y_test[0]}  |  Predicted: {y_pred[0]}")
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(output_image_path, dpi=150)
    plt.close(fig)
    print(f"Prediction preview saved successfully to '{output_image_path}'.")

    return model, acc


if __name__ == "__main__":
    run_pipeline()
