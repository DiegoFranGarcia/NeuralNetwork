# Cat vs Dog Image Classifier

A convolutional neural network (CNN) built with PyTorch that classifies images as either a cat or a dog. Trained on the Kaggle Dogs vs Cats dataset.

## Overview

This project implements a binary image classification pipeline using a custom CNN architecture. The model is trained from scratch and includes a full training loop, evaluation metrics, and an inference script for classifying new images.

## Tech Stack

- Python 3.11
- PyTorch 2.x
- torchvision
- NumPy
- Matplotlib
- Pillow

## Project Structure

NeuralNetwork/
├── README.md
├── requirements.txt
├── data/
│   ├── train/
│   │   ├── cats/
│   │   └── dogs/
│   └── val/
│       ├── cats/
│       └── dogs/
├── src/
│   ├── model.py        # CNN architecture definition
│   ├── train.py        # Training loop and checkpointing
│   ├── evaluate.py     # Evaluation metrics and confusion matrix
│   └── predict.py      # Single image inference
├── notebooks/
│   └── exploration.ipynb
└── tests/
└── test_model.py

## Setup

```bash
git clone https://github.com/DiegoFranGarcia/NeuralNetwork.git
cd NeuralNetwork
pip install -r requirements.txt
```

## Dataset

Download the Dogs vs Cats dataset from Kaggle:

```bash
kaggle datasets download -d salader/dogs-vs-cats
unzip dogs-vs-cats.zip -d data/
```

The dataset contains 25,000 labeled images split into training and validation sets.

## Training

```bash
python src/train.py --epochs 20 --batch-size 32 --lr 0.001
```

Training arguments:
- `--epochs` — number of training epochs (default: 20)
- `--batch-size` — batch size (default: 32)
- `--lr` — learning rate (default: 0.001)
- `--checkpoint` — path to save model checkpoints

## Evaluation

```bash
python src/evaluate.py --checkpoint checkpoints/best_model.pt
```

Reports accuracy, precision, recall, F1 score, and confusion matrix on the validation set.

## Inference

```bash
python src/predict.py --image path/to/image.jpg --checkpoint checkpoints/best_model.pt
```

Returns the predicted class (cat or dog) and confidence score.

## Model Architecture

The CNN consists of:
- 3 convolutional blocks (Conv2d + BatchNorm + ReLU + MaxPool)
- 2 fully connected layers with dropout
- Binary output with sigmoid activation

Input images are resized to 224x224 and normalized using ImageNet mean and standard deviation.

## Running Tests

```bash
pytest tests/
```
