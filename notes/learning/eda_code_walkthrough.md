# AI 小项目代码解析 — `01_wind_data_eda.py`

> 项目路径：`C:\Users\wexco\coding\fowt-cable-ai\notebooks\01_wind_data_eda.py`
> 数据：Kaggle Wind Turbine SCADA Dataset (T1.csv)
> 用途：跟着这份 md 看代码，理解每个步骤"做什么 + 为什么 + 关键参数"

---

## 0. 项目骨架与依赖

```python
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

HERE = Path(__file__).resolve().parent
DATA_PATH = HERE.parent / "data" / "T1.csv"
USE_SYNTHETIC = not DATA_PATH.exists()
```

**目的**：
- 引入数据分析栈（NumPy、Pandas、Matplotlib、Seaborn）
- 用 `pathlib` 做跨平台路径，`HERE` 是脚本所在目录、`DATA_PATH` 是 T1.csv 的预期位置
- `USE_SYNTHETIC` 是降级开关——如果真数据缺失就跑合成数据，保证脚本一定能跑通

**为什么这样写**：
- **路径用 `pathlib`** 而不是字符串拼接：跨 Windows / macOS / Linux 通用
- **降级机制**：演讲日数据可能没到位、网络不通、文件被锁——有 fallback 比"跑挂"安全
- **seaborn whitegrid 样式**：默认 matplotlib 是灰底，whitegrid 是白底带浅灰网格，更适合投影和打印

---

## Cell 1 — 数据加载与解析

```python
if USE_SYNTHETIC:
    # 生成合成数据 (略)
    ...
else:
    df = pd.read_csv(DATA_PATH)
    df.columns = ["timestamp", "power_kW", "wind_speed",
                  "power_theoretical", "wind_dir"]
    df["timestamp"] = pd.to_datetime(df["timestamp"], format="%d %m %Y %H:%M")
    df = df.set_index("timestamp").sort_index()

print(f"Shape: {df.shape}")
print(f"Time range: {df.index.min()} -> {df.index.max()}")
print(df.head())
```

**目的**：把 CSV 读进 Pandas DataFrame，并把时间戳列设为索引。

**关键步骤解释**：

| 步骤 | 作用 | 为什么 |
|---|---|---|
| `pd.read_csv(DATA_PATH)` | 读取 CSV 文件 | Pandas 时序入口 |
| `df.columns = [...]` | 重命名列（原列名带括号、单位，操作不便） | 后续 `df.wind_speed` 等访问更简洁 |
| `pd.to_datetime(..., format="%d %m %Y %H:%M")` | 把字符串日期解析成 datetime 对象 | Kaggle 数据的日期格式是 `"01 01 2018 00:00"` 这种，必须给 format |
| `.set_index("timestamp")` | 把时间列设为行索引 → DatetimeIndex | **关键步骤**：让 `.resample()`、`.rolling()`、`.loc["2018-03":"2018-04"]` 这些时序方法可用 |
| `.sort_index()` | 按时间升序排序 | SCADA 数据有时是乱序的，保证后续 resample 正确 |

**输出**：
- Shape: `(50460, 5)` — 5 万行，4 个数值列
- Time range: `2018-01-01 00:00:00 → 2018-12-31 23:50:00`

---

## Cell 2 — 数据质量检查

```python
print("=== dtypes ===")
print(df.dtypes)
print("\n=== missing values ===")
print(df.isna().sum())
print("\n=== describe ===")
print(df.describe().round(2))
```

**目的**：在做任何分析前，先体检——看类型、缺失、数值范围是否合理。

**关键步骤解释**：

| 调用 | 检查什么 |
|---|---|
| `df.dtypes` | 每列类型对不对？比如 wind_speed 应该是 float，不是 string |
| `df.isna().sum()` | 每列缺失值数量。0 = 没有缺失 |
| `df.describe()` | 数值统计：count, mean, std, min, 25%, 50%, 75%, max。检查 min/max 是否在物理范围内（比如风速 0-30 m/s 才合理） |

**为什么这步重要 — Fail-Fast 原则**：
- SCADA 数据常有传感器掉线（产生 NaN）、单位漂移（kW vs MW）、负值异常
- 在这里发现 → 1 分钟修复
- 拿到模型训练阶段才发现 → 调试半天

**本次结果**：
- 类型正确（float64）
- **缺失 0%** — 数据质量好
- 风速 max ≈ 25 m/s（接近 cut-out），功率 max ≈ 3600 kW（额定）→ 范围合理

