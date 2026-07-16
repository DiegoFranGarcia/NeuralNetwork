import torch

from src.model import CatDogCNN


def test_catdogcnn_outputs_sigmoid_range():
    model = CatDogCNN()
    inputs = torch.randn(4, 3, 224, 224)

    outputs = model(inputs)

    assert torch.all(outputs >= 0)
    assert torch.all(outputs <= 1)
