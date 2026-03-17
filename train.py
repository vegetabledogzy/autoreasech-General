"""
autoiter — 训练脚本模板

这是 agent 迭代修改的主文件。
用户先填入自己的基线实现，然后交给 agent 自主优化。

要求：
    1. 训练结束后，打印指标行，格式: <metric_name>: <value>
       例如: accuracy: 0.9234
    2. 指标名称必须与 config.yaml 中 metric.name 一致
    3. 如果评估逻辑简单，可以直接写在这里（不需要单独的 evaluate.py）
"""

import time
import sys

# ============================================================
# TODO: 用户在此实现自己的训练逻辑
# ============================================================
#
# 下面是一个极简的示例框架，展示输出格式约定。
# 请替换为你的真实训练代码。
#


def train():
    """训练入口。用户替换为真实实现。"""

    print("=" * 60)
    print("autoiter — training started")
    print("=" * 60)

    start_time = time.time()

    # ----------------------------------------------------------
    # 示例：CIFAR-10 分类（伪代码，请替换）
    # ----------------------------------------------------------
    #
    # import torch
    # import torch.nn as nn
    # import torchvision
    # import torchvision.transforms as T
    #
    # # 数据
    # transform = T.Compose([T.ToTensor(), T.Normalize((0.5,)*3, (0.5,)*3)])
    # trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
    # testset  = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
    # trainloader = torch.utils.data.DataLoader(trainset, batch_size=128, shuffle=True)
    # testloader  = torch.utils.data.DataLoader(testset,  batch_size=256, shuffle=False)
    #
    # # 模型
    # model = torchvision.models.resnet18(num_classes=10).cuda()
    # optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    # criterion = nn.CrossEntropyLoss()
    #
    # # 训练
    # for epoch in range(10):
    #     model.train()
    #     for x, y in trainloader:
    #         x, y = x.cuda(), y.cuda()
    #         loss = criterion(model(x), y)
    #         optimizer.zero_grad()
    #         loss.backward()
    #         optimizer.step()
    #
    # # 评估
    # model.eval()
    # correct, total = 0, 0
    # with torch.no_grad():
    #     for x, y in testloader:
    #         x, y = x.cuda(), y.cuda()
    #         correct += (model(x).argmax(1) == y).sum().item()
    #         total += y.size(0)
    # accuracy = correct / total
    # val_loss = 0.0  # 如需要可计算
    #
    # ----------------------------------------------------------

    # 占位：替换为真实指标
    accuracy = 0.0
    val_loss = 0.0

    elapsed = time.time() - start_time

    # ----------------------------------------------------------
    # 输出指标（agent 通过 grep 提取，格式不要改）
    # ----------------------------------------------------------
    print("---")
    print(f"accuracy: {accuracy:.6f}")
    print(f"val_loss: {val_loss:.6f}")
    print(f"training_seconds: {elapsed:.1f}")


if __name__ == "__main__":
    train()