---

## Cell 3 — 日尺度时序图

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

**目的**：把 10 分钟数据降到日均，看全年趋势。

**关键步骤解释**：

| 代码 | 作用 / 参数解读 |
|---|---|
| `df.resample("1D").mean()` | **核心方法**。"1D" = 1 天频率；`.mean()` = 聚合方式取平均。还可以 `.max()`, `.sum()` 等 |
| `plt.subplots(2, 1, ..., sharex=True)` | 上下两个子图共享 x 轴（时间轴对齐） |
| `figsize=(14, 7)` | 宽 14、高 7 英寸；宽高比约 2:1，适合时序图 |
| `dpi=150` | 输出 PNG 的分辨率，150 适合投影 / 文档；300 适合印刷 |
| `bbox_inches="tight"` | 保存时裁掉多余空白边 |

**为什么用日均而不是原始 10 分钟**：
- 10 分钟原始数据有 5 万个点，画出来锯齿状一片，看不清趋势
- 日均 365 个点，季节性一目了然
- mean 聚合对**对称分布**（如风速）很合适；如果数据偏态（如降水），可能需要用 median

**输出**：`01_daily_timeseries.png` — 上面板风速、下面板功率的年度趋势

---

## Cell 4 — 24 小时滑动平均

```python
hourly = df.resample("1h").mean()
hourly["wind_speed_smooth"] = (
    hourly["wind_speed"].rolling(window=24, center=True).mean()
)
fig, ax = plt.subplots(figsize=(14, 4))
ax.plot(hourly.index, hourly["wind_speed"], alpha=0.3, label="hourly")
ax.plot(hourly.index, hourly["wind_speed_smooth"],
        color="red", lw=1.2, label="24h rolling mean")
ax.set_ylabel("Wind speed [m/s]"); ax.legend()
plt.tight_layout()
plt.savefig("02_rolling_mean.png", dpi=150, bbox_inches="tight")
```

**目的**：用滑动窗口分离"日内昼夜波动"和"长期趋势"。

**关键步骤解释**：

| 参数 | 含义 | 为什么这么选 |
|---|---|---|
| 先 `resample("1h")` | 把 10 分钟降到 1 小时 | 滑动窗口在 1 小时尺度上更直观；也能减少计算量 |
| `.rolling(window=24, ...)` | 滑动窗口大小 = 24 个点 | 1 小时数据 × 24 = **正好一个昼夜周期**，能消除日内波动 |
| `center=True` | 窗口中心对齐当前点 | **避免相位滞后**：默认 `center=False` 时窗口右对齐，趋势线会"晚"半个窗口（12 小时） |
| `.mean()` | 聚合方式 | 简单平均最常见；也可以 `.median()` 抗异常 |
| `alpha=0.3` | 原始线半透明 | 突出红色平滑线，原始数据作为背景 |

**center=True 的对比直觉**：
```
原始数据：    ↑─↓─↑─↓─↑─↓   (波动)
trailing mean (默认): ←平滑值滞后
center mean:  对齐 ↑↓ 中心，无延迟
```

**输出**：`02_rolling_mean.png` — 原始小时数据（灰）+ 24h 滑动平滑（红）

---

## Cell 5 — 相关性矩阵 + 功率曲线

```python
corr = df[["wind_speed", "power_kW", "power_theoretical", "wind_dir"]].corr()
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 左：相关性热力图
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0, ax=axes[0])
axes[0].set_title("Correlation matrix")

# 右：功率曲线
axes[1].scatter(df["wind_speed"], df["power_kW"], s=2, alpha=0.3,
                label="measured")
sorted_df = df.sort_values("wind_speed")
axes[1].plot(sorted_df["wind_speed"], sorted_df["power_theoretical"],
             color="red", lw=1, label="theoretical")
axes[1].set_xlabel("Wind speed [m/s]"); axes[1].set_ylabel("Power [kW]")
axes[1].set_title("Power curve: measured vs theoretical")
axes[1].legend()
plt.tight_layout()
plt.savefig("03_corr_and_powercurve.png", dpi=150, bbox_inches="tight")
```

**目的**：找出最影响发电量的特征 + 验证理论曲线和实测的关系。

**关键步骤解释**：

