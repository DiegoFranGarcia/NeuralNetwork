import sys

import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

from src.train import evaluate, parse_args, train_one_epoch


def build_dummy_loader() -> DataLoader:
    inputs = torch.randn(2, 3, 224, 224)
    labels = torch.tensor([0.0, 1.0])
    dataset = TensorDataset(inputs, labels)
    return DataLoader(dataset, batch_size=1)


def test_train_one_epoch_returns_metrics():
    model = nn.Sequential(
        nn.Flatten(),
        nn.Linear(3 * 224 * 224, 1),
        nn.Sigmoid(),
    )
    dataloader = build_dummy_loader()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
    criterion = nn.BCELoss()

    loss, accuracy = train_one_epoch(
        model, dataloader, optimizer, criterion, torch.device("cpu")
    )

    assert isinstance(loss, float)
    assert 0.0 <= accuracy <= 1.0


def test_evaluate_returns_metrics():
    model = nn.Sequential(
        nn.Flatten(),
        nn.Linear(3 * 224 * 224, 1),
        nn.Sigmoid(),
    )
    dataloader = build_dummy_loader()
    criterion = nn.BCELoss()

    loss, accuracy = evaluate(model, dataloader, criterion, torch.device("cpu"))

    assert isinstance(loss, float)
    assert 0.0 <= accuracy <= 1.0


def test_parse_args_defaults(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["train.py"])

    args = parse_args()

    assert args.data_dir == "data"
    assert args.epochs == 20
    assert args.batch_size == 32
    assert args.lr == 0.001
    assert args.checkpoint is None
