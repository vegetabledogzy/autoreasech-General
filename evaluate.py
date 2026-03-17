"""
autoiter — 通用评估脚本模板

这个文件是只读的（除非用户明确允许修改）。
用户需要根据自己的任务实现 evaluate() 函数。

输出格式约定：
    评估结束后，必须打印一行格式为:
        <metric_name>: <value>
    例如:
        accuracy: 0.9234
        val_loss: 0.3421
        mAP: 0.7856

    这行输出会被 agent 通过 grep 提取，用于判定实验是否改善。
"""

import argparse
import json
import os
import sys


def evaluate(checkpoint_path: str = "checkpoint.pt", data_dir: str = "data") -> dict:
    """
    评估模型并返回指标字典。

    用户需要根据自己的任务实现此函数。返回的 dict 中至少包含
    config.yaml 中 metric.name 对应的 key。

    Args:
        checkpoint_path: 模型 checkpoint 路径
        data_dir: 数据目录

    Returns:
        dict, 例如 {"accuracy": 0.9234, "loss": 0.3421}
    """
    # ============================================================
    # TODO: 用户在此实现自己的评估逻辑
    # ============================================================
    #
    # 示例（伪代码）:
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
    raise NotImplementedError("请在 evaluate() 中实现你的评估逻辑")


def main():
    parser = argparse.ArgumentParser(description="autoiter evaluate")
    parser.add_argument("--checkpoint", default="checkpoint.pt", help="模型 checkpoint 路径")
    parser.add_argument("--data-dir", default="data", help="数据目录")
    args = parser.parse_args()

    metrics = evaluate(args.checkpoint, args.data_dir)

    # 打印所有指标，每行一个，格式: name: value
    # agent 会用 grep 提取需要的那一行
    for name, value in metrics.items():
        if isinstance(value, float):
            print(f"{name}: {value:.6f}")
        else:
            print(f"{name}: {value}")


if __name__ == "__main__":
    main()