| 代码 | 作用 |
|---|---|
| `df[[...]].corr()` | **Pearson 相关系数矩阵**。返回 4×4 对称方阵 |
| `sns.heatmap(..., annot=True)` | 热力图，`annot=True` 把数字写在格子里 |
| `cmap="coolwarm"` | 配色：负值蓝、零白、正值红 |
| `center=0` | 0 是颜色的中性点 |
| `scatter(..., s=2, alpha=0.3)` | 散点：点小（s=2）+ 半透明（α=0.3）= 5 万点叠加不会糊成一片黑 |
| `df.sort_values("wind_speed")` | 按 x 轴排序，理论曲线才能画成连续线（否则是乱序折线） |

**Pearson 公式直觉**：
```
corr(X, Y) = Cov(X, Y) / (std(X) × std(Y))
        值 ∈ [-1, 1]
        1 = 完美正相关（X 变大 Y 也线性变大）
        0 = 无线性关系
        -1 = 完美负相关
```

**本次结果**：
- wind_speed ↔ power_kW = **0.91**（强正相关）
- wind_dir ↔ 其他 ≈ 0（**因为机舱有 yaw control 自动迎风**，方向不重要）
- power_kW ↔ power_theoretical ≈ 0.95（理论曲线校准过）

**功率曲线读图**：
- 3-12 m/s 立方上升段
- 12 m/s 以上接近额定 3600 kW
- **12 m/s 以上有大量散点在红线下方** → 运行损失

---

## Cell 6 — 2×2 汇总图

```python
fig, axes = plt.subplots(2, 2, figsize=(14, 8))
# 4 个子图：daily wind / hourly + rolling / heatmap / power curve
...
plt.savefig("04_summary_2x2.png", dpi=150, bbox_inches="tight")
```

**目的**：把前面 4 张图组合成一张交付物，便于放进 PPT。

**关键步骤**：
- `plt.subplots(2, 2)` → 4 个子图轴 `axes[0,0]`, `axes[0,1]`, `axes[1,0]`, `axes[1,1]`
- 每个子图用 `axes[row, col].plot/scatter/...` 单独绘制
- `plt.tight_layout()` 自动调整子图间距，避免标签互相挤压

**这步价值**：从 4 张独立 PNG 到 1 张 2×2 PNG，**演讲时只需要切一次 slide** 就看到所有诊断。

---

## Cell 7 — 关键洞察打印

```python
mean_ws = df["wind_speed"].mean()
mean_pw = df["power_kW"].mean()
corr_ws_pw = df["wind_speed"].corr(df["power_kW"])
missing_pct = df.isna().sum().sum() / df.size * 100

print(f"Mean wind speed: {mean_ws:.2f} m/s")     # 7.56
print(f"Mean active power: {mean_pw:.2f} kW")    # 1307.68
print(f"Corr(wind_speed, power_kW): {corr_ws_pw:.3f}")  # 0.913
print(f"Missing fraction: {missing_pct:.2f}%")   # 0.00
```

**目的**：把分析结论写成可口述的几行数字，**给演讲准备弹药**。

**为什么重要**：
- 这些数字是"被问起"时秒答的备料
- `:.2f` / `:.3f` 是 f-string 格式控制，限制小数位数
- 运行一次 → 拷贝结论到讲稿

---

## Cell 8-11 — 4 张带标注的单图

> 这 4 张图是给 PPT P8 和 P9 用的——**关键信息直接写在图上**，听众一眼就懂。

### Cell 8 — Plot 1: 日均风速 + 年均线 + 极值标注

```python
ax.plot(daily.index, daily["wind_speed"], color="steelblue")
ax.axhline(mean_ws, color="red", linestyle="--",
           label=f"Year mean = {mean_ws:.2f} m/s")

# 标注冬季峰值
winter = daily.loc["2018-01":"2018-03"]["wind_speed"]
w_date, w_val = winter.idxmax(), winter.max()
ax.annotate(f"Winter peak\n≈ {w_val:.1f} m/s",
            xy=(w_date, w_val), xytext=(40, 5),
            textcoords="offset points",
            arrowprops=dict(arrowstyle="->", color="darkred"))
```

**关键技术点**：
- `axhline(y, ...)` 画水平参考线，**年均线**是这张图的"锚"
- `daily.loc["2018-01":"2018-03"]` — **DatetimeIndex 切片**（只有时间索引才能这样写）
- `idxmax()` / `max()` 在切片上找峰值的时间和数值
- `annotate(..., xy=数据坐标, xytext=偏移像素, arrowprops=箭头样式)` — Matplotlib 标准标注

