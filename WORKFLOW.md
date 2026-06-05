# 仓库结构与推送工作流

## 为什么不按"日期"或"第几天"组织？

Git 的提交历史本身就是时间线。每次 `git push` 都带有日期戳，
可以通过 `git log` 查看。因此文件夹名称不需要承载时间信息——
它只需要说明**内容是什么**，而不是**什么时候写的**。

---

## 仓库结构

```
_fowt-cable-ai/
├── code/             ← 所有 Python（.py / .ipynb，编号 + 工具脚本都放这里）
├── notes/
│   ├── papers/       ← 论文精读笔记（每篇论文一个 .md）
│   └── learning/     ← 自学笔记：概念、cheatsheet、代码走读、setup 指南
├── figures/          ← 图表、可视化输出（按分析名子目录）
├── seminars/         ← 组会 / 学会汇报（事件存档）
│   └── <YYYY-MM-DD>_<topic>/   ← 仅这里允许日期
├── _local/           ← 本地专属，永远 gitignore
│   ├── data/         ←   原始数据（CSV / .sim）
│   └── pdfs/         ←   文献 PDF
├── push.bat / push.sh ← 一键推送
├── LOG.md            ← 进度日志（最新在顶）
├── WORKFLOW.md       ← 本文件
└── README.md
```

### 文件放哪里？

| 文件类型 | 放在哪里 |
|---------|---------|
| 论文阅读笔记 `.md` | `notes/papers/论文名或ID.md` |
| 自学笔记 / cheatsheet `.md` | `notes/learning/主题名.md` |
| Python 脚本（任何） | `code/` |
| 图表 / 图片（来自分析） | `figures/<分析名>/` |
| 组会汇报（PPT + 讲稿 + 生成脚本） | `seminars/<日期>_<主题>/` |
| 原始数据 (CSV / sim) | `_local/data/`（**永远不上传**） |
| 文献 PDF | `_local/pdfs/`（**永远不上传**） |
| 进度日志条目 | 追加到 `LOG.md` 顶部 |

> 顶层只剩 5 个内容文件夹 + 3 个 .md + 推送脚本。
> 看到 `_` 开头就知道是本地不上传的。

---

## 一键推送

**Windows 双击运行（推荐）：**
```
双击 push.bat
```

**终端：**
```bash
bash push.sh
```

脚本自动执行：显示变更 → 暂存 → 输入 commit 信息 → 推送

---

## Commit 信息参考

| 场景 | 示例 |
|------|------|
| 新增论文笔记 | `notes: Cerik2024 cable fatigue reading` |
| 新增自学笔记 | `notes: LSTM sequence modeling basics` |
| 新增脚本 | `code: 02 xgboost surrogate` |
| 更新已有文件 | `update: revise CNN-GRU reading notes` |
| 结构调整 | `refactor: reorganize layout` |

---

## 常见问题

**脚本报错 "No remote origin found"：**
```bash
git remote add origin https://github.com/WexDiao/fowt-cable-ai.git
```

**push 被拒绝（rejected）：**
```bash
git pull origin main --rebase
bash push.sh
```

**查看提交历史：**
```bash
git log --oneline --graph
```

**误加了不该提交的文件：**
```bash
git reset HEAD <文件名>
```
