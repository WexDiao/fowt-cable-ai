# 动力电缆文献知识总结 · Week1-2 追赶版

> 整理日期：2026-06-02 | 覆盖范围：综合学习计划 Phase 0（Week 1-2）
> 来源：Week1 已有笔记浓缩 + Week2-3 已下载 PDF（B-1/B-4/B-9/B-EX2/B-3）摘要级整合
> 用途：Phase 0 知识沉淀 + 下周（Phase 0 末段 + Phase 1 起始）入门基础

---

## Section A：Week1 笔记浓缩（B-2 WFO 白皮书 + 基础概念）

### A.1 固定式 vs 浮式 — 一段话讲清楚

固定式风机塔架固定海床（水深 <50-60m），电缆静态埋在海底，无反复弯曲疲劳问题。
浮式风机（FOWT）平台漂浮（水深 60-300m+），随波浪做 6DOF 运动，动力电缆必须跟随平台运动，反复承受弯曲/扭转/张力 → **疲劳成为主要失效模式**。

> 行业规模：2030 目标 305 GW，2033 目标 480 GW，相当于 6 年要把当前装机量翻 4 倍以上。

### A.2 三种构型对比表

| 构型 | 简图特征 | 优点 | 缺点 | 适用场景 |
|---|---|---|---|---|
| **悬链线（Catenary）** | 平台→自然悬垂→TDP | 结构简单、无附件 | TDP 张力大、疲劳寿命短 | 深水 + 平静海况 |
| **懒波（Lazy-Wave）★主流** | 下降段→Sag→浮力段→Hog→TDP | 浮力段隔离平台运动，TDP 疲劳寿命 ×3-5 | 需要浮力体 + 设计复杂 | 当前实际项目主流 |
| **W 形 / 双波（Double-Wave）** | 加第二浮力段，电缆完全悬浮不触底 | 浅水超越懒波，进一步降低张力/曲率 | 浮力体多、Hog Bend E 为新增疲劳热点 | 浅水（来自 B-4 量化结论） |

### A.3 四大疲劳热点（按严重程度排序）

| 排名 | 位置 | 失效力学机制 | 保护措施 |
|---|---|---|---|
| ★★★ | **Hang-off Point（挂接点）** | 平台运动直接传入、弯曲最剧烈 | Bend Stiffener（弯曲加强件） |
| ★★ | **TDP（触底点）** | 海床土摩擦 + Surge 反复移动 + 地质条件 | 沟槽 / 土壤参数研究 |
| ★ | **Sag Bend（下弯点）** | 浮力体边缘刚度突变 → 应力集中 | 浮力段端部柔性过渡 |
| ★ | **Hog Bend（上弯点）** | 同 Sag，刚度突变 | 同上 |

### A.4 电缆截面 4 个力学参数

| 参数 | 含义 | 设计影响 |
|---|---|---|
| **EI** 弯曲刚度 [kNm²] | 抵抗弯曲变形 | 决定电缆全局形态、Sag/Hog 位置 |
| **EA** 轴向刚度 [MN] | 抵抗拉伸变形 | 决定张力下的伸长量 |
| **GJ** 扭转刚度 [kNm²] | 抵抗扭转，铠装钢丝扭转-弯曲耦合 | Yaw 运动→扭转载荷传递 |
| **MBR** 最小弯曲半径 [m] | 绝缘层不被破坏的下限 | **设计底线** — 任何工况下不可低于 |

### A.5 故障统计

- 电缆故障 = **FOWT 总保险损失的 83%**（B-2 白皮书原文；B-1 引用为 80%）
- 平均维修时间 60 天；平均 4 次故障/寿命
- 故障原因占比（固定式经验，浮式可借鉴）：**安装 46%** / 制造 31% / 设计 15% / 外部损伤 8%

### A.6 行业规范 4 条

