# AI 学习知识汇总 · Week1-2 追赶版

> 整理日期：2026-06-02 | 覆盖：AI 路线 Phase 1（Week 1-2 = 数据基础）
> 实际完成：仅 Git/Shell 前置（Day 1-2）
> 本文件用途：① 已学内容速查；② 未学内容**速通知识卡**；③ **立即可跑的迷你 EDA 项目骨架**（解决"项目实体"焦虑的核心）
> 关联文件：`AI学习路线_Hitachi_Lumada导向.md`（12 周完整路线，本文件只覆盖前 2 周）

---

## ⚠ 先看 — 给"AI 学习有迷茫感"的回应

> 你说："对于 AI 的学习有点迷茫感觉没有项目实体，没有学习的实感和方向。"

**真相**：路线图设计的核心矛盾是 **"知识点先于项目"**。前 2 周的设计是"看视频 + 学库"，没有可见产出。这本身就是迷茫的来源。

**本文件的解法**：跳过"先学完再做"的执念，直接进入 **Section F 的迷你项目**。3 天后你 GitHub 上会有一个 `fowt-cable-ai` 仓库，里面有第一个跑通的 ipynb 和可见的图表。**这就是项目实体**。

知识点（Section A-E）只是边做边查的速查册，不是必须按顺序读完。

---

## Section A：Shell / Git 已学速查（你已完成的部分）

> 对应 Missing Semester Lec.1 + Lec.6

### A.1 终端基础命令
```
ls          # 列出当前目录文件
cd <path>   # 切换目录；cd ~ 回家；cd .. 上一级；cd - 上一次
mkdir <name>          # 新建文件夹
mkdir -p a/b/c        # 一并建多级
cp src dst            # 复制；cp -r 递归
mv src dst            # 移动 / 重命名
rm <file>             # 删除文件；rm -r 递归；rm -rf 强删（危险）
```

### A.2 路径
- 绝对路径：`/Users/Admin/Documents/StudyNotes/`
- 相对路径：`./` 当前目录、`../` 上一级、`~` 家目录
- 项目里**始终用相对路径**，方便协作

### A.3 运行 Python
```bash
python3 script.py             # 直接运行
python3 -c "print('hi')"      # 一行
jupyter lab                   # 启动 Jupyter
```

### A.4 管道 / 重定向
```
cmd1 | cmd2      # cmd1 输出 → cmd2 输入
cmd > file       # 覆写
cmd >> file      # 追加
cmd 2> err.log   # 标准错误
```

### A.5 Git 工作流（核心 8 条）
```
git init                       # 当前目录初始化为仓库
git status                     # 看变更
git add <file>                 # 加入暂存区（也可 git add .，但风险高）
git commit -m "msg"            # 提交到本地仓库
git log --oneline -10          # 看历史
git remote add origin <url>    # 关联远程
git push -u origin main        # 首次推送
git pull                       # 拉取最新
```

### A.6 `.gitignore` Python 项目模板
```
__pycache__/
*.pyc
.ipynb_checkpoints/
.env
.DS_Store
*.csv         # 数据文件不上传（除非小样本）
data/raw/     # 原始数据
*.h5
*.pt
```

---

## Section B：StatQuest A1 理论卡片（4 张，必看）

> **资源**：StatQuest with Josh Starmer（YouTube，搜频道名，有中文字幕），合计 ≈ 1.5h
> 在你开始 Section C-E 前看完这 4 张卡。

### 卡 1：Bias vs Variance（过拟合本质）
- **直觉**：模型对训练数据"贴得太紧"= 高 variance（过拟合）；贴得太松 = 高 bias（欠拟合）。
- **形象**：高 bias 像近视看不清靶心；高 variance 像手抖每次打不同位置。
- **一行公式**：`Total Error ≈ Bias² + Variance + Noise`
- **面试一句话**："Bias 是模型表达力不足，variance 是模型对训练样本过度敏感；通过交叉验证发现两者的平衡。"

### 卡 2：Cross Validation（为何留验证集）
- **直觉**：把训练数据切成 K 折，每折轮流当验证集 → 估计模型对未见数据的泛化性能，不被单次划分运气左右。
- **常用**：k=5 或 k=10
- **一行公式**：`CV score = mean over k folds (validation MSE)`
- **面试一句话**："留单次 hold-out 易被随机划分影响，K-fold CV 给出泛化误差的稳定估计。"

### 卡 3：Linear Regression（ML 如何"学习"的最小例子）
- **直觉**：找一条直线 `y = wx + b` 使所有点到直线的距离平方和最小。
- **一行公式**：`L = Σ(y_i - (w·x_i + b))²` → 对 w, b 求导=0 解析解
- **面试一句话**："最小二乘法是凸优化问题，存在唯一闭式解，是所有 ML 算法的'入门样板'。"

