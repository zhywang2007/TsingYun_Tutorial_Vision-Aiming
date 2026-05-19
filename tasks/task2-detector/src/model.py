"""MNIST digit model scaffold for Task 2.

Detector code should call the inference function in this module. Training code
lives in train.py so detector.py stays focused on board detection, corner
geometry, and PnP.
"""

from __future__ import annotations

from pathlib import Path
from typing import Sequence

import cv2
import numpy as np

import torch
import torch.nn.functional as F

from train import MNISTClassifier

RgbPixel = tuple[int, int, int]
ImageLike = np.ndarray

DEFAULT_MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "mnist_classifier.npz"

_cached_model: object | None = None
_cached_model_path: Path | None = None


def preprocess_mnist_crop(board_crop: ImageLike) -> np.ndarray:
    board = np.asarray(board_crop, dtype=np.uint8)
    if board.ndim == 3 and board.shape[2] == 3:
        gray = cv2.cvtColor(board, cv2.COLOR_BGR2GRAY)
    elif board.ndim == 2:
        gray = board.astype(np.uint8)
    else:
        raise ValueError("preprocess_mnist_crop expects a 2D or 3-channel image")

    resized = cv2.resize(gray, (28, 28), interpolation=cv2.INTER_AREA)
    normalized = resized.astype(np.float32) / 255.0
    normalized = normalized.reshape((1, 28, 28))
    return normalized


def load_mnist_model(model_path: Path = DEFAULT_MODEL_PATH) -> object:
    global _cached_model, _cached_model_path
    model_path = Path(model_path)
    if _cached_model is not None and _cached_model_path == model_path:
        return _cached_model

    model = MNISTClassifier()
    if model_path.exists():
        state_dict = torch.load(model_path, map_location="cpu")
        if isinstance(state_dict, dict):
            model.load_state_dict(state_dict)
        else:
            raise ValueError(f"Expected model state dict, got {type(state_dict)}")
    model.eval()

    _cached_model = model
    _cached_model_path = model_path
    return model


def predict_mnist_digit(model: object, model_input: np.ndarray) -> tuple[int, float]:
    tensor = torch.from_numpy(model_input.astype(np.float32))
    if tensor.ndim == 3:
        tensor = tensor.unsqueeze(0)
    elif tensor.ndim == 2:
        tensor = tensor.unsqueeze(0).unsqueeze(0)
    elif tensor.ndim == 4:
        pass
    else:
        raise ValueError("predict_mnist_digit expects input with 2, 3, or 4 dimensions")

    with torch.no_grad():
        logits = model(tensor)
        probabilities = F.softmax(logits, dim=1)
        confidence, predicted = torch.max(probabilities, dim=1)

    return int(predicted.item()), float(confidence.item())


def classify_mnist_digit(board_crop: ImageLike, model_path: Path = DEFAULT_MODEL_PATH) -> tuple[int, float]:
    model = load_mnist_model(model_path)
    model_input = preprocess_mnist_crop(board_crop)
    return predict_mnist_digit(model, model_input)
