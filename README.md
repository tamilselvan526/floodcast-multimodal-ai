# 🌌 OptiDigit-ML

[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Docker Support](https://img.shields.io/badge/docker-enabled-blue.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![ML Framework: Scikit--Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)

An optimized, containerized machine learning pipeline for handwritten digit classification. Built with **Scikit-Learn** using a tuned **Logistic Regression** model, this repository provides a reproducible, lightweight environment for training, testing, and visualizing model predictions.

---

## ⚡ Features

- 🎯 **High Accuracy**: Logistic Regression classifier tuned for the 8x8 MNIST-equivalent digits dataset.
- 🐳 **Dockerized Setup**: Zero-dependency environment replication with Docker.
- 📊 **Visual Output**: Auto-saves visualization of the actual vs. predicted label to `prediction.png`.
- 🛠️ **Developer Friendly**: Structured with `.gitignore`, pinned `requirements.txt`, and standard licensing.

---

## 📐 Project Architecture

```mermaid
graph TD
    A[Load Digits Dataset 8x8] --> B[Split Data: 80% Train / 20% Test]
    B --> C[Train Logistic Regression Model]
    C --> D[Predict Test Set Labels]
    D --> E[Calculate Accuracy Score]
    D --> F[Generate & Save prediction.png]
    style A fill:#1a1a2e,stroke:#30363d,stroke-width:2px,color:#00ffff
    style B fill:#1a1a2e,stroke:#30363d,stroke-width:2px,color:#fff
    style C fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#fff
    style D fill:#1a1a2e,stroke:#30363d,stroke-width:2px,color:#fff
    style E fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#34d399
    style F fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#34d399
```

---

## 🚀 Quick Start

You can run this project either locally using a Python virtual environment or inside a Docker container.

### Option A: Local Environment (Recommended)

1. **Clone the repository** (or navigate to the project directory):
   ```bash
   cd OptiDigit-ML
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute the classification demo**:
   ```bash
   python ml_demo.py
   ```

---

### Option B: Containerized Run (Docker)

If you have Docker installed, you can build and execute the project without installing Python or any libraries locally.

1. **Build the Docker Image**:
   ```bash
   docker build -t optidigit-ml .
   ```

2. **Run the Container**:
   ```bash
   docker run --rm -v ${PWD}:/app optidigit-ml
   ```
   > **Note:** The `-v ${PWD}:/app` flag mounts your current directory to the container, ensuring that the generated `prediction.png` is saved back to your local host machine.

---

## 📁 Repository Structure

```text
├── .gitignore              # Git ignore rules for Python & IDE files
├── Dockerfile              # Docker container configuration
├── LICENSE                 # MIT Open-Source License
├── README.md               # Visual documentation (this file)
├── requirements.txt        # Pinned python library dependencies
├── ml_demo.py              # Main model training and prediction script
└── prediction.png          # Generated prediction output image
```

---

## 📈 Model Performance

When evaluated on the test set, the classifier outputs:
- **Model**: Logistic Regression (L2 regularization, max 5000 iterations)
- **Dataset**: Scikit-Learn Digits (1,797 samples, 10 classes)
- **Typical Accuracy**: ~`96.1%` to `97.8%` (depending on train-test split)

Upon running, the script will output:
```text
Accuracy: 0.9611111111111111
Image saved as prediction.png
```

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more details.
