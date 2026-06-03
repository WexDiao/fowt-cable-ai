# 仓库结构与推送工作流

## 为什么不按"日期"或"第几天"组织？

Git 的提交历史本身就是时间线。每次 `git push` 都带有日期戳，
可以通过 `git log` 查看。因此文件夹名称不需要承载时间信息——
它只需要说明**内容是什么**，而不是**什么时候写的**。

---

## 仓库结构

```
fowt-cable-ai/
├── notes/
│   ├── papers/        ← 论文精读笔记（每篇论文一个 .md 文件）
│   └── concepts/      ← 理论概念笔记（ML 原理、工程知识等）
├── notebooks/         ← Jupyter notebook（编号命名，如 01-eda.ipynb）
├── scripts/           ← 独立 Python 脚本
├── fowt-cable-ai/     ← Python 包源码
├── figures/           ← 图表、可视化输出
├── papers/            ← 文献 PDF（本地保留，不上传）
├── push.bat           ← 双击一键推送（Windows）
├── push.sh            ← 终端推送脚本
├── WORKFLOW.md        ← 本文件
└── README.md
```

### 文件放哪里？

| 文件类型 | 放在哪里 |
|---------|---------|
| 论文阅读笔记 `.md` | `notes/papers/论文名或ID.md` |
| 理论/概念笔记 `.md` | `notes/concepts/主题名.md` |
| Python 脚本 `.py` | `scripts/` |
| Python 包代码 | `fowt-cable-ai/` |
| Jupyter notebook | `notebooks/` |
| 图表 / 图片 | `figures/` |
| 文献 PDF | `papers/`（仅本地，永远不上传） |

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
| 新增概念笔记 | `notes: LSTM sequence modeling basics` |
| 新增脚本 | `scripts: fatigue damage calculator` |
| 新增 notebook | `notebook: 02 xgboost surrogate` |
| 更新已有文件 | `update: revise CNN-GRU reading notes` |
| 结构调整 | `refactor: reorganize notes layout` |

---

## 一次性迁移：从 day1 迁移到新结构

GitHub 上目前有 `Daily_Notes/day1/` 文件夹（旧结构），需要合并到本地后清理。

**第一步：合并 GitHub 历史到本地**

```bash
git fetch origin
git merge origin/main --allow-unrelated-histories -m "merge: bring in GitHub history before restructure"
```

> 如果出现冲突，保留本地文件版本即可。

**第二步：把 day1 的 .md 文件移到新位置**

```bash
# 这是一篇论文精读笔记 → papers/
mv "Daily_Notes/day1/精读_白皮书_Section1_导言与背景.md" notes/papers/

# 这是一篇通用笔记 → concepts/
mv "Daily_Notes/day1/动力电缆笔记_Week1.md" notes/concepts/
```

**第三步：删除旧文件夹和意外上传的 PDF**

```bash
git rm -r Daily_Notes/
```

**第四步：统一 branch 名称（master → main）**

```bash
git branch -m master main
```

**第五步：提交并推送**

```bash
git add -A
git commit -m "refactor: restructure from day-based to topic-based layout"
git push origin main
```

> 之后 `push.bat` / `push.sh` 会自动检测当前分支名，无需修改脚本。

---

## 常见问题

**脚本报错 "No remote origin found"：**
```bash
git remote add origin https://github.com/WexDiao/DailyNotes.git
```

**push 被拒绝（rejected）：**
```bash
git pull origin main --rebase
bash push.sh
```

**查看提交历史（替代"第几天"的方式）：**
```bash
git log --oneline --graph
```

**误加了不该提交的文件：**
```bash
git reset HEAD <文件名>
```
