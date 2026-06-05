# Kaggle T1.csv 数据下载指引

> 目标文件：`C:\Users\wexco\coding\fowt-cable-ai\data\T1.csv`
> 预计耗时：5-10 分钟（取决于 Kaggle 账号是否已有）

---

## Step 1：注册 / 登录 Kaggle 账号（已有跳过）

1. 打开 https://www.kaggle.com/
2. 右上角 **Register**（免费，可用 Google 账号一键登录）
3. 完成邮箱验证

---

## Step 2：进入数据集页面

1. 打开数据集链接：
   **https://www.kaggle.com/datasets/berkerisen/wind-turbine-scada-dataset**
2. 页面会显示数据集介绍、字段说明、几张示例图

---

## Step 3：下载数据集

1. 页面顶部找到 **Download** 按钮（黑色，右上角附近）
2. 点击下载，文件名是 `archive.zip`（约 1-2 MB）
3. 浏览器默认保存到 `C:\Users\wexco\Downloads\`

**如果遇到提示需要验证手机号**：
- Kaggle 偶尔要求验证手机号才能下载，按提示完成即可（用国内手机号也可以）

---

## Step 4：解压并移到项目目录

1. 找到 `archive.zip`，右键 → "解压到当前文件夹"（或用 7-zip）
2. 解压后会得到 `T1.csv`（约 5 MB）
3. **把 T1.csv 复制到这个路径**：

   ```
   C:\Users\wexco\coding\fowt-cable-ai\data\T1.csv
   ```

   如果 `data` 目录不存在，PowerShell 一行命令创建：
   ```powershell
   New-Item -ItemType Directory -Force -Path "C:\Users\wexco\coding\fowt-cable-ai\data"
   ```

---

## Step 5：告诉我"数据到位了"

之后我会：
1. 重新跑 `01_wind_data_eda.py`（这次会读取真实数据，而不是合成数据）
2. 自动生成 4 张新的真实数据 PNG
3. 重新生成 PPT，把合成数据图替换成真实数据图

---

## 验证方法（可选）

如果你想自己先确认数据到位，PowerShell 跑：

```powershell
Test-Path "C:\Users\wexco\coding\fowt-cable-ai\data\T1.csv"
```

返回 `True` 就是到位了。

或者看一眼文件头：

```powershell
Get-Content "C:\Users\wexco\coding\fowt-cable-ai\data\T1.csv" -Head 3
```

应该看到 `Date/Time,LV ActivePower (kW),Wind Speed (m/s),...` 这样的列名。

---

## 万一遇到问题

| 问题 | 解决 |
|---|---|
| Kaggle 注册不了 | 换用 Google 账号一键登录 |
| 下载按钮灰着 | 刷新一下、或换浏览器 |
| 手机号验证失败 | 换一个手机号、或用合成数据先发表（当前 PPT 用的就是合成数据） |
| 解压后没有 T1.csv | 文件名可能略有不同，找最大的那个 .csv 文件 |
| 路径里中文乱码 | 不影响，PowerShell 内部处理 UTF-8 |

---

## 不下载也能交差

如果你今晚来不及下载（或者 Kaggle 出问题），当前 PPT 里用的是**合成数据**，发表时**不要**提"Kaggle"——改成说：

> "I prepared a synthetic dataset that mimics the SCADA structure to validate the pipeline. Switching to the real Kaggle data is the next quick step."

这样不撒谎、且突出"我把流水线跑通了"是重点而非数据本身。