| 规范 | 内容 | 注意 |
|---|---|---|
| **DNV-ST-0359** | 海上风电海底动力电缆设计标准（★★★ 最重要） | 高压（>66kV）动力电缆条目薄弱 |
| **IEC 63026** | 海底动力电缆测试方法（60kV 以下） | 高压无对应 |
| **CIGRE TB 862** | 动力应用海底电缆机械测试推荐 | 偏机械实验 |
| **DNV-RP-F401** | 海底应用电力电缆 | 通用，含安装/运维 |

> **规范缺口量化（Carbon Trust 调查，引自 B-2）**：在 62 份相关技术文献中，只有 **6 份**直接适用于动力海底电力电缆（约 10%）。湿式静态 132kV、动态 132kV 均存在显著标准空白。

---

## Section B：Week2 文献摘要

### B-1 · Cerik & Huang (2024)
**标题**：Recent advances in mechanical analysis and design of dynamic power cables for FOWT
**期刊**：Ocean Engineering 2024 | 综述类
**关键词**：cable internal structure / global configuration / FEA local analysis / fretting & fatigue / experimental tests

**核心要点**：
- 这是过去 20 年动力电缆机械分析的系统综述。
- 把电缆分为 inter-array / inter-platform / export 三类，强调"dynamic cable"是指能承受持续运动+循环载荷的电缆。
- 引用 80% 损失归因于电缆故障的数字（DNV 2018），并明确：维修平均 60 天。
- **关键技术挑战**：高电压化（66kV→132kV）+ 动态电缆设计精炼，是浮式应用的两大方向。
- **方法学路线**：FEA 局部分析（横截面）+ 多体动力学全局分析；OrcaFlex / SIMA / Moordyn 为代表性全局工具；UFLEX / Helica 为局部工具。
- **铜导体疲劳**专题（Nasution 系列、Poon 系列）作为内层"卷绕铠装-导体"摩擦疲劳关键参考。

**与你研究的对接点**：
1. 综述里识别的"研究空白"包括：高保真度局部模型 + 高效全局模型的耦合策略 → 你的 ML 代理模型方向直接对接这一空白（用 ML 当"高效层"）。
2. 引用的 Beier 2024a/b 两篇都是"suspended cable"（悬挂阵列电缆），是 B-9 / B-EX3 的同一团队作品 → 你将来跟踪 University of Stavanger Muk Chen Ong 组的产出。

### B-4 · Zhao et al. (2021)
**标题**：A comparison of two dynamic power cable configurations for a FOWT in shallow water
**期刊**：AIP Advances 2021（CC-BY 开放）
**核心数字**：2021 论文，已比早期 catenary 研究升级到 **lazy-wave vs double-wave** 对比，三峡集团 + 上海勘测设计研究院联合。

**核心要点**：
- 在 SIMO/RIFLEX 中建了 fully-coupled FOWT-cable 模型（aero-hydro-servo-elastic）。
- 推导了 double-wave（双波）的参数化几何表达。
- 雨流计数 + 应变-寿命曲线（strain-cycle）评估铜导体疲劳。

**6 条主要结论**（直接抄要点）：
1. Double-wave 在压缩缓解、抗弯能力、疲劳表现上**均优于** lazy-wave。
2. Lazy-wave 和 double-wave 两种构型**挂接点（hang-off）都是疲劳最严重位置**。
3. Double-wave 新增 **Hog Bend E**（第二弧的上弯点）作为另一个潜在疲劳失效位置。
4. **弯矩**是铜导体疲劳的主要贡献量（不是张力）。
5. Double-wave 第二弧设计建议：**位置更低、弧度更小**。
6. VIV 疲劳、ancillary 附件保护（bend-stiffener / bend-restrictor）暂未纳入，是后续工作方向。

**与你研究的对接点**：
- 弯矩主导疲劳 → 你 ML 代理模型的输出量首选「热点弯矩」而非张力。
- Lazy-wave 挂接点疲劳最严重 → 训练数据矩阵优先覆盖 (Hs, Tp, 悬挂角度) 三参数。

