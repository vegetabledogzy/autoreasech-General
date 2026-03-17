"""
autoiter — Evaluation script template

This file is read-only (unless the user explicitly allows modification).
Users should implement the evaluate() function for their own task.

Output format convention:
    After evaluation, print one line per metric:
        <metric_name>: <value>
    e.g.:
        accuracy: 0.9234
        val_loss: 0.3421
        mAP: 0.7856

    The agent extracts this line via grep to determine whether the experiment improved.
"""

import argparse
import json
import os
import sys


def evaluate(checkpoint_path: str = "checkpoint.pt", data_dir: str = "data") -> dict:
    """
    Evaluate the model and return a metrics dict.

    Users should implement this for their own task. The returned dict must
    contain at least the key matching metric.name in config.yaml.

    Args:
        checkpoint_path: Path to model checkpoint
        data_dir: Data directory

    Returns:
        dict, e.g. {"accuracy": 0.9234, "loss": 0.3421}
    """
    # ============================================================
    # TODO: Implement your evaluation logic here
    # ============================================================
    #
    # Example (pseudocode):
    #
    # import torch
    # from model import MyModel
    # from data import get_test_loader
    #
    # model = MyModel()
    # model.load_state_dict(torch.load(checkpoint_path))
    # model.eval()
    #
    # correct, total = 0, 0
    # for x, y in get_test_loader(data_dir):
    #     pred = model(x).argmax(dim=1)
    #     correct += (pred == y).sum().item()
    #     total += y.size(0)
    #
    # return {"accuracy": correct / total}
    #
    raise NotImplementedError("Please implement your evaluation logic in evaluate()")


def main():
    parser = argparse.ArgumentParser(description="autoiter evaluate")
    parser.add_argument("--checkpoint", default="checkpoint.pt", help="Model checkpoint path")
    parser.add_argument("--data-dir", default="data", help="Data directory")
    args = parser.parse_args()

    metrics = evaluate(args.checkpoint, args.data_dir)

    # Print all metrics, one per line, format: name: value
    # The agent will grep for the target metric line
    for name, value in metrics.items():
        if isinstance(value, float):
            print(f"{name}: {value:.6f}")
        else:
            print(f"{name}: {value}")


if __name__ == "__main__":
    main()
