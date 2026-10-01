import torch

from src.model import CatDogCNN


def test_catdogcnn_has_expected_layers():
    model = CatDogCNN()
    layers = list(model.features)

    expected_types = [
        torch.nn.Conv2d,
        torch.nn.BatchNorm2d,
        torch.nn.ReLU,
        torch.nn.MaxPool2d,
        torch.nn.Conv2d,
        torch.nn.BatchNorm2d,
        torch.nn.ReLU,
        torch.nn.MaxPool2d,
        torch.nn.Conv2d,
        torch.nn.BatchNorm2d,
        torch.nn.ReLU,
        torch.nn.MaxPool2d,
    ]

    assert [type(layer) for layer in layers] == expected_types

    classifier_layers = list(model.classifier)
    assert isinstance(classifier_layers[1], torch.nn.Linear)
    assert isinstance(classifier_layers[3], torch.nn.Dropout)
    assert isinstance(classifier_layers[4], torch.nn.Linear)


def test_catdogcnn_forward_returns_predictions():
    model = CatDogCNN()
    inputs = torch.randn(2, 3, 224, 224)

    outputs = model(inputs)

    assert outputs.shape == (2, 1)
