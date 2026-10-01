import torch

from src.model import CatDogCNN


def test_catdogcnn_forward_output_is_bounded():
    model = CatDogCNN()
    inputs = torch.randn(1, 3, 224, 224)

    outputs = model(inputs)

    assert torch.all(outputs >= 0)
    assert torch.all(outputs <= 1)