### 卡 4：Train / Val / Test Split（数据集划分）
- **直觉**：训练集学习参数 / 验证集调超参 / 测试集只评估一次（绝不参与决策）。
- **划分比例**：常见 70 / 15 / 15；时序数据**必须按时间顺序切**（不能随机！）
- **一行规则**：测试集"看过一次后不能再改模型"。
- **面试一句话**："时序数据用随机切会泄露未来信息给训练集，必须用 time-based split。"

---

## Section C：NumPy 核心 API 速查

> 安装：`pip install numpy`
> 资源：官方 quickstart（30 分钟扫一遍即可）

```python
import numpy as np

# 创建
a = np.array([1, 2, 3])              # 一维
b = np.zeros((3, 4))                 # 3x4 全零
c = np.ones((2, 2))
d = np.linspace(0, 10, 100)          # 0-10 之间 100 个点
e = np.arange(0, 100, 5)             # 0,5,10,...,95

# 形状
print(a.shape)                       # (3,)
b.reshape(2, 6)
b.T                                  # 转置

# 索引切片
a[0]; a[-1]; a[1:3]
b[0, :]; b[:, 1]; b[0:2, 1:3]
a[a > 1]                             # 布尔索引

# 向量化（最大优势 — 不要写 for 循环）
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
x + y                                # [5, 7, 9]
x * 2                                # [2, 4, 6]
np.sin(x); np.exp(x); np.log(x)

# Broadcast 规则
A = np.ones((3, 4))                  # (3,4)
v = np.array([1, 2, 3, 4])           # (4,)
A + v                                # v 自动广播到每行

# 聚合
a.mean(); a.std(); a.sum(); a.min(); a.max()
a.argmax()                           # 最大值索引
b.mean(axis=0)                       # 沿轴聚合
```

---

## Section D：Pandas 核心 API 速查（时序数据导向）

> 安装：`pip install pandas`
> 资源：Kaggle Pandas course（~4h），可只跳着看时序部分

```python
import pandas as pd

# 读取
df = pd.read_csv("data.csv",
                 parse_dates=["timestamp"],
                 index_col="timestamp")

# 速览
df.head(); df.tail(); df.shape; df.dtypes; df.describe()
df.info()                                # 缺失值 + 类型概览
df["col"].value_counts()

# 选择
df["col"]; df[["a", "b"]]
df.loc["2024-01-01":"2024-01-31"]       # 按时间标签切片
df.iloc[0:10, :]                        # 按位置

# 时间聚合
df.resample("1H").mean()                # 1 小时平均
df.resample("1D").agg(["mean", "max"])  # 多个统计量

# 滑动窗口
df["col"].rolling(window=24).mean()     # 24 步滑动均值
df["col"].rolling(window=24).std()

# 分组
df.groupby("category").agg(
    mean_value=("value", "mean"),
    count=("value", "count"),
)

# 缺失值
df.isna().sum()                         # 各列缺失数
df.fillna(0)
df.fillna(method="ffill")               # 前向填充
df.interpolate(method="time")           # 时间插值（时序首选）
df.dropna()
```

---

## Section E：Matplotlib + Seaborn 速查

> 安装：`pip install matplotlib seaborn`

```python
import matplotlib.pyplot as plt
import seaborn as sns

# 折线（时序首选）
fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(df.index, df["wind_speed"])
ax.set_xlabel("Time"); ax.set_ylabel("Wind Speed [m/s]")
ax.set_title("Wind speed time series")
plt.tight_layout()
plt.savefig("wind.png", dpi=150, bbox_inches="tight")

# 热力图（相关性矩阵）
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", center=0)

# 箱线图（分布对比）
sns.boxplot(data=df, x="month", y="power")

# 散点 + 回归线
sns.regplot(data=df, x="wind_speed", y="power")
```

---

## Section F ⭐：立即可跑的迷你 EDA 项目骨架（**核心交付**）

> **3 天目标**：GitHub 仓库 `fowt-cable-ai` 上线，第一个 ipynb 跑通并有 4 张图。

### F.1 项目结构

```
~/code/fowt-cable-ai/
├── README.md
├── .gitignore
├── data/
│   └── T1.csv          # SCADA 数据
└── notebooks/
    └── 01_wind_data_eda.ipynb
```

### F.2 数据集推荐（**首选 — 门槛最低**）

