"""
autoiter — Training script template

This is the main file the agent iterates on.
Fill in your baseline implementation, then let the agent optimize autonomously.

Requirements:
    1. Print a metric line after training, format: <metric_name>: <value>
       e.g.: accuracy: 0.9234
    2. Metric name must match metric.name in config.yaml
    3. If evaluation is simple, you can include it here (no need for a separate evaluate.py)
"""

import time
import sys

# ============================================================
# TODO: Implement your training logic here
# ============================================================
#
# Below is a minimal example showing the output format convention.
# Replace with your actual training code.
#


def train():
    """Training entry point. Replace with your real implementation."""

    print("=" * 60)
    print("autoiter — training started")
    print("=" * 60)

    start_time = time.time()

    # ----------------------------------------------------------
    # Example: CIFAR-10 classification (pseudocode, replace this)
    # ----------------------------------------------------------
    #
    # import torch
    # import torch.nn as nn
    # import torchvision
    # import torchvision.transforms as T
    #
    # # Data
    # transform = T.Compose([T.ToTensor(), T.Normalize((0.5,)*3, (0.5,)*3)])
    # trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
    # testset  = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
    # trainloader = torch.utils.data.DataLoader(trainset, batch_size=128, shuffle=True)
    # testloader  = torch.utils.data.DataLoader(testset,  batch_size=256, shuffle=False)
    #
    # # Model
    # model = torchvision.models.resnet18(num_classes=10).cuda()
    # optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    # criterion = nn.CrossEntropyLoss()
    #
    # # Train
    # for epoch in range(10):
    #     model.train()
    #     for x, y in trainloader:
    #         x, y = x.cuda(), y.cuda()
    #         loss = criterion(model(x), y)
    #         optimizer.zero_grad()
    #         loss.backward()
    #         optimizer.step()
    #
    # # Evaluate
    # model.eval()
    # correct, total = 0, 0
    # with torch.no_grad():
    #     for x, y in testloader:
    #         x, y = x.cuda(), y.cuda()
    #         correct += (model(x).argmax(1) == y).sum().item()
    #         total += y.size(0)
    # accuracy = correct / total
    # val_loss = 0.0  # compute if needed
    #
    # ----------------------------------------------------------

    # Placeholder: replace with real metrics
    accuracy = 0.0
    val_loss = 0.0

    elapsed = time.time() - start_time

    # ----------------------------------------------------------
    # Print metrics (agent extracts via grep, do not change format)
    # ----------------------------------------------------------
    print("---")
    print(f"accuracy: {accuracy:.6f}")
    print(f"val_loss: {val_loss:.6f}")
    print(f"training_seconds: {elapsed:.1f}")


if __name__ == "__main__":
    train()