---

## Section C：Week3 文献摘要

### B-9 · Beier, Schnepf, Van Steel, Ye, Ong (2023)
**标题**：Fatigue Analysis of Inter-Array Power Cables between Two FOWTs Including a Simplified Method to Estimate Stress Factors
**期刊**：J. Marine Science and Engineering 2023, 11, 1254（MDPI 开放）

**核心要点**：
- 研究 **suspended inter-array cable**（两台 spar-type FOWT 之间的悬挂式电缆 + 浮力块）。
- 工具组合：**OrcaFlex 11.2d**（全局动力 + 疲劳）+ Python 3.10（脚本驱动）+ **UFLEX 2.8**（横截面应力因子）。
- 海况：北海典型环境条件。
- **提出"简化应力因子估算法"**：基于复合梁应力理论 + MBR，无需 FEM 就能得到初步估算，与 UFLEX 对比验证。

**4 条疲劳分析关键发现**：
1. 简化法对**纯拉伸**载荷给出的应力因子准确；对**叠加曲率**载荷给出**保守**结果（偏安全）→ 适用于初步设计阶段。
2. Suspended 构型在所示条件下**疲劳寿命非常长**（低循环载荷）。
3. 关键疲劳区域**位于挂接点和浮力块旁边**；**弯曲是疲劳主要贡献**（再次验证 B-4 结论）。
4. 海洋生物附着对疲劳寿命影响小（因大部分电缆位于无附着深度）。

**疲劳分析 5 步流程**（结合 B-9 整理，可直接用于 Phase 1）：
```
Step 1：OrcaFlex 时域仿真（3h，0.05s 步） → 输出热点处弯矩 M(t)
Step 2：横截面分析（UFLEX 或简化复合梁理论） → 应力因子 σ/M
Step 3：Rainflow 计数 → 应力幅 (Δσ_i, n_i) 分布
Step 4：S-N 曲线查表（DNV-RP-C203）→ 各幅值疲劳寿命 N_i
Step 5：Miner 线性叠加 → D = Σ(n_i / N_i)；设计要求 D < 1/DFF（DFF=10）
```

### B-EX2 · Holcombe et al. (2025)
**标题**：Experimental–numerical model comparison of a dynamic power cable for a FOWT
**期刊**：Ocean Engineering 2025

**核心要点**：
- **物理实验：1:70 水槽比尺**（Plymouth COAST 实验室海洋盆），模拟全尺度 70m 水深。
- FOWT 模型：IEA 15MW + UMaine VolturnUS-S 半潜平台。
- 电缆模型：**tethered wave 系绳波**构型；用 Froude 相似律设计，材料按 EA / EI 目标尺缩选取。
- 测量：Qualisys 光学跟踪 7 个标记点的轨迹；同步运行 OrcaFlex 数值模型（用实测物理参数喂入，做"like-for-like"对比）。

**两种海况**：
| 工况 | Hs [m] | Tp [s] | γ | 时长 |
|---|---|---|---|---|
| 运行海况 | 1.8 | 9.1 | 1 | 1 h |
| 1/50 年风暴 | 12 | 14.4 | 2.6 | 1 h |

**主要发现**：
- 数值模型整体能很好捕捉电缆运动响应；低频区域（约 0.07 Hz = 平台 surge 共振）吻合最好。
- **平台运动是电缆运动主导**：通过 hang-off 传递（运行海况下 99% 能量来自 FOWT 运动；风暴下风暴海况下 63% 能量来自波浪）。
- 加速度峰值上 OrcaFlex 普遍**预测偏小**，sag bend 和 hog bend 处差异明显。
- 直接波浪载荷不可忽略，需在数值模型中精确建模。

