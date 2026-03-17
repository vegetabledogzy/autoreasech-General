# autoiter

A general-purpose autonomous research iteration framework: let an AI agent loop through "modify code → run experiment → evaluate metrics → reflect" — you wake up to an experiment notebook and a better model.

Inspired by [autoresearch](https://github.com/karpathy/autoresearch). Generalized for any ML research task.

[English](#english) | [中文](#中文)

---

## English

### Differences from autoresearch

| | autoresearch | autoiter |
|---|---|---|
| Training time | Fixed 5 min | No limit, runs to completion |
| Metric | val_bpb (fixed) | User-defined (accuracy, loss, mAP...) |
| Editable files | train.py only | Configurable, multi-file |
| Reflection | None | Hypothesis before, analysis after |
| Stagnation handling | None | Deep reflection & bottleneck analysis |
| Task type | LLM pretraining | General (classification, detection, generation, regression...) |

### Project structure

```
autoiter/
├── program.md        — Agent instructions (human edits, agent follows)
├── config.yaml       — Experiment config (human fills in)
├── train.py          — Training script template (agent iterates)
├── evaluate.py       — Evaluation script template (read-only)
├── reflections.md    — Experiment reflections (agent maintains)
├── results.tsv       — Experiment log (agent maintains, not committed)
└── .gitignore
```

### Quick start

1. Fill in your training code in `train.py` (or your own file)
2. If evaluation is separate, fill in `evaluate.py`; otherwise print metrics at the end of `train.py`
3. Edit `config.yaml` — set metric name, direction, run command, etc.
4. Point your AI agent to `program.md`:

```
Read program.md and config.yaml, then start the autonomous iteration loop.
```

### Output format

Your training/evaluation script must print a metric line at the end:

```
accuracy: 0.9234
```

Format: `<metric_name>: <value>`. The agent extracts it via grep.

### Tips

- `program.md` is your "research org code" — iterate on it as you learn what works.
- Add task-specific constraints (VRAM limits, data augmentation rules, etc.) to `program.md`.
- `reflections.md` is one of the most valuable outputs — it records what worked, what didn't, and why.

---

## 中文

### 与 autoresearch 的区别

| | autoresearch | autoiter |
|---|---|---|
| 训练时间 | 固定 5 分钟 | 不固定，跑到自然结束 |
| 指标 | val_bpb（固定） | 用户自定义（accuracy、loss、mAP...） |
| 可编辑文件 | 仅 train.py | 用户配置，支持多文件 |
| 反思系统 | 无 | 实验前写假设，后写分析 |
| 停滞处理 | 无 | 连续失败触发深度反思和瓶颈分析 |
| 任务类型 | LLM 预训练 | 通用（分类、检测、生成、回归...） |

### 项目结构

```
autoiter/
├── program.md        — agent 指令（人类编辑，agent 遵循）
├── config.yaml       — 实验配置（人类填写）
├── train.py          — 训练脚本模板（agent 迭代修改）
├── evaluate.py       — 评估脚本模板（只读）
├── reflections.md    — 实验反思记录（agent 自动维护）
├── results.tsv       — 实验结果日志（agent 自动维护，不提交 git）
└── .gitignore
```

### 快速开始

1. 把你的训练代码填入 `train.py`（或你自己的文件）
2. 如果评估逻辑独立，填入 `evaluate.py`；否则直接在 train.py 末尾打印指标
3. 编辑 `config.yaml`，配置指标名称、方向、运行命令等
4. 启动你的 AI agent，指向 `program.md`：

```
请阅读 program.md 和 config.yaml，开始自主迭代实验。
```

### 输出格式约定

训练/评估脚本结束时，必须打印指标行：

```
accuracy: 0.9234
```

格式为 `<metric_name>: <value>`，agent 通过 grep 提取。

### 使用建议

- `program.md` 是你的"研究组织代码"，可以根据经验不断迭代优化。
- 如果你的任务有特殊约束（如显存限制、数据增强策略），在 `program.md` 中补充说明。
- `reflections.md` 是最有价值的产出之一——它记录了什么有效、什么无效、为什么。