**Kaggle "Wind Turbine SCADA Dataset"**
- 链接：https://www.kaggle.com/datasets/berkerisen/wind-turbine-scada-dataset
- 内容：土耳其单台风机 2018 年全年 10min 间隔 SCADA 数据 ≈ 50,000 行
- 字段：`Date/Time`、`LV ActivePower (kW)`（实际发电功率）、`Wind Speed (m/s)`、`Theoretical_Power_Curve (KWh)`（理论功率曲线）、`Wind Direction (°)`
- 下载方式：需要 Kaggle 账号（免费），下载得到 `T1.csv`

**备选**（Week 3+ 升级）：ERA5 Reanalysis（需要 CDS API key，门槛高）

### F.3 环境一键装

```bash
pip install numpy pandas matplotlib seaborn jupyter
```

### F.4 ipynb 6-Cell 完整代码（直接复制粘贴可跑）

#### Cell 1：导入 + 读取

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

df = pd.read_csv("../data/T1.csv")
# 字段重命名（更简洁）
df.columns = ["timestamp", "power_kW", "wind_speed", "power_theoretical", "wind_dir"]
df["timestamp"] = pd.to_datetime(df["timestamp"], format="%d %m %Y %H:%M")
df = df.set_index("timestamp").sort_index()
print(f"Shape: {df.shape}")
print(f"Time range: {df.index.min()} → {df.index.max()}")
df.head()
```
**产出**：知道数据多大、覆盖什么时间。

#### Cell 2：数据质量检查

```python
print("=== dtypes ===")
print(df.dtypes)
print("\n=== missing values ===")
print(df.isna().sum())
print("\n=== describe ===")
print(df.describe().round(2))
```
**产出**：确认是否有缺失值、各列数值范围合理性。

#### Cell 3：时序可视化（日尺度）

```python
daily = df.resample("1D").mean()
fig, axes = plt.subplots(2, 1, figsize=(14, 7), sharex=True)
axes[0].plot(daily.index, daily["wind_speed"], color="steelblue")
axes[0].set_ylabel("Wind speed [m/s]")
axes[0].set_title("Daily mean — wind speed")
axes[1].plot(daily.index, daily["power_kW"], color="darkorange")
axes[1].set_ylabel("Power [kW]")
axes[1].set_title("Daily mean — active power")
axes[1].set_xlabel("Date")
plt.tight_layout()
plt.savefig("01_daily_timeseries.png", dpi=150, bbox_inches="tight")
plt.show()
```
**产出**：看到全年趋势（冬季风强、夏季弱等）。

#### Cell 4：滑动 24h 平均 + 趋势叠加

```python
hourly = df.resample("1H").mean()
hourly["wind_speed_smooth"] = hourly["wind_speed"].rolling(window=24, center=True).mean()
fig, ax = plt.subplots(figsize=(14, 4))
ax.plot(hourly.index, hourly["wind_speed"], alpha=0.3, label="hourly")
ax.plot(hourly.index, hourly["wind_speed_smooth"], color="red", lw=1.2, label="24h rolling mean")
ax.set_ylabel("Wind speed [m/s]"); ax.legend(); ax.set_title("Wind speed with 24h trend")
plt.tight_layout()
plt.savefig("02_rolling_mean.png", dpi=150, bbox_inches="tight")
plt.show()
```
**产出**：日内波动 vs 长期趋势对比。

#### Cell 5：相关性热力图 + 功率曲线

```python
# 相关性
corr = df[["wind_speed", "power_kW", "power_theoretical", "wind_dir"]].corr()
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0, ax=axes[0])
axes[0].set_title("Correlation matrix")
# 功率曲线
axes[1].scatter(df["wind_speed"], df["power_kW"], s=2, alpha=0.3, label="measured")
axes[1].plot(df["wind_speed"].sort_values(),
             df.sort_values("wind_speed")["power_theoretical"],
             color="red", lw=1, label="theoretical")
axes[1].set_xlabel("Wind speed [m/s]"); axes[1].set_ylabel("Power [kW]")
axes[1].set_title("Power curve: measured vs theoretical")
axes[1].legend()
plt.tight_layout()
plt.savefig("03_corr_and_powercurve.png", dpi=150, bbox_inches="tight")
plt.show()
```
**产出**：知道哪些特征预测发电量最强（一定是 wind_speed），并看到实测 vs 理论功率曲线的偏差。

#### Cell 6：关键洞察（Markdown）

```markdown
## Key Insights