### Cell 9 — Plot 2: 滑动均 + 趋势标注

```python
ax.plot(hourly.index, hourly["wind_speed"], color="lightgray",
        lw=0.4, alpha=0.7, label="Hourly raw")
ax.plot(hourly.index, hourly["wind_speed_smooth"], color="red",
        lw=1.4, label="24-h rolling (center=True)")
ax.annotate("Diurnal noise removed;\nseasonal trend visible",
            xy=(hourly.index[mid_idx], hourly["wind_speed_smooth"].iloc[mid_idx]),
            xytext=(25, 60), textcoords="offset points",
            arrowprops=dict(arrowstyle="->", color="black"))
```

**关键技术点**：
- 原始数据 `lw=0.4` 细线 + `alpha=0.7` 半透明 = 当背景
- 红线 `lw=1.4` 突出
- 标注指向曲线中段，文字说明 "diurnal noise removed; seasonal trend visible"
- 让听众**看图就明白滑动均的作用**

### Cell 10 — Plot 3: 相关性 + 重点格子加框

```python
sns.heatmap(corr, annot=True, fmt=".2f",
            annot_kws={"size": 13, "weight": "bold"})

# 给 wind_speed ↔ power_kW 加黑色边框
from matplotlib.patches import Rectangle
i_ws = cols.index("wind_speed")
i_p = cols.index("power_kW")
for (xp, yp) in [(i_p, i_ws), (i_ws, i_p)]:
    ax.add_patch(Rectangle((xp, yp), 1, 1,
                            fill=False, edgecolor="black", lw=2.5))
```

**关键技术点**：
- `annot_kws={"size": 13, "weight": "bold"}` — 热力图内数字字号加大、加粗
- **`Rectangle` 加边框** 是这张图的灵魂——把听众的目光直接锁到 0.91 那个格子
- 加两次（对称两格）保证视觉对齐

### Cell 11 — Plot 4: 功率曲线 + 三段式标注

```python
ax.scatter(df["wind_speed"], df["power_kW"], s=2, alpha=0.2, color="steelblue")
ax.plot(sorted_df["wind_speed"], sorted_df["power_theoretical"],
        color="red", lw=2)

# 三条标注
ax.axvline(3, color="green", linestyle=":")           # cut-in
ax.text(3.2, ..., "cut-in ≈ 3 m/s", color="green")
ax.axhline(rated, color="orange", linestyle="--")     # rated
ax.text(0.5, rated + 50, f"rated ≈ {rated:.0f} kW")
ax.axvspan(12, 25, alpha=0.08, color="red")           # losses zone
ax.annotate("Losses zone\n(below theoretical)",
            xy=(17, rated * 0.4),
            bbox=dict(boxstyle="round", facecolor="white", edgecolor="darkred"))
```

**关键技术点**：
- `axvline` 画垂直参考线（cut-in、cut-out）
- `axhline` 画水平参考线（额定功率）
- `axvspan` 画**半透明垂直色块**——比线更强地标出区域（损失区）
- `annotate(..., bbox=dict(...))` 给标注加白底圆角框，**在散点群里清晰可读**

---

## 整体设计思路总结

| 步骤 | 数据动作 | 可视化动作 | 与最终目的的关系 |
|---|---|---|---|
| Cell 1 | Load + parse → DatetimeIndex | — | 时序分析的入场券 |
| Cell 2 | Quality check | — | Fail-fast，防错入下游 |
| Cell 3 | Resample to daily | 上下子图 | 季节性 |
| Cell 4 | Rolling 24h | 原始+平滑叠加 | 趋势 vs 噪声 |
| Cell 5 | corr() + sort_values | 热力图 + 散点 | 特征重要性 + 功率曲线 |
| Cell 6 | — | 2×2 汇总 | 演讲一图全览 |
| Cell 7 | 提取关键数字 | print | 口述弹药 |
| Cell 8-11 | 同 3-5 | + 标注 + 高亮 | **让图自解释** |

**贯穿主题**：
> 每一步都对应未来 cable surrogate 工作流的一个等价步骤——
> Load CSV → Load OrcaFlex outputs
> Resample → 时间对齐
> Rolling → 平滑振动信号
> Corr → 找驱动张力/曲率的特征
> Power curve → "Tension vs Wave Height" 类的工况曲线

这套 EDA 不只是练手，**它的骨架就是 cable surrogate 项目的骨架**。

---

*文件版本：v1 · 2026-06-05*