**对你研究的启示**：
- 1:70 缩比 + Froude 相似律 → 如果未来要做模型实验，参数选取直接抄。
- 平台运动主导 → 你的 ML 代理模型若以"浮体 6DOF 时序"为输入，是合理的物理选择（验证了 CNN-GRU 输入设计）。

### B-3 · Janocha, Ong, Lee, Chen, Ye (2024)
**标题**：Reference Power Cable Models for Floating Offshore Wind Applications
**期刊**：Sustainability 2024, 16, 2899（MDPI 开放）；隶属 **IEA Task 49 WP2 Reference Power Cable Design**

**核心贡献**：发布 **33 / 66 / 132 kV 三档参考电缆**的完整结构与力学参数数据库，直接可用于 OrcaFlex 全局响应仿真。

**参数总表（直接抄成 Excel 用）**：

| 参数 | 33 kV | 66 kV | 132 kV | 单位 |
|---|---|---|---|---|
| **EA**（轴向刚度） | **622** | **658** | **846** | MN |
| **GJ**（扭转刚度） | **125** | **152** | **250** | kNm² |
| EI（弯曲刚度，bi-linear） | 见原文图 12 | 见原文图 12 | 见原文图 12 | kNm² |
| 外径（无浮力段） | — | **184** | — | mm |
| 单位重量（空气中） | — | **547** | — | N/m |
| 外径（带浮力段） | — | **390** | — | mm |
| 单位重量（带浮力段） | — | **948** | — | N/m |

> 注 1：EI 在论文中只给出 bi-linear 关系图（图 12），无单一数值。设计时按 **stick stiffness**（小曲率段斜率）和 **slipping stiffness**（大曲率段斜率，称"nominal"）两段取值。
> 注 2：外径/重量论文只列出 66kV 数值在 case study，33/132kV 需查表 5 或论文附图。下周读 PDF 时补全 33 / 132 完整外径行。

**材料属性表**：

| 材料 | 密度 [kg/m³] | 弹性模量 [MPa] | 泊松比 | 摩擦刚度 [MPa/mm] | 摩擦系数 |
|---|---|---|---|---|---|
| Copper | 8890 | 112,200 | 0.34 | 1500 | 0.30 |
| Steel | 7800 | 200,000 | 0.26 | 2000 | 0.20 |
| XLPE | 925 | 1000 | 0.40 | 1200 | 0.25 |
| MDPE | 956 | 1000 | 0.40 | 1200 | 0.46 |
| HDPE | 980 | 1000 | 0.40 | 1500 | 0.10 |
| PPY | 895 | 150 | 0.40 | 1500 | 0.10 |

**Case study 设置（可直接复用）**：
- OC3-Hywind spar FOWT（5MW 参考机），转子直径 126m，hub 高 90m，spar draft 120m，3 根系泊，水深 200m
- 电缆：66 kV，全长 530m，懒波构型，挂接点位于 SWL 下 30m
- OrcaFlex 11.3a，0.05s 时间步，FEM beam 单元 530 段（每段 1m）
- 3 次随机种子 × 每次 3h 时长

**关键洞察**：
- 该参考电缆的存在显著降低了未来工作"造电缆模型"的工作量 — 直接套用即可。
- 论文同时报告："动力电缆对浮式风机响应特征影响不显著"（即 cable→FOWT 耦合反馈弱），简化分析可只算 cable-only 响应。

---

## Section D：跨周/跨方向知识关联

### D.1 与 C-3 立管方向共通方法（基于 Week1 笔记 §12 扩展）

| 共通项 | B-4 动力电缆 | C-3 深水立管 |
|---|---|---|
| 流体力公式 | Morison Equation（细长体） | Morison Equation |
| 疲劳流程 | OrcaFlex + Rainflow + Miner | OrcaFlex + Rainflow + Miner |
| 4 疲劳热点位置 | 挂接点 / Sag / Hog / TDP | 挂接点 / Sag / Hog / TDZ |
| 工具栈 | OrcaFlex + UFLEX | OrcaFlex + SHEAR7 |