- 全年平均风速 ≈ X m/s，发电量 ≈ Y kW（替换为你实际值）
- 风速与发电量相关系数 ≈ 0.95+（强正相关，符合预期）
- 实测功率在 wind_speed ≈ 12-25 m/s 区间显著低于理论功率，提示存在**功率损失**（机械故障 / 气流偏角 / 控制策略）
- 24h 滑动均值揭示**风速日内变化**：白天午后峰值与夜间低谷的差异
- 缺失率 ≈ Z%（替换为实际值），可用前向填充或时间插值处理
```

**产出**：3-5 句洞察 — 这是面试时被问"你这个项目做了什么"的核心答案。

### F.5 3 天微观时间盒

| 时段 | 时长 | 任务 | 验证 |
|---|---|---|---|
| **Day 1（06-02 周二）** | 1.5h | ① pip 安装环境 ② Kaggle 注册下载 T1.csv ③ StatQuest A1 4 视频看完 | `python3 -c "import pandas; print('ok')"` 输出 ok |
| **Day 2（06-03 周三）** | 2h | ① `jupyter lab` 启动 ② 跑 Cell 1-4 ③ 截 3 张图保存 | 3 张 png 文件生成 |
| **Day 3（06-04 周四）** | 1.5h | ① 跑 Cell 5-6 ② 写 README ③ git init + push | GitHub 仓库可访问 |

### F.6 Git push 完整命令序列

```bash
cd ~/code
mkdir fowt-cable-ai && cd fowt-cable-ai

# 初始化
git init

# 写 .gitignore（复制 Section A.6 的模板）
cat > .gitignore << 'EOF'
__pycache__/
*.pyc
.ipynb_checkpoints/
.env
.DS_Store
data/T1.csv
EOF

# 写最简 README（日英双语，给面试官看的入口）
cat > README.md << 'EOF'
# fowt-cable-ai

FOWT 動力ケーブル疲労予測のための AI 代理モデル研究。
Surrogate ML models for fatigue prediction of dynamic power cables in FOWTs.

## Notebooks
- `notebooks/01_wind_data_eda.ipynb` — Wind turbine SCADA exploratory data analysis
EOF

# 创建文件夹
mkdir -p data notebooks

# 把 T1.csv 放到 data/，把你的 ipynb 放到 notebooks/

# 提交
git add README.md .gitignore notebooks/
git commit -m "Initial commit: wind SCADA EDA notebook"

# 在 GitHub 网页上新建 fowt-cable-ai 仓库（Public，不勾 README），拿到 url
git remote add origin git@github.com:<你的用户名>/fowt-cable-ai.git
git branch -M main
git push -u origin main
```

### F.7 成功标志

- [ ] GitHub 上能打开 `notebooks/01_wind_data_eda.ipynb` 看到代码和图表
- [ ] README 有日英双语简介
- [ ] 3 张 png 在 notebooks/ 里能被点开看到
- [ ] 你能用一句日语说："風速とアクティブパワーの強い相関（≈0.95）を確認し、理論曲線との乖離も特定しました。"

---

## Section G：这个项目和最终目标的关系（缓解迷茫感）

> "为什么要做这个？做完能干啥？"

```
现在：01_wind_data_eda.ipynb（这周交付）
   ↓ Pandas/Matplotlib 直觉
Week 3-4：02_fatigue_surrogate_XGBoost.ipynb  (B-14 风格)
   ↓ XGBoost + SHAP
Week 5-6：03_seabed_ML_prediction.ipynb       (B-20 风格)
   ↓ PyTorch 训练循环
Week 7-8：04_lstm_cable_tension.ipynb         (LSTM 时序)
   ↓ 时序数据预处理
Week 9-10：05_CNN_GRU_cable_surrogate.ipynb ⭐ (B-13 复现 R²=0.9864)
   ↓ 端到端代理模型
Week 11-12：06_cable_health_monitor_demo/    (Streamlit + Claude API)
   ↓ 演示 Dashboard
→ Hitachi Lumada APM 面试核心叙事
→ MC Digital / PKSHA LLM 集成证明
```

**今天跑通这个 ipynb = 你已经在台阶 1 上**，整个路径是连续可达的，不是空中楼阁。

---

## Section H：不要做的事（避免 3 天内分心）

| 别做 | 原因 |
|---|---|
| 看 CS231n / CS336 / 微积分课 | 与 Hitachi Lumada 目标无关，时间陷阱 |
| 跳到 PyTorch / CNN-GRU | 没有数据基础（Section D），写代码会卡 |
| 同时跑多个 Kaggle 数据集 | 单数据集做完一遍 > 多数据集做半截 |
| 纠结 README 写日语还是英语 | 双语各一段，3 分钟搞定 |
| 等到"全部学完再做" | 这就是迷茫的根源；做就对了 |

---

*整理日期：2026-06-02 | 用于追赶 Phase 1 Week 1-2 | 配套：动力电缆文献知识总结_Week1-2_20260602.md / 两周学习进度评估_20260602.md*