### D.2 电缆独有问题（立管无）

1. **电气绝缘老化**：水树（Water Treeing）、电树（Electrical Treeing）
2. **MBR 约束**：最小弯曲半径作为设计底线
3. **触底点土反力**：海床土壤参数（吸附力、摩擦系数、地质条件）影响疲劳
4. **双层铠装**（动态需双层、静态只需单层）
5. **Yaw 运动 → 铠装扭转-弯曲耦合**

---

## Section E：缺失文献清单（待用户下载）

> 优先级标注：★★★ Phase 0-1 必读 | ★★ Phase 1-2 建模与对比 | ★ Phase 2-3 ML 代理模型

### Phase 1：OrcaFlex 建模 + 疲劳深化（**本周优先下载**）

| 代号 | 标题 | 年份 | 优先级 | 状态 | 链接 |
|---|---|---|---|---|---|
| **B-5** | Dynamic power cable layout for 15MW FOWT: Part 1（OrcaFlex 建模细节） | 2025 | ★★★ | ✗ 缺 🟢 开放 | https://www.joet.org/journal/view.php?doi=10.26748/KSOE.2025.014 |
| **B-6** | Dynamic power cable layout for 15MW FOWT: Part 2 ULS | 2025 | ★★ | ✗ 缺 🟢 开放 | https://www.joet.org/journal/view.php?doi=10.26748/KSOE.2025.024 |
| **B-7** | Power cable dynamics at different water depths | 2025 | ★★ | ✗ 缺 🟡 机构账号 | https://www.sciencedirect.com/science/article/abs/pii/S0951833925002217 |
| **B-8** | Key parameters for inter-array cable configurations | 2025 | ★★ | ✗ 缺 🟢 开放 | https://www.mdpi.com/2077-1312/13/5/875 |
| **B-EX1** | DNV-ST-0359: Subsea Power Cables for Wind Power Plants（规范，常翻） | 2022 | ★★★ | ✗ 缺 🟡 DNV 账号 | https://www.dnv.com/services/subsea-power-cable-certification-services-for-offshore-wind/ |
| **B-EX3** | Reliability analysis of FWT dynamic cables under realistic loads | 2023 | ★★ | ✗ 缺 🟢 开放 | https://doi.org/10.1016/j.oceaneng.2023.114594 |

### Phase 2：AI/ML 代理模型（次优先，4 周后用）

| 代号 | 标题 | 年份 | 优先级 | 状态 | 链接 |
|---|---|---|---|---|---|
| **B-13** | CNN-GRU 预测动力电缆动力响应（R²=0.9864）⭐ 核心复现对象 | 2024 | ★★★ | ✗ 缺 🟡 | https://www.sciencedirect.com/science/article/abs/pii/S0951833924001333 |
| **B-14** | Data-driven surrogate for real-time fatigue monitoring of mooring lines | 2024 | ★★★ | ✗ 缺 🟢 开放 | https://wes.copernicus.org/preprints/wes-2024-162/wes-2024-162.pdf |
| **B-18** | AI in FOWT: design, monitoring, control — comprehensive review | 2025 | ★★ | ✗ 缺 🟢 开放 | https://www.mdpi.com/1996-1073/18/22/5937 |
| **B-15** | CNN-LSTM-ATT + Chebyshev 系泊张力预测 | 2025 | ★★ | ✗ 缺 🟡 | https://www.sciencedirect.com/science/article/abs/pii/S0029801825010406 |
| **B-16** | Attention-MLP 可解释 FOWT 动力响应预测 | 2025 | ★★ | ✗ 缺 🟡 | https://www.sciencedirect.com/science/article/pii/S002980182501409X |
| **B-17** | ML 自动系泊故障检测（15MW FOWT，hull sensors） | 2025 | ★★ | ✗ 缺 🟡 | https://www.sciencedirect.com/science/article/pii/S0141118725004298 |

### 已下载（确认在手）

| 代号 | 状态 |
|---|---|
| B-2 WFO 白皮书 2024 | ✓ week1/WFO-Cables-and-FOSS-White-Paper.pdf |
| B-1 Ocean Engineering 综述 | ✓ week2/Recent advances...pdf |
| B-4 lazy vs double-wave | ✓ week2/A comparison of two...pdf |
| B-9 Fatigue 简化应力因子 | ✓ week3/Fatigue Analysis...pdf |
| B-EX2 实验-数值对比 | ✓ week3/Experimental–numerical...pdf |
| B-3 参考电缆参数库 | ✓ week3/Reference Power Cable Models...pdf |
| 上田 D3 修論 2023 | ✓ 202303_修論_上田雄大.pdf |

**反馈给用户：** 上述 12 篇缺失文献中，**B-5 / B-EX1 / B-13 / B-14** 这 4 篇是 Phase 1-2 直接卡点，建议优先去链接下载（其中 B-EX1 DNV 规范需要研究室账号或购买）。

---

## Section F：Phase 0 自测对照（5 题 + 参考答案要点）

> 摘自 Week1 笔记 §自测清单，给出可参照的答案要点供你自查。

### Q1：手绘懒波电缆示意图，标注 5 个位置
**要点**：从平台向下 → 自由悬垂段 → **Sag Bend（下弯点）** → **浮力段**（装 Buoyancy Module）→ **Hog Bend（上弯点）** → 触底段 → **TDP（触底点）** → 静态延伸至变电站；**Hang-off Point（挂接点）** 在最顶端。

### Q2：懒波为什么比悬链线疲劳寿命长 3-5 倍？
**要点**：浮力段如同弹性缓冲器，平台 6DOF 运动经过 Sag-浮力段-Hog 这一"S 形"二次反射后能量大幅衰减；到达 TDP 的循环弯矩幅值显著降低。同时浮力体提供静态支撑，减少 TDP 处的张力均值。两个效应叠加 → S-N 曲线对应寿命 ×3-5。**B-4 论文进一步证明双波在此基础上再优化**。

### Q3：4 个疲劳热点及失效机制
- 挂接点：平台运动直接传入 → 弯矩最大
- TDP：海床摩擦 + Surge 反复移动 → 拖曳-反弹疲劳
- Sag/Hog Bend：浮力段端部刚度突变 → 应力集中

### Q4：EI / EA / MBR 的含义
- EI：弯曲刚度，决定全局形态与共振频率
- EA：轴向刚度，决定张力下的伸长
- MBR：最小弯曲半径，**设计底线**（DNV-ST-0359 强制），超过则绝缘损伤
- （额外）GJ：扭转刚度，关系到 Yaw 运动下的扭转-弯曲耦合（B-3 数据：33kV=125 / 66kV=152 / 132kV=250 kNm²）

### Q5（加分）：固定式电缆故障原因占比最高的是哪个？对浮式启示？
- **安装 46%**（最高）→ 启示：浮式风电要从一开始建立严格的安装质量控制流程；触底敷设、悬挂调试都是高风险窗口。

---

## 下周（Phase 0 末段 + Phase 1 起始）锚点任务

> 不在本文件做策略调整，仅列锚点供参考。详细评估见文件 3。

1. **B-3 参数数据库**全文精读，补全 33/132kV 的外径与重量
2. **B-9 疲劳 5 步流程**画完整图（Step1-5 + 5 工具）
3. 申请 OrcaFlex / Particle Works 许可证（提前期未知，应尽快发邮件）
4. 下载 Phase 1 4 篇关键文献（B-5 / B-EX1 / B-13 / B-14）
5. 联系河岸さん 邮件草稿

---

*整理日期：2026-06-02 | 用于 2026-05-19 起两周计划追赶 | 下次更新建议：Phase 1 Week 3 末（约 06-09）*
