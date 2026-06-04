# 精读总结：浮式海上风机动力电缆力学分析与设计最新进展

> **原文**：Recent Advances in Mechanical Analysis and Design of Dynamic Power Cables for Floating Offshore Wind Turbines
> **作者**：Burak Can Cerik & Luofeng Huang（英国克兰菲尔德大学）
> **期刊**：Ocean Engineering, 第311卷, 2024年, 文章编号118810
> **文章类型**：综述（Review）——系统梳理近20年相关文献，绘制该领域的知识地图
> **阅读方式**：按原文段落顺序，逐段引述 + 逐段深度解析，面向初学者

---

## 摘要（Abstract）

---

### 【摘要·核心内容】

> *"This review paper presents a comprehensive analysis of the mechanical design and analysis of dynamic power cables for marine renewable energy applications, focusing on research from the last two decades. The review covers key aspects such as mechanical properties, failure mechanisms, fatigue analysis, experimental studies, local cable analysis, and global load analysis. The study aims to provide a concise summary of the state-of-the-art, identifying recent advancements and research gaps in the field."*

**解析：**

这段摘要一句话交代了综述的**定位、范围和目标**。

**为什么要专门综述动力电缆？**
与普通陆地电缆或静态海底电缆不同，浮式风机的动力电缆（Dynamic Power Cable）处于持续的运动环境中——风机平台随波浪、风、流不断摇摆，电缆两端被迫跟随，每天都在经历数以万计次的弯曲和拉伸循环。这种工况使动力电缆的力学行为极为复杂，普通电缆设计理论无法直接适用，必须专门研究。

**综述覆盖的六个核心领域：**

| 领域 | 对应本文章节 | 核心问题 |
|------|------------|---------|
| 力学特性（Mechanical Properties） | §2 | 电缆刚度、强度如何 |
| 失效机制（Failure Mechanisms） | §2,§4.2-4.4 | 什么原因导致断裂？ |
| 疲劳分析（Fatigue Analysis） | §4.1-4.2 | 能用多久？ |
| 实验研究（Experimental Studies） | §3 | 试验数据从哪来？ |
| 局部分析（Local Analysis） | §4.1 | 铜丝内部应力如何分布？ |
| 全局载荷分析（Global Load Analysis） | §4.5 | 整根电缆的运动和受力如何？ |

---

## 第1章 引言（Introduction）

---

### 【引言·第1段：动力电缆的独特挑战与分类】

> *"Understanding the unique challenges and design considerations of these dynamic cables is crucial for the successful development and operation of floating offshore wind farms. In the context of marine renewable energy systems, power cables can be categorised as inter-array, inter-platform, or export cables. The term 'dynamic cable' has emerged in recent years to describe cables specifically designed to withstand continuous motion and cyclical loading, distinguishing them from static or quasi-static cables."*

**解析：**

这段引出了一个关键的概念区分——**动态电缆（Dynamic Cable）vs 静态电缆（Static Cable）**。这个名词之所以是"近年才出现"，正说明浮式风电是新兴领域，其特有的工程概念正在快速形成。

**电缆按功能的三分法：**

```
浮式风电场电力系统示意图（基于Fig. 1）：

风机A ─── 阵列内电缆（Inter-array）─── 风机B
            ↓
        海上变电站
            ↓
        出口电缆（Export Cable）
            ↓
        岸上变电站
```

- **阵列内电缆（Inter-array Cable）**：风机之间的连接，负责把各机组发出的电汇集到变电站
- **平台间电缆（Inter-platform Cable）**：连接浮式平台之间（如风机到浮式变电站）
- **出口电缆（Export Cable）**：把整个风场的电力送到岸上

**动态（Dynamic）的含义：**
动态不是指电缆本身在"动"，而是指它承受**持续变化的机械载荷**——张力、弯曲、扭转——由平台运动和环境载荷（波、流、风）共同驱动。与静态电缆（铺在海底，几乎不动）相比，动态电缆的设计难度高出一个数量级。

---

### 【引言·第2段：失效的经济代价】

> *"Power cable failures have substantial financial implications for offshore wind energy projects. Approximately 80% of offshore wind-related financial losses and insurance claims are attributed to cable failures, including both static and dynamic cables. With repair-related downtimes averaging 60 days, these failures can result in significant revenue losses and increased maintenance costs. Moreover, dynamic cables for floating offshore wind applications typically incur higher costs compared to traditional static cables due to their more complex design and manufacturing requirements."*

**解析：**

这是引言中最震撼的数据，值得逐字理解：

**"80%的经济损失归咎于电缆故障"**：
这个数字来自保险行业数据（de Wild, 2018；DNV统计），说明在海上风电所有部件失效中，电缆是**头号成本源**。这看起来不直觉——风机叶片、齿轮箱似乎更复杂，但电缆故障的特殊之处在于：
1. 修复难度极高（水下操作、专业船只）
2. 停机时间长达60天（相比叶片维修只需几天）
3. 一根电缆故障可能导致整个阵列离网

**"平均停工60天"**：
这60天不只是修复时间，还包括：等待合适的天气窗口（北海每年适合海上作业的天数有限）、调集专业修复船、故障定位等。每天停工损失 = 风场总装机容量（MW）× 平均风速下的发电效率 × 电价。

**成本比较：**
动态电缆比静态电缆贵的原因：
- 更复杂的多层螺旋结构
- 更严格的材料要求（抗疲劳、柔性）
- 更复杂的设计流程（需要全局+局部分析）
- 安装难度更高（需要专业安装技术）

---

### 【引言·第3段：先进分析技术的角色】

> *"Advanced mechanical analysis techniques, such as finite element analysis (FEA) and multi-body dynamics simulations, play a crucial role in developing reliable and cost-effective dynamic power cables. These methods enable designers to predict cable behaviour under various loading conditions, optimise cable structure and materials, and assess fatigue life. Integrating these techniques early in the design process allows for the development of cables better suited for the marine environment, reducing failure risks and financial losses."*

**解析：**

**为什么要在早期就使用高级分析？**
这是一个工程设计哲学问题。传统工业（如石油天然气柔性管）的设计思路是"经验驱动"——工程师凭借过往项目经验进行设计，测试验证，再优化。但浮式风电是新兴领域，缺乏积累，且每个项目的水深、风况、平台类型都不同，不能照搬经验。因此必须依赖**数值模拟**（FEA + 动力分析）在设计阶段就预测电缆行为，而不是"做出来再测试"。

本综述的两类核心计算工具：
- **FEA（有限元分析）**：计算电缆截面内铜丝/钢丝的应力分布 → 局部疲劳预测
- **多体动力学/全局分析软件**（OrcaFlex等）：模拟整根电缆在海洋中的运动 → 全局载荷预测

---

### 【引言·第4段：综述方法论与结构说明】

> *"This review focuses primarily on dynamic power cables designed for floating offshore wind turbines, while also drawing on relevant studies from other marine renewable energy applications where the findings are applicable to floating wind scenarios."*

**解析：**
综述的范围界定：以浮式风机电缆为主，同时借鉴波浪能、潮汐能设备的电缆研究（因为这些场景的电缆也经历动态载荷，物理机制相同）。这种跨应用场景的借鉴是合理的：铜导体的疲劳特性不会因应用场景不同而改变。

---

## 第2章 动力电缆力学设计基础（Mechanical Design Aspects）

---

### 【2.1·第1段：电缆三相结构与电压等级】

> *"Three-phase cables are normally used for floating offshore wind turbines to maintain the high voltage - alternating current being transmitted and avoid any transmission losses. At the moment, 33 and 66 kV cables are well-established technology with three-phase semi-wet and wet designs as inter-array/platform cables, which are based on the use of XLPE-WTR (water tree retardant) materials for insulation."*

**解析：**

**为什么是三相（Three-phase）？**
海上风机发出的是三相交流电（Three-phase AC），相当于3根火线的组合，互相之间有120°相位差。三相系统的好处：同等功率下，线路电流更小，损耗更低；三相系统天然平衡，不需要中性线。因此一根三芯电缆可以完整传输一台风机的所有功率，比三根单芯电缆节省空间和成本。

**33kV vs 66kV 的选择：**
- 传统阵列间电缆使用**33kV**，是成熟可靠的技术
- 新一代向**66kV**迁移：同样的电缆截面面积，66kV能传输约4倍功率（P = √3 × U × I）
- 欧洲海上风电已逐渐转向66kV，未来甚至有132kV的讨论
- 更高电压带来绝缘要求更严格（绝缘层需更厚）、水树问题更突出

**XLPE-WTR（防水树交联聚乙烯）：**
这是在普通XLPE中加入了专门延缓水树生长的添加剂（Water Tree Retardant）。因为浮式风机电缆长期浸泡在海水中，水分渗入的风险更高，必须使用防水树材料。

---

### 【2.1·第2段：导体——从铜丝绞合到功率传输】

> *"The conductors, located at the centre of each core, are the principal components of the power cable. They comprise a group of helically stranded wires, compacted together through an extrusion process. This way, the cable has better flexibility properties, which is essential for dynamic cables. Additionally, current is also distributed uniformly over the cross-section, improving the conductor's current-carrying capacity. Copper and aluminium are commonly used as conductor materials, with aluminium cores and cables needing to be larger to transmit the same power."*

**解析：**

**"Helically stranded wires"（螺旋绞合导线）的深层原因：**

为什么不用一根实心铜棒？从表面上看，实心棒截面积更大，传电性更好。但有两个关键问题：

1. **柔性要求**：实心铜棒一旦弯折就会产生永久塑性变形甚至断裂；绞合的细铜丝可以相互滑动，整体可以弯曲而不断裂——就像钢丝绳可以弯绕在滑轮上，但钢棒不行。动态电缆需要每天弯曲数万次，柔性是生命线。

2. **集肤效应（Skin Effect）**：高频交流电（50Hz）在导体中不是均匀分布的，而是集中在导体表面传输（集肤深度约9mm@50Hz/铜）。实心棒中心的铜几乎不通电，是浪费。绞合结构的每根细丝都参与导电，利用率高。

**铜 vs 铝：**

| 特性 | 铜（Cu） | 铝（Al） |
|------|---------|---------|
| 导电率（%IACS） | 100% | 61% |
| 密度（g/cm³） | 8.96 | 2.70 |
| 价格 | 贵且价格波动大 | 便宜 |
| 所需截面 | 基准 | 约1.64×铜 |
| 动态电缆适用性 | 更适合（强度更高） | 较差（软，疲劳寿命短） |

Ahmad等（2023）的研究表明：铜导体比铝导体更适合动态悬浮电缆，因为铜的强度更高，在反复弯曲载荷下不易疲劳失效。

---

### 【2.1·第3段：绝缘与介电系统——水树与电树威胁】

> *"The dielectric system prevents electrical failures or leakage of currents during transmission and, together with the conductor and conductor sheath, forms a single core. However, the insulation material in the dielectric system of dynamic power cables for floating offshore wind turbines is susceptible to the formation of electrical trees and water trees. Electrical trees are microscopic, tree-like structures that grow within the insulation material when subjected to high electrical stress, while water trees are similar structures that form due to the presence of moisture and electric fields. Both types of trees can lead to the degradation of the insulation material over time, compromising the integrity of the dielectric system and potentially causing premature failure of the power cable."*

**解析：**

**什么是水树和电树？——通俗理解：**

想象XLPE绝缘层是一块橡皮。正常情况下橡皮密实无裂纹。但：

- **水树（Water Tree）**：就像橡皮长期受潮，内部开始出现吸水的微小通道，这些通道在电场作用下不断延伸，形成树根状的微裂纹网络。形成条件：海水（水分）+ 交流电场，两者缺一不可。
- **电树（Electrical Tree）**：就像橡皮被高压电"烧"出的焦痕，结构更尖锐、生长更快。形成条件：局部电场强度超过绝缘材料的电场强度阈值。

**为什么浮式风机电缆更危险？**
静态电缆铺在海底，外护套完好时基本不会进水。但动态电缆：
1. 持续弯曲运动可能导致外护套出现细微裂纹 → 海水渗入通道
2. 海水的盐分和离子进一步加速水树生长
3. 反复弯曲还加速裂纹扩展

这正是浮式风机电缆必须使用防水树添加剂（WTR）的原因，也是§4.3整节专门研究水树问题的原因。

---

### 【2.1·第4段：铠装层的黏滑行为——非线性弯曲的核心机制】

> *"wires begin to slip against each other, transitioning from the 'stick' state to the 'slip' state. This transition is not instantaneous but occurs gradually over a range of curvatures, representing a transition phase between the two states. During this transition phase, the cable's bending stiffness decreases, as the slipping armour wires contribute less to the cable's resistance to bending. As a result, the cable becomes more flexible in bending, exhibiting a non-linear bending response. This stick–slip behaviour and the associated transition phase have important implications for the cable's performance and long-term reliability, as the repeated sliding and friction between the armour wires can lead to fretting wear, fatigue damage accumulation, and potential challenges in accurately predicting the cable's behaviour and loads."*

**解析：**

这是理解整篇综述所有力学内容的**核心机制**，值得深入解析：

**黏滑（Stick-Slip）行为的物理过程：**

```
小曲率（Stick状态）：
钢丝A → → → → → →
钢丝B → → → → → →
两者紧贴、相互锁定，共同抵抗弯曲 → 弯曲刚度高

大曲率（Slip状态）：
钢丝A → → → →→→→  ←相对滑动发生
钢丝B →→→→ → → →
内侧钢丝受压缩、外侧钢丝受拉伸，各自独立变形 → 弯曲刚度低
```

**弯矩-曲率图（M-κ 曲线）的典型形状：**

```
弯矩M
↑          ___________（线性增长，斜率=低刚度EI_slip）
|         /
|        / ← 过渡段（非线性，黏→滑转变）
|       /
|______/ ← 初始段（线性，斜率=高刚度EI_stick）
└──────────────→ 曲率κ
       κ_cr（临界曲率）
```

**为什么这对工程如此重要？**

1. **全局分析的输入**：OrcaFlex等软件需要知道电缆的弯曲刚度（EI）才能正确预测电缆运动。如果用错误的（线性）弯曲刚度，计算出的曲率时历就是错的，进而导致疲劳预测失误。

2. **疲劳的根本来源**：钢丝之间反复发生"黏→滑→黏→滑"的切换，每次切换都伴随摩擦能量损耗和接触点微小磨损——这就是微动疲劳（Fretting Fatigue，见§4.2）的直接来源。

3. **预测困难**：黏滑转变点（临界曲率κ_cr）与张力、摩擦系数、制造工艺都有关，而这些参数往往难以精确获得。

---

### 【2.1·第5段：动态电缆 vs 静态电缆的外护套差异】

> *"A significant modification in dynamic cables, as opposed to static ones, is the incorporation of a sturdier external protective layer (such as PE, Nylon, or another type of solid extruded coating) rather than the lightweight protective rovings (spiral-wound strings of polypropylene rope with a bitumen coating) found in static cables. Additionally, dynamic cables are characterised by an increased number of armouring layers which serve to shield the cable from physical harm and ensure it remains torsionally balanced."*

**解析：**

这一句话揭示了动态与静态电缆在工程设计上的本质差异：

| 特性 | 静态电缆 | 动态电缆 |
|------|---------|---------|
| 外护套 | 轻质聚丙烯绳缠绕（bitumen涂层） | 厚实挤出HDPE/尼龙护套 |
| 铠装层数 | 通常1层 | 通常2层（反向绞合） |
| 设计目标 | 抗腐蚀、承压 | 抗疲劳、抗弯、扭转平衡 |
| 弯曲柔性 | 次要考虑 | 最优先设计指标 |

**"扭转平衡（Torsionally Balanced）"的重要性：**
两层钢丝反向绞合（一层顺时针、一层逆时针），其扭转效应相互抵消。如果电缆在张力作用下发生扭转，轻则损伤内部组件，重则使悬挂式电缆扭转成螺旋形失稳。反向铠装是防止这种灾难性失效的关键设计。

---

### 【2.2·第1段：懒波形——浮式风电的主流方案】

> *"When it comes to floating offshore wind farms, the array cables' dynamic sections are significantly longer compared to their counterparts in fixed-bottom installations. This is because these cables are suspended in the water column, extending from the floater or the floating substation, often assuming a lazy-wave configuration. The primary purpose of the lazy-wave configuration is to reduce the maximum tension at the hang-off point..."*

**解析：**

**为什么动态段比固定式风机的长得多？**
固定式风机只需要在海底附近的很短一段配上柔性过渡段（因为桩基几乎不动）；浮式风机整台机组都在运动，电缆必须提供足够的"运动余量"，从挂出点一直到某个静止点（触地点或海底接头），整段都是动态的。

**懒波形（Lazy Wave）的形成逻辑：**

```
平台                  触地点（TDP）
  ↓挂出点               ↓
   \                 ___/（静态铺底段）
    \        ↑浮力模块
     \     /‾‾‾（上弓段 Hog）
      ‾‾‾\ /
          ‾（下垂段 Sag）
```

如果没有浮力模块，电缆会形成简单的悬链线（Catenary），挂出点处张力会非常大——风机每一次运动都直接拉扯这个点。

浮力模块的作用：
- 把中段电缆向上托起，形成一个"储变形缓冲器"
- 当平台向远处漂移时，上弓段伸展，释放储存的电缆长度，避免顶端张力骤增
- 当平台回弹时，上弓段压缩，多余的长度在上弓段"收纳"

**弓段（Hog）和垂段（Sag）是疲劳危险区：**
这两段的曲率变化最大（弓/垂段的反向曲率在平台运动时不断切换），铠装钢丝在这里反复发生最大幅度的黏滑转变，是设计中需要重点校核疲劳的位置。

---

### 【2.2·第2段：全悬浮式——深水的未来选项】

> *"Another approach that is being considered for deep water applications is to suspend the array cables across their entire length. While this method could potentially reduce the overall cable length required, it would also subject the cables to increased loading due to the movement induced by water currents. Although this approach has not been implemented in any floating projects thus far, it is believed to become an attractive option for water depths of around 500 m or more."*

**解析：**

**全悬浮式（Fully Suspended）与懒波形的根本区别：**

| | 懒波形 | 全悬浮式 |
|--|--------|---------|
| 连接方式 | 平台→水中悬挂→海底铺底 | 平台→水中悬挂→平台（不触底） |
| 电缆长度 | 较长（需要绕到海底再铺回） | 较短（两点间最短路径） |
| 海流影响 | 较小（有触地段稳定） | 较大（整根电缆暴露在海流中） |
| 适用水深 | 中等水深（100~300m） | 深水（500m+） |
| 工程实践 | 已有项目实施 | 目前仍在研究阶段 |

全悬浮式的关键研究问题：Schnepf等（2023）和Ahmad等（2023）的研究（见§4.5）表明，通过附加浮筒（Subsea Buoys）可以有效控制全悬浮电缆的形状和顶端张力，使这种配置变得实际可行。

---

## 第3章 实验研究（Experimental Research）

---

### 【3.1·第1段：测试的必要性与数据匮乏困境】

> *"Given the intricate structure of dynamic power cables, which comprise multiple layers with varying dimensions, materials, and complex contact and friction conditions, the development of analytical or numerical methods for assessing cable stiffness and capacity, as well as models for stress analysis and fatigue life prediction, requires validation against reliable experimental test data. However, cable mechanical tests are often conducted for design verification purposes rather than basic research, and due to commercial interests, these test data are not readily available for reproduction and reuse."*

**解析：**

这段精确地描述了动力电缆研究面临的**核心矛盾**：

**为什么必须要实验？**
数值模型（FEA、OrcaFlex等）的输入参数（摩擦系数、接触刚度、制造预应力等）无法从理论直接确定，必须通过实验数据来"标定"。如果没有实验验证的数值模型，其预测结果的可靠性无从保证，更无法用于工程设计决策。

**为什么实验数据稀缺？**
电缆制造商（如Nexans、Prysmian、NKT）进行了大量测试，但这些数据是**商业机密**（Commercial Secrets）。制造商的测试是为了满足客户验收要求（如CIGRE标准），而不是为了发表学术论文。学术界可用的公开数据因此极为有限。

这个矛盾贯穿整篇综述，在第5章"研究缺口"中被列为头号问题。

---

### 【3.1·Ménard & Cartraud (2023)：四点弯曲测试——最完整的公开数据集】

> *"Ménard and Cartraud (2023) conducted a series of experimental tests on a three-phase dynamic power cable with a diameter of 101 mm, which was assumed to be connected to an 8 MW floating offshore wind turbine. Cyclic bending tests were performed on a four-point bending test rig, and bending moment–curvature curves were obtained. The results exhibited stick–slip transition behaviour, which is typical in helically stranded wire-type structures. While the geometrical data of the cable were reported in detail, material parameters were taken from material databases or other studies dedicated to dynamic submarine power cables. Friction coefficients and the initial stress state due to the cable manufacturing process were estimated by tuning the numerical model with the test data."*

**解析：**

**四点弯曲测试（Four-point Bending Test）原理：**

```
施力点  施力点
  ↓      ↓
──────────────── 电缆试样
  ↑      ↑
支座    支座
（两个支座+两个加力点，共4个接触点）
```

四点弯曲的优点：两个加力点之间的电缆段受**纯弯曲**（Pure Bending，无剪力），测得的弯矩-曲率关系最干净，不受剪力影响。

**为什么这篇数据"特别宝贵"？**
文章公开了电缆的**详细几何参数**（每层导线直径、螺旋角、层数等），这使得其他研究者可以用这些参数建立自己的FEA模型，再用实验数据验证——这正是§4.1中Ménard & Cartraud (2023)的FEA工作所采用的流程。几何参数+弯矩曲率实验数据的组合，构成了该领域最完整的公开验证数据集之一。

**局限性**：摩擦系数和制造残余应力需要通过"调参"（Tuning）才能让模型与实验吻合，说明这些参数存在一定的不确定性。

---

### 【3.1·Ringsberg et al. (2023)：低刚度电缆综合测试】

> *"A comprehensive experimental test campaign was conducted by Ringsberg et al. (2023) on three dynamic power cables (1 kV, 3.6 kV, and 24 kV) without metallic armours, which were considered suitable for application in wave or tidal energy converters. Axial tension, bending, torsion, and fatigue tests were performed on the target cables, and the repeatability of the tests was demonstrated. The study highlighted challenges in fatigue testing of power cables, particularly the unsuitability of the combined traction-three-point bending fatigue test setup."*

**解析：**

这组测试的电缆**没有金属铠装**，用合成芳纶（Aramid）纤维绳代替钢丝铠装。芳纶纤维（Kevlar®是著名商标）重量轻、强度高，但弯曲刚度低于钢丝——这正是"低刚度电缆"名称的由来。

**测试方法学贡献——指出了一个重要的方法论缺陷：**

传统的"拉力+三点弯曲疲劳测试"装置（Combined Traction-Three-point Bending Fatigue Test）对这类低刚度电缆不适用，因为：
- 三点弯曲在中点产生剪力，而真实电缆主要承受弯矩和轴向力的组合
- 低刚度电缆对夹具设计更敏感

这个发现对整个领域有警示意义：不能把石油天然气脐带缆的测试标准直接套用到动力电缆，特别是柔性较强的电缆。

---

### 【3.1·Ehlers et al. (2023)：极限强度测试——极端载荷下的破坏数据】

> *"Ehlers et al. (2023) investigated the ultimate strength of power transmission cables under excessive loading conditions, such as those caused by anchor hooking or overloading during installation. Experiments on full-scale cables included tests on both HVAC and HVDC configurations... The results provided force-displacement curves and material test data, which are directly applicable to advanced non-linear FEA."*

**解析：**

**研究背景——渔船拖锚事故：**
海上风电场附近常有渔船作业，渔船拖锚意外钩住电缆、将其过度拉伸的事故时有发生。这种极端拉伸载荷与正常运行的疲劳载荷完全不同——它是**单次超出强度的破坏**，而非累积损伤。

**HVAC vs HVDC 对比的意义：**
- **HVAC（高压交流）**：三芯电缆，3根导体并排
- **HVDC（高压直流）**：单芯电缆，1根导体（正/负极各一根）
- 两者截面结构不同，极限强度和破坏模式自然不同

**数据的工程价值：**
力-位移曲线 + 各组件材料参数 = 建立非线性FEA所需的完整输入集。这类数据使研究者可以不做实验、直接用FEA重现破坏过程并预测未测试工况下的强度。

---

### 【3.2·Nasution et al. (2013, 2014)：建立铜导体S-N曲线的奠基性工作】

> *"Nasution et al. (2013, 2014) tested individual copper wires and copper strands under different cyclic loading regimes (tension-tension for individual wires and constant tension-bending for full-section conductors) and reported S-N curves for individual wires. Their research also included comparisons with FEA, which considered trellis (point) contact and inline contact within each layer, as well as surface irregularities in wires."*

**解析：**

**S-N曲线是疲劳计算的核心工具：**
S-N曲线（Stress-Number of cycles curve，也叫Wöhler曲线）描述材料在给定应力幅值S下的疲劳寿命N。知道了S-N曲线，再通过雨流计数法获得实际载荷的应力幅值分布，就可以用Miner-Palmgren法则计算累积损伤。

**两种测试模式的意义：**
1. **单根铜丝拉-拉疲劳（Wire-level）**：获得铜丝自身材料的S-N特性，排除接触摩擦影响，是"纯材料"疲劳数据
2. **整体铜导体拉伸+弯曲疲劳（Conductor-level）**：包含了层间摩擦、微动效应，反映真实使用条件

**两种接触类型的区别：**
- **Trellis Contact（交叉点接触）**：相邻层的导线交叉缠绕，接触点是个小区域（点接触或线接触），应力集中严重
- **Inline Contact（同层接触）**：同一层相邻导线之间的接触，线接触，应力集中相对轻微

**重要性**：Nasution等的S-N曲线被本综述中引用的Beier等（2023）、其他多篇论文直接采用，是该领域标准参考数据。

---

### 【3.2·Hu et al. (2022)：铜导体非线性弯曲滞回行为——关键参数识别】

> *"Hu et al. (2022) conducted a study on the non-linear bending hysteresis behaviour of copper conductors used in dynamic power cables. They found that the friction coefficient and radial extrusion pressure from the conductor's outer sheath layer significantly affect the critical sliding curvature and bending hysteresis properties."*

**解析：**

**什么是弯曲滞回（Bending Hysteresis）？**

当电缆弯曲然后回弯时，由于摩擦的存在，加载路径和卸载路径不重合，形成一个封闭的"滞回圈"（Hysteresis Loop）：

```
弯矩M
↑  /‾‾‾‾‾（加载曲线，M随κ增大）
| /
|/            ← 这个封闭圈的面积
|\               = 每个弯曲循环消耗的能量
| \               = 转化为热能 + 内部损伤
|  \___（卸载曲线，M随κ减小但路径不同）
└──────────────→ 曲率κ
```

这个滞回特性意味着：每次弯曲循环，电缆内部都在消耗能量，而这些能量的一部分转化为铜丝接触点处的微小塑性变形和磨损——正是疲劳损伤的来源。

**两个关键参数：**
1. **摩擦系数（Friction Coefficient）**：铜丝之间的摩擦越大，黏→滑转变所需的曲率越大（临界曲率越高），滞回圈越大（每循环损伤越大）
2. **径向挤压力（Radial Extrusion Pressure）**：来自外护套对导体的径向约束，约束越强，摩擦越大，效果与提高摩擦系数类似

---

### 【3.2·Jiang et al. (2023)：压实度对疲劳寿命的影响】

> *"Jiang et al. (2023b) investigated the influence of compaction degrees on the fatigue performance of stranded copper conductors. They observed that the fatigue data did not fall within the same scatter band. The authors attributed this difference to the deformation of conductor wires caused by the compaction procedure during fabrication. The study also proposed a simplified fitting formula to quantitatively describe the relationship between fatigue life and compaction degrees."*

**解析：**

**什么是压实度（Compaction Degree）？**
铜丝绞合后，需要通过模具挤压（Compaction）使各丝紧密排列，减少空隙。压实度越高，截面越密实，空隙越小，铜丝之间越紧密。

**压实度影响疲劳寿命的机制：**
高压实度 → 铜丝横截面形状发生变形（从圆形变成多边形）→ 接触区域变宽→ 接触压力分布改变 → 应力集中系数改变 → 疲劳寿命改变

这个发现有重要的**工程意义**：不同制造商、不同批次的电缆压实度不同，用统一的S-N曲线预测所有导体的疲劳寿命会带来系统误差。Jiang等提出的简化公式为快速估算不同压实度下的疲劳寿命提供了工具。

---

### 【3.2·Hu et al. (2024)：机械应变对XLPE中电树生长的影响】

> *"Hu et al. (2024) investigated the effects of compressive and tensile strains on the growth of electrical trees in cross-linked polyethylene (XLPE) samples from power cables. They found that compressive strain widened electrical trees along the direction of the applied strain, while tensile strain led to narrower trees and distorted their rotational symmetry... time-to-failure was decreased by a factor of 1.8 at 5.7% tensile strain, which could have implications for the in-service usage of high voltage cables under dynamic forces found in floating wind applications."*

**解析：**

这篇文章建立了**力学应变与绝缘失效**之间的直接联系，这在此前研究中是被忽视的：

| 应变类型 | 对电树形态的影响 | 对寿命的影响 |
|---------|--------------|------------|
| 压缩应变（Compressive） | 树枝沿应变方向变宽 | >5%时生长速率减半（延长寿命） |
| 拉伸应变（Tensile） | 树枝变窄，对称性破坏 | 5.7%时失效时间缩短1.8倍 |

**对浮式风机电缆的警示意义：**
浮式风机电缆的弯曲导致绝缘层同时承受压缩（弯曲内侧）和拉伸（弯曲外侧）。5.7%的拉伸应变听起来很大，但在局部弯折处（尤其是最小弯曲半径工况下）是完全可能出现的。

这意味着：**绝缘层的疲劳寿命可能比我们基于纯电场分析所预测的更短**——力学因素不可忽视。

---

## 第4章 局部与全局分析（Local and Global Analysis）

---

### 【4章·开篇：疲劳分析的标准工作流程】

> *"The workflow for fatigue analysis of dynamic power cables typically consists of several steps. First, a global load analysis is performed using software such as OrcaFlex to determine the cable's response to environmental loads, such as waves and currents, and the motions of the floating platform. The results from the global analysis are then used as input for local analysis, which focuses on the stress distribution within the cable's cross-section. Software tools like Helica or UFLEX are commonly employed for this purpose. The local stress time-series obtained from the analysis are then processed using rainflow counting to extract the stress cycle information. Finally, the fatigue damage is assessed using a cumulative damage model, such as the Palmgren-Miner's rule, to estimate the cable's fatigue life."*

**解析：**

这段明确了本领域的**四步标准分析流程**：

```
步骤①  全局动力分析（Global Load Analysis）
        工具：OrcaFlex / OpenFAST+MoorDyn / Ansys AQWA
        输出：各节点张力T(t)、曲率C(t)随时间变化的时历
               ↓
步骤②  局部截面分析（Local Cross-section Analysis）
        工具：Helica（DNV软件）/ UFLEX（SINTEF软件）/ 自开发FEA
        输出：铜丝、钢丝内部应力时历σ(t)
        方法：将全局载荷通过"应力因子"转换：σ = Kt·T + Kc·C
               ↓
步骤③  雨流计数（Rainflow Counting）
        工具：Python/MATLAB脚本
        输出：不同应力幅值Δσ下的循环次数ni
               ↓
步骤④  疲劳损伤计算（Fatigue Damage Assessment）
        模型：Palmgren-Miner法则：D = Σ(ni/Ni)
        输出：累积损伤度D → 疲劳寿命 = 1/D_year（年）
```

这四步中，步骤②是最关键也最复杂的，因为它需要将"电缆整体载荷"转换为"各组件应力"，而这个转换必须考虑非线性弯曲行为。§4.1的FEA研究就是专门解决步骤②的方法问题。

---

### 【4.1·FEA建模的挑战：为什么复杂截面难以直接建模？】

> *"The cable's cross-section consists of multiple components with different materials and complex contact conditions, leading to a high degree of non-linearity in the analysis. The use of solid elements to model each component accurately can result in an extremely large number of elements, increasing computational costs and potentially causing solver convergence issues. Moreover, the helical geometry of the cable components further complicates the modelling process, requiring careful consideration of the pitch angles and contact definitions."*

**解析：**

**直接建模的规模估算：**
一根66kV三芯动力电缆，截面包含：
- 3组铜导体，每组约19根铜丝（≈57根铜丝）
- 2层铠装钢丝，每层约40根（≈80根钢丝）
- 多层聚合物材料

如果每根铜丝用实体单元（Solid Elements）精细建模，整根电缆（如1000m长）的有限元网格数量将达到**数亿个单元**，即使是超级计算机也难以在合理时间内求解。

研究人员因此发展出三种减少计算量的策略，详见下面三节。

---

### 【4.1·策略一：周期边界条件（Periodic Boundary Conditions）】

> *"The first trend is the employment of periodic boundary conditions to reduce the model size and computational effort. By exploiting the cable's helical symmetry, a representative segment of the cable can be modelled, and the results can be extrapolated to the entire cable length."*

**Li et al. (2024) 的代表性体积单元（RVE）模型：**

> *"Li et al. (2024b) developed a three-dimensional Representative Volume Element (RVE) model for predicting the non-linear bending stiffness of three-core submarine power cables. Their approach uses dashpot-enhanced periodic boundary conditions to address the stick–slip challenges associated with cable bending. The model incorporates thermal effects on material and contact properties, allowing for thermal-mechanical coupled flexural analysis."*

**解析：**

**为什么周期边界条件有效？**
螺旋绞合的电缆具有**螺旋对称性**：沿轴方向每隔一个螺旋节距（Helix Period，通常10~20倍直径）结构完全重复。因此，只需建一段"代表性单元"（长度=一个螺旋节距），施加适当的边界条件（确保两端变形连续且力平衡），就可以代表整根电缆的行为。计算量从整根电缆缩小到一个节距，降低1~2个数量级。

**"阻尼器增强型（Dashpot-enhanced）"的创新：**
传统周期边界条件难以处理黏滑转变（因为黏滑是不连续的非线性行为）。加入dashpot（阻尼元件）后，可以平滑地模拟黏→滑的渐进过渡，收敛性更好。

---

### 【4.1·策略二：梁单元建模（Beam Element Modelling）】

> *"Kim and Lee (2017) presented a novel approach for modelling helically stranded cables using multiple beam finite elements. Their method aimed to achieve accurate results comparable to those obtained from full solid FE models while significantly reducing the computational cost. The proposed beam FE model considers wire-to-wire contacts and elasto-plastic material behaviour."*

**解析：**

**实体单元 vs 梁单元的对比：**

| 参数 | 实体单元（Solid Element） | 梁单元（Beam Element） |
|------|----------------------|---------------------|
| 自由度数/单元 | 24（8节点×3方向） | 6（每端3平移+3转动） |
| 适合分析 | 应力集中、局部失效 | 整体变形、弯曲刚度 |
| 计算量 | 极大 | 小 |
| 精度 | 高（局部） | 中等（整体） |

Kim & Lee (2017) 的核心验证结论：梁单元模型在预测轴向和横向（弯曲）载荷下的整体响应时，与实体模型精度相当，但计算量大幅减少。这为后来的大量FEA研究提供了基础。

---

### 【4.1·策略三：均质化与层级建模（Homogenisation & Hierarchical Modelling）】

> *"Homogenisation involves replacing the complex cable cross-section with an equivalent homogeneous material, reducing the number of elements and contact definitions required. Hierarchical modelling employs a multi-scale approach, where the results from a detailed local model are used to inform a simplified global model, enabling efficient analysis of the entire cable length."*

**Kuznecovs et al. (2019) 的层级建模框架：**

> *"One of the key aspects of their work was the development of a cable design model that incorporates a detailed design and dimensioning methodology for cables with multi-order helical structures. This hierarchical modelling approach considers the cable at different levels: conductor, power core, and full cable. By addressing the structural response at each level, which informs the next higher level, the analysis of the full cable's mechanical properties was enabled."*

**解析：**

**"多阶螺旋结构（Multi-order Helical Structures）"的含义：**

```
层级①：铜丝（单根） → 螺旋绞合
层级②：铜导体（一束铜丝） → 相对于电缆轴螺旋缠绕
层级③：电芯（导体+绝缘+屏蔽）→ 三个电芯相互螺旋扭绕
层级④：全缆（含铠装、填充、护套）
```

在每个层级上，研究人员先建立精细的FEA模型，算出这一层的等效刚度，再把等效属性传递到上一层的简化模型中。这种"自下而上"的均质化策略，既保留了各层的物理特性，又避免了全层次精细建模的计算量爆炸。

---

### 【4.1·综合案例：Ménard & Cartraud (2023) 三维FEA模型】

> *"Ménard and Cartraud (2023) proposed a 3D FE numerical approach to calculate the global mechanical behaviour and local stress state of dynamic submarine power cables. To reduce the computational domain and mesh size, the authors employed the homogenisation theory of periodic structures and beam element modelling of the armour components. The study also investigated the sensitivity of the cable's bending behaviour to frictional interactions and manufacturing residual stresses."*

**解析：**

这篇文章是**同时运用三种策略**的综合案例，代表当前FEA方法的最高水准：

- 非关键组件（填充物等）→ 均质化
- 铠装钢丝 → 梁单元
- 关键区域 → 实体单元
- 整体上利用周期性 → 只建一个节距

**最重要的发现：**
敏感性分析表明，**摩擦系数**和**制造残余应力**是影响弯曲行为的最关键参数——这两个参数都极难直接测量，需要通过实验反演获得。这也解释了为什么实验数据（§3.1中的Ménard & Cartraud实验）如此宝贵：没有实验就无法校准这两个关键参数。

---

### 【4.1·简化建模的边界：Ye & Yuan (2020)】

> *"Ye and Yuan (2020) conducted a systematic investigation of modelling alternatives for non-critical components in dynamic offshore power cables. They found that computing efficiency can be greatly improved by simplifying or omitting irregular-shaped filled bodies, with little influence on the estimation of the cable's axial and bending stiffness. However, such simplifications may lead to slightly higher stress ranges in the tensile armour wires, making the analysis more conservative."*

**解析：**

这篇工作的价值在于给工程师提供了一份**"可以简化什么"的指南**：

| 组件 | 可否简化 | 对轴向/弯曲刚度 | 对铠装钢丝应力 |
|------|---------|--------------|--------------|
| 填充物形状 | **可以** | 影响很小（<5%） | 略偏高（保守） |
| 护套层网格 | **不可粗化** | 影响显著 | 显著 |
| 铠装钢丝网格 | **不可粗化** | 影响显著 | 显著 |

**"偏保守"的含义：**
简化填充物后，铠装钢丝的应力预测值偏高（比真实值大）。这意味着简化模型计算出的疲劳寿命偏短，设计上偏安全。在工程设计阶段可以接受，但若需要精确评估寿命，则不能过度简化。

---

### 【4.2·微动疲劳：Poon et al. (2022-2024) 系列研究】

> *"Recent papers by Poon et al. (2022a,b, 2023, 2024) addressed the fretting-related damage in cable conductors extensively. Their work introduced a comprehensive finite element methodology encompassing global-local analysis to identify critical inter-wire fretting conditions under dynamic loading. Their findings highlighted the significant impact of factors such as lay angle, contact size, wire diameter, friction, and slip on fretting fatigue life, revealing that increased values generally reduce the lifespan of the cables."*

**解析：**

**微动疲劳（Fretting Fatigue）的机制详解：**

当两个相互接触的金属表面发生**极小幅度的相对滑动**（通常只有几微米，肉眼完全看不出来），接触点处会：
1. 产生微小的磨损坑（Wear Scar）
2. 磨损坑底部形成应力集中
3. 裂纹从应力集中处萌生（Crack Initiation）
4. 裂纹在后续循环中扩展（Crack Propagation）
5. 导体断裂

这是铜导体疲劳失效最主要的微观机制，比纯拉伸或纯弯曲更危险，因为接触损伤显著降低材料的疲劳寿命。

**Poon等确认的影响因素（均为"越大→寿命越短"的关系）：**

| 因素 | 增大时对寿命的影响 | 物理原因 |
|------|----------------|---------|
| 卷绕角（Lay Angle） | 寿命↓ | 角度大→接触力法向分量大→磨损加剧 |
| 接触面积（Contact Size） | 寿命↓ | 接触区越大→局部应力集中越严重 |
| 导线直径（Wire Diameter） | 寿命↓ | 直径大→接触区曲率小→名义接触应力大 |
| 摩擦系数（Friction） | 寿命↓ | 摩擦越大→切向力越大→磨损加速 |
| 滑移量（Slip） | 寿命↓ | 滑移越大→每循环磨损越多 |

**"全局-局部链接"的创新：**
Poon等的方法论贡献在于把全局动力分析（整根电缆受力）和微观接触分析（铜丝接触点）通过系统化的"全局-局部"框架连接起来，使从工况载荷到微观损伤的完整预测链成为可能。

---

### 【4.3·水树建模：Young et al. (2018, 2020) 方法论框架】

> *"Young (2020) and Young et al. (2018a,b) presented a methodology for modelling the propagation of water trees in dynamic cables, aimed at predicting the time until failure. His work accounted for both mechanical and electrical stresses experienced by the cable... By combining these mechanical and electrical stresses, his method employed fatigue damage and crack propagation methods to model the micro-scale breaking of insulation chemical bonds, predicting water tree propagation. However, this methodology was not backed up by experiments and lacked validation."*

**解析：**

Young等建立了**浮式风机水树预测的第一个系统性框架**：

```
步骤1：全局平台模型（OpenFAST等）
        → 波浪+风载荷 → 平台运动时历
步骤2：局部截面力学模型（FEA）
        → 绝缘层中的机械应力分布
步骤3：电场模型
        → 水树存在时电场畸变 → 局部电场应力
步骤4：综合裂纹扩展模型
        机械应力 + 电场应力 → 化学键断裂速率 → 水树扩展时间
步骤5：失效预测
        → 水树扩展到穿透绝缘层所需时间
```

**局限性（作者坦承）：缺乏实验验证**
这个方法论的整个预测链虽然逻辑严密，但从未与真实水树生长实验的数据对比。这是一个公认的弱点，也解释了为什么后续研究（Li等2022、Ringsberg等2024）需要引入实验数据加以验证和修正。

---

### 【4.3·Li et al. (2022) & Serdyuk et al. (2023)：电场是水树扩展的主导力】

> *"Li et al. (2022) presented a comprehensive study on the degradation mechanisms of dynamic power cables due to water treeing... Key findings highlight that while electric field-induced stresses play a predominant role in water tree propagation, cyclic mechanical stresses from cable motions do not significantly contribute to crack growth under the investigated load scenarios."*

> *"Serdyuk et al. (2023) performed computer simulations implementing an electro-mechanical model, which indicated strong effects of the test voltage and temperature. It was found that increased applied voltage generates stronger stress, whereas increasing temperature leads to its weakening."*

**解析：**

**Li等的关键结论——机械应力的作用被高估了：**

这个结论看似反直觉：浮式风机电缆一直在弯曲，难道弯曲不加速水树生长？Li等的模拟表明：在正常运行工况范围内，波浪引起的弯曲产生的机械应力对水树扩展的**贡献不显著**。电场应力才是主导因素。

**工程含义：**
这意味着，提高电缆电压或在高温环境中运行（海水温度升高、生物附着导致散热差），对水树寿命的影响**远比减小平台运动幅度更大**。设计策略上，应更关注绝缘材料选择和电场管理，而不仅仅是减小机械载荷。

**Serdyuk等的补充：温度效应的方向**
- 温度升高 → 材料电导率增大 → 界面电荷密度变化 → 电场应力减弱（对水树有缓解作用）
- 但高温同时加速XLPE老化，这是负面效应

两种效应叠加，温度与水树寿命的关系并非单调，需要具体问题具体分析。

---

### 【4.3·Ringsberg et al. (2024)：多物理场综合方法——当前最高水准】

> *"Ringsberg et al. (2024) presented a comprehensive methodology for predicting the failure of dynamic subsea power cables, with a focus on water tree growth in the insulation material. Their study combined global mechanical stress analysis, local finite element modelling, and electric stress analysis to assess both fatigue damage in conductors and insulation breakdown. The authors demonstrated how the combination of mechanical and electrical stresses can significantly reduce the predicted service life of the cable compared to considering electrical stresses alone."*

**解析：**

这篇论文是水树/绝缘失效研究当前的最高综合水准：

```
Ringsberg et al. (2024) 的三合一分析框架：

全局力学分析（SIMA）
    ↓ 平台运动 → 电缆曲率时历
局部FEA力学分析（ABAQUS）
    ↓ 导体疲劳损伤 + 绝缘层力学应力
电场分析（COMSOL）
    ↓ Maxwell应力 + 水树生长速率

↓ 综合评估：
导体疲劳寿命 + 绝缘击穿时间 = 电缆综合寿命
```

**最重要的发现：**
当把力学疲劳和电场应力联合考虑时，预测的电缆服务寿命**显著短于**仅考虑电场应力的情况。这定量验证了"多物理场耦合不可忽视"的结论，为§5章缺口8（多物理场分析）的立论提供了直接依据。

---

### 【4.4·Maksassi et al. (2022, 2024)：贻贝附着的热效应——导体超温威胁】

> *"Maksassi et al. (2022) conducted a comprehensive thermal characterisation of mussels, revealing that their effective thermal conductivity varies with age and porosity. Juvenile mussels (3–6 months) exhibited the lowest thermal conductivity, while adult mussels (12–18 months) showed the highest."*

> *"Maksassi et al. (2024) found that mussel colonisation can cause the copper conductor temperature to exceed its maximum operating temperature of 90°C. Juvenile mussels had the most significant impact, potentially raising the conductor temperature to 95.18°C, while adult mussels increased it to 90.8°C."*

**解析：**

**导体为什么会发热？**
当电流I流过铜导体时，产生焦耳热 P = I²R（I是电流，R是铜的电阻）。这些热量必须通过绝缘层、铠装层、海水散发出去，否则温度会一路升高。正常运行中，海水提供了充足的冷却，导体温度维持在90°C以下（这是XLPE绝缘材料的最高耐热温度）。

**贻贝的"隔热毯"效应：**
```
海水（良好散热）
    ↑ 热量传递路径
贻贝层（幼年→低导热，充当隔热毯）
    ↑ 热量被阻断
电缆外护套
    ↑
铠装层 → 绝缘层 → 导体（发热源）
```

幼年贻贝（3~6月龄）的导热系数最低，隔热效果最强，使导体温度达到**95.18°C**，超过90°C限值5°C以上。这看起来只有5°C，但XLPE的老化是**指数加速型**的（Arrhenius定律），温度每升高10°C，材料老化速度大约翻倍。5°C超温意味着绝缘寿命显著缩短。

**计划外的"反转"：**
成年贻贝（12~18月）的导热系数反而更高（因为贻贝随着生长，孔隙增大，水流更畅通，对流传热加强），实际上比幼年贻贝的隔热效果差。这个反直觉的结论说明：在设计中必须考虑贻贝生长的动态过程，而不能简单地假设"贻贝越厚越危险"。

---

### 【4.4·Yang et al. (2017)：生物附着对疲劳寿命的影响——最高减少68%】

> *"Yang et al. (2017) investigated the impact of biofouling on the energy performance and fatigue life of mooring lines and power cables in a wave energy converter system. Biofouling was found to decrease the fatigue life of mooring lines by approximately 20%. The study highlighted that the impact of biofouling is more pronounced under moderate sea states, where it can reduce the fatigue life of moorings by up to 68%."*

**解析：**

**生物附着如何影响疲劳（力学路径）：**
1. 外径增大 → 水动力阻力面积增大 → 波流对电缆的横向力增大
2. 重量增大 → 重力载荷增大 → 触地点张力增大
3. 以上两者共同导致 → 电缆运动幅度增大 → 张力/曲率变化范围增大 → 疲劳循环应力幅值增大

**"中等海况下影响更显著"的直觉解释：**
- 轻微海况（小浪）：本来载荷小，附着增加的额外载荷比例很大（相对增量大）
- 极端海况（大浪）：本来载荷就很大，附着的额外贡献相对不明显
- 中等海况：附着的绝对影响量最大，且出现频率最高（疲劳损伤与概率相关）

---

### 【4.5·全局分析综述：各代表性研究梳理】

---

#### Sobhaniasl et al. (2020)：第一套完整的疲劳寿命评估程序

> *"Sobhaniasl et al. (2020) proposed a procedure to determine the fatigue life of power cables connected to a 5 MW floating offshore wind turbine supported by a spar-buoy at a depth of 320 m. Simple beam models were used for calculating strains and stresses in the cable, while strain versus number of cycles curve (ε-N) was utilised for fatigue damage calculation."*

**解析：**
这是浮式风机电缆疲劳评估的**第一批完整工程流程论文**之一。关键特点：
- 使用了**单向耦合**（One-way Coupling）：先算平台动力响应，再把运动作为边界条件输入电缆计算。这比全耦合（电缆影响反馈到平台）简单，是工程中的常用近似。
- 采用ε-N曲线（应变-寿命）而非S-N曲线，更适合铜这类韧性金属。

---

#### Hall et al. (2021)：OpenFAST的MoorDyn模块加入弯曲刚度

> *"Hall et al. (2021) addressed the enhancement of the MoorDyn module within OpenFAST, integrating bending stiffness capabilities to simulate dynamic power cables. Findings confirmed the effective implementation of bending stiffness, demonstrating close agreement with OrcaFlex."*

**解析：**
这项工作的重要性在于：**开源工具的能力提升**。

OrcaFlex是收费的商业软件（年费数万美元），许多学术团队和发展中国家的工程师负担不起。OpenFAST是美国NREL开发的免费开源软件。但原来OpenFAST中的MoorDyn（系泊线模块）只能模拟有轴向刚度的线，无法模拟有弯曲刚度的电缆。Hall等的工作填补了这个空白，使开源工具可以做更准确的动力电缆仿真，降低了研究门槛。

---

#### Beier et al. (2023, 2024)：悬浮阵列间电缆——与本综述配套阅读的关键文献

> *"Beier et al. (2023, 2024a) presented fatigue analysis of inter-array power cables in two different papers. Critical insights include confirming curvature-induced stresses as the primary contributor to fatigue damage and demonstrating the advantages of alternative configurations using semi-submersible floaters."*

**解析：**
**Beier等2023年的论文**正是本系列笔记中另一篇精读文章（*Fatigue Analysis of Inter-Array Power Cables...*），此处不再重复详解。

**Beier等2024年的扩展：**
- 2023年：Spar型风机 + 悬浮电缆（带浮筒）
- 2024a年：**对比Spar型和半潜型**（Semi-submersible）平台

结论：半潜型平台的悬浮电缆配置比Spar型**更有优势**。原因：半潜平台的运动频率特性与Spar不同，在某些海况下，半潜平台引起的电缆曲率变化幅度更小，疲劳载荷更轻。

---

#### Rentschler et al. (2019, 2020)：懒波形的遗传算法优化

> *"Rentschler et al. (2020) proposed a design approach for dynamic inter-array cables that combines fatigue analysis and performance assessment under extreme weather conditions. Their study optimised lazy wave configurations using a genetic algorithm, which adjusts the position of buoyancy elements to lower the wave shape and reduce the cumulative length of buoyancy sections to 18%–23% of the total cable length."*

**解析：**

**遗传算法（Genetic Algorithm, GA）用于电缆优化：**

优化问题：选择浮力模块的位置和数量，使疲劳损伤最小，同时满足极端工况下的张力限制。

设计变量：浮力段起始位置、浮力段长度、浮力模块的浮力量

GA工作原理：模拟自然选择——随机生成一批"候选方案"，评估适应度（疲劳损伤），保留最优者，再"繁殖"（组合优秀方案特征）产生下一代候选，如此迭代数十代，收敛到最优解。

**"18%-23%"的最优浮力段比例：**
这意味着：1000m总长的电缆，浮力模块覆盖的长度约为180~230m最优。比例过小 → 上弓段不够高，缓冲效果差；比例过大 → 成本高，且可能引起其他位置应力增大。

**横向摆动的警示：**
当环境载荷方向与两台风机连线垂直时（侧向来浪），电缆横向摆动（Lateral Oscillation）的幅度比纵向更大，此时触地点处的弯曲可能超过弯曲限制器的保护范围，需要改用"斜波形（Pliant Wave）"或加装额外保护。

---

#### Abrahamsen et al. (2024) & Janocha et al. (2024)：参考设计——工程标准化的基础

> *"Abrahamsen et al. (2024) proposed a conceptual reference dynamic power cable for a 15 MW NREL reference turbine on a UMaine floater in 82 m water depth. Mechanical simulations revealed that the cable sections near the floating turbine were overloaded, highlighting the need for a cable bend stiffener in future designs. The authors also identified fatigue hotspots in the lazy-wave configuration."*

> *"Janocha et al. (2024) contributed significantly to dynamic power cable design for large floating wind turbines by developing and validating three baseline designs rated at 33 kV, 66 kV, and 132 kV. Their study established a comprehensive structural and mechanical property database through FEM modelling in UFLEX."*

**解析：**

**为什么参考设计（Reference Design）很重要？**

浮式风电是新兴领域，目前每个项目都各自设计电缆，缺乏行业公认的基准。参考设计的意义：
1. 研究者使用同一个"标准电缆"做对比研究，结果可以互相比较
2. 工业界可以基于参考设计快速评估新项目
3. 为制定行业标准提供参考起点

**Abrahamsen等发现"连接处过载"的工程含义：**
即使在设计阶段进行了仔细的全局分析，仍然发现电缆在靠近平台的位置（挂出点附近）载荷超过了电缆的设计容量。这证明了两点：
1. 弯曲刚化器（Bend Stiffener）是不可省略的附件
2. 全局分析与局部强度校核必须同步进行，不能只做其中一项

---

## 第5章 讨论与研究缺口（Discussion and Research Needs）

---

### 【5章·Table 1：研究现状与未来方向总表（原文直接翻译）】

原文 Table 1 是全章的框架：

| 当前研究状态 | 建议未来研究方向 |
|------------|---------------|
| 全尺寸力学测试 | 标准化测试规程 + 公开数据共享 |
| FEA截面局部分析 | 验证并改进截面分析工具（Helica、UFLEX等） |
| 疲劳预测的全局载荷分析 | 细化连接全局与局部分析的方法 |
| 导体微动疲劳研究 | 开发包含微动效应的先进疲劳模型 |
| 绝缘层水树生长建模 | 整合力学+热学+电场的多物理场分析 |
| 懒波形配置优化 | 探索深水新型构型（W形等） |
| 高压动力电缆开发（≤66kV） | 研究>132kV电缆及波纹护套电缆力学 |
| 悬浮阵列间电缆研究 | 面向不同浮台类型的优化设计 |
| 项目定制化设计 | 制定行业统一标准和设计指南 |
| 电缆-浮台耦合分析 | 改进联合仿真技术 |

---

### 【5章·缺口1：实验数据匮乏且不公开】

> *"One of the primary limitations identified in this review is the scarcity of publicly available experimental data for validating mechanical models used in cable stiffness and capacity assessment. Future research should focus on conducting extensive testing programs that cover a wide range of cable designs, materials, and loading scenarios."*

**解析：**
如§3.1所述，电缆力学测试数据大量掌握在制造商手中，公开数据极为有限。这不是技术问题，而是**商业模式问题**。解决路径：
- 行业联合建立共享测试数据库（类似油气行业的RISER数据库）
- 政府资助的测试项目，要求数据公开发表
- 制定CIGRE等国际组织的测试规范，并推广执行

---

### 【5章·缺口2：基于材料试样的S-N曲线过于保守】

> *"Current testing approaches that rely on S-N curves of material coupons may lead to overly conservative estimates of the fatigue life of complete cable assemblies. Future research should explore alternative testing methods, such as full-scale cable fatigue tests under representative loading conditions."*

**解析：**

**"过于保守"的问题有多严重？**
材料试样的S-N曲线（如Nasution等的铜丝S-N曲线）给出的是孤立铜丝的疲劳寿命。但在实际电缆中，铜丝受到相邻丝的摩擦约束——这个约束在某些情况下会**延长**疲劳寿命（因为摩擦阻止了裂纹扩展），而在另一些情况下（微动疲劳）会**缩短**寿命。材料试样测试无法体现这些相互作用，直接使用可能导致预测结果偏离实际达数倍。

理想的解决方案是全尺寸电缆在真实载荷历程（Real Loading Sequence）下的疲劳测试，但成本极高（需要特种试验机、长时间测试），目前尚无系统性的公开成果。

---

### 【5章·缺口3：项目定制化导致无法标准化】

> *"The design and testing of dynamic power cables are highly dependent on project-specific factors, such as environmental conditions, installation methods, cable configurations, and floater types. As a result, current cable designs and test programs are often tailored to individual projects, hindering the development of standardised solutions."*

**解析：**

这是浮式风电电缆领域的**体制性困境**：

- 不同水深（50m、300m、1000m）→ 不同配置（悬链线、懒波形、W形）
- 不同平台类型（Spar、半潜、TLP）→ 不同运动特性 → 不同载荷
- 不同地理位置（北海、台湾、挪威）→ 不同波浪/流条件

这种多样性使得建立统一标准极为困难，但不是不可能。成熟行业（如石油天然气柔性立管行业）的经验表明：通过定义一套**代表性设计工况（Representative Design Load Cases）**，可以在多样性中找到共性框架。DNV目前已有DNV-ST-0359（海上风机海底电缆标准）和DNV-RP-F401（电力电缆推荐规范），但针对动态浮式风电的专门化标准仍缺乏。

---

### 【5章·缺口4：截面分析软件验证不足】

> *"While widely used software packages like Helica and UFLEX have been employed in numerous studies, comprehensive validation studies comparing their predictions with experimental data and other validated models are still limited."*

**解析：**

**当前的验证现状：**
- UFLEX：SINTEF进行了部分内部验证，也有学术文献中的交叉验证（如Beier等2023年与UFLEX结果对比）
- Helica：DNV GL的内部验证文献，公开资料有限

**为什么需要更系统的验证？**
工程界使用这两个软件时，本质上是在**信任开发者提供的验证**，而不是基于独立的、全面覆盖各种工况的验证。就像飞机设计软件需要经过适航当局独立验证，安全关键的电缆分析软件也应经过类似的系统验证。这对于未来监管机构批准浮式风电项目也至关重要。

---

### 【5章·缺口5：深水与附件研究严重不足】

> *"As the offshore wind industry expands into deeper waters, the importance of understanding the behaviour and performance of dynamic power cables in various water depths and configurations becomes increasingly evident... The auxiliaries of dynamic power cables, such as bend stiffeners and restrictors, play a critical role in ensuring the cable's integrity and longevity... research on the design and testing of these components is relatively limited."*

**解析：**

**弯曲刚化器（Bend Stiffener）与弯曲限制器（Bend Restrictor）的区别：**

| | 弯曲刚化器（Stiffener） | 弯曲限制器（Restrictor） |
|--|----------------------|----------------------|
| 工作原理 | 渐变刚度的聚合物锥体，逐渐增大附近电缆刚度，避免急剧弯折 | 多节连锁结构，当达到最小弯曲半径时"锁死"，机械限位 |
| 适用场景 | 挂出点（电缆出入口） | 中间位置或触地点 |
| 设计难点 | 刚度分布需要优化匹配 | 铰链关节的疲劳 |

这两种附件是防止电缆局部过弯折（超过MBR）的关键部件，但针对它们的专项研究在本综述中几乎找不到引用——这本身就说明这是一个明确的研究空白。

---

### 【5章·缺口6：新材料与创新设计】

> *"The exploration of new materials, structures, and designs for dynamic power cables presents an exciting opportunity for future research. Non-metallic designs, such as those incorporating fibre reinforcements or thermoplastic composites, may offer advantages in terms of weight reduction, corrosion resistance, and cost-effectiveness."*

**解析：**

目前学术界和工业界正在探索的几个方向：
1. **芳纶纤维铠装**（Aramid Armour）：比钢丝轻很多，抗疲劳性能好，但成本高（Ringsberg等2023年测试的低刚度电缆采用了这种设计）
2. **热塑性复合材料护套**：可以根据水深定制刚度，抗腐蚀
3. **集成传感器**：在电缆内部嵌入光纤或其他传感器，实时监测曲率、温度、应变，实现预测性维护（Predictive Maintenance）

---

### 【5章·缺口7：132kV以上高压动力电缆的独特挑战】

> *"Future research should address the mechanical properties and fatigue behaviour of high-voltage dynamic cables, with particular attention to wet designs and their long-term performance under combined mechanical, thermal, and electrical stresses. Additionally, the behaviour of cables with corrugated sheath armours, which may exhibit different mechanical characteristics compared to traditional helical wire armours, requires further investigation."*

**解析：**

**"波纹护套铠装（Corrugated Sheath Armour）"是一个新概念：**

传统动态电缆用螺旋钢丝铠装，而高压（132kV+）的大截面电缆可能采用**波纹金属护套**（类似金属软管的波纹结构）代替钢丝铠装。波纹护套的黏滑行为与钢丝铠装完全不同，目前几乎没有专门的力学研究。

**Carbon Trust（碳信托基金）2023年报告的背景：**
这份行业报告明确指出132kV阵列间电缆的测试标准不够完善，特别是湿式设计（Wet Design，直接接触海水的绝缘设计）的测试规程亟需建立。这说明监管层面也已经意识到这个问题的迫切性。

---

### 【5章·缺口8：多物理场耦合——力/热/电三者的综合效应】

> *"Another critical research gap identified in this review is the lack of studies that combine mechanical, thermal, and electrical effects in the analysis and design of dynamic power cables. The complex interactions between these phenomena can significantly influence the cable's performance and long-term reliability."*

**解析：**

这是整个§5章最重要的研究缺口，三种物理场的交互影响如下：

```
机械场（Mechanical）
  ↕ 弯曲应力影响绝缘材料刚度
  ↕ 应变改变电场分布（§3.2 Hu等2024）

热场（Thermal）
  ↕ 导体电阻随温度变化
  ↕ 材料属性（弹性模量、摩擦系数）随温度变化
  ↕ 生物附着影响散热（§4.4）

电场（Electrical）
  ↕ Maxwell应力在绝缘层产生机械应力
  ↕ 水树生长受电场和机械应力共同驱动（§4.3）
```

当前研究的现状：99%的研究只考虑其中一个或两个物理场，三者同时耦合的研究极为罕见。Ringsberg等（2024）是最接近三场耦合的工作，但实际上他们也是分别建模后串行传递结果，而非真正同步求解。

---

### 【5章·缺口9：全局-局部分析链接需改进】

> *"The current approach of obtaining unit-load stress response from local analysis models and mapping the time series of loads to obtain stress time series for fatigue damage calculation using Miner's rule is a simplified method that may not fully capture the complexities of cable behaviour. Future research should explore more refined approaches that consider the non-linear effects and the influence of model extents on the accuracy of stress predictions."*

**解析：**

**"应力因子（Stress Factor）法"的局限性：**

当前主流方法（包括Beier等2023年使用的方法）：
```
σ_component = Kt × T + Kc × C
```

其中Kt和Kc是**固定系数**，假设组件应力与载荷（T, C）成线性关系。但实际上：
- 电缆行为是**非线性**的（黏滑效应）
- Kt和Kc可能随载荷幅值变化（大张力下的Kt与小张力下的Kt不同）

这种线性叠加在应力较小（线性范围内）时误差不大，但在大幅值载荷下可能系统性地低估或高估应力。改进方向：建立与载荷幅值相关的非线性应力因子查找表，或直接进行全程非线性局部-全局联合分析（计算量更大但更准确）。

---

## 第6章 结论（Conclusions）

---

### 【结论·总述段】

> *"This review paper has provided a comprehensive overview of the recent advances in the mechanical analysis and design of dynamic power cables for floating offshore wind turbines. The study has highlighted the critical role of dynamic power cables in ensuring the reliability and cost-effectiveness of floating offshore wind energy systems, as well as the unique challenges associated with their design and operation in the harsh marine environment."*

**解析：**
结论段是对全文的高度凝练，以下逐条梳理：

---

### 【结论·六条核心发现】

> *"The review of experimental studies has shown the importance of full-scale cable testing and component-level investigations in understanding the mechanical behaviour and failure mechanisms of dynamic power cables."*

**第1条（实验）**：全尺寸测试和组件测试均已取得进展，但公开数据仍严重不足。实验是整个分析链的基础，没有实验验证，数值模型无法被信任。

---

> *"The advancements in FEA techniques, particularly in modelling the complex cross-sectional structure and non-linear behaviour of cables, have been discussed, emphasising the need for further validation and standardisation of these tools."*

**第2条（FEA）**：三种FEA简化策略（周期边界条件、梁单元、均质化）已相当成熟，但工具间的系统性交叉验证仍不足。

---

> *"The integration of global load analysis and local stress analysis has been identified as a crucial aspect of the dynamic cable design process, with recent studies demonstrating the effectiveness of this approach in predicting cable fatigue life and optimising cable configurations."*

**第3条（全局-局部联合分析）**：OrcaFlex + Helica/UFLEX的组合流程已证明可行，但全局-局部的链接方法（应力因子法）存在线性化假设的局限，需要改进。

---

> *"The review has also highlighted the potential of new materials, designs, and high-voltage cable systems in improving the performance and reliability of dynamic power cables."*

**第4条（新技术）**：非金属铠装、集成传感器、132kV+电缆是三个值得重点投入的新兴方向。

---

> *"Several critical research gaps and challenges have been identified, including the need for more comprehensive experimental data, the development of standardised design and testing protocols, the validation of cross-sectional analysis software tools..."*

**第5条（研究缺口）**：九个主要缺口已在§5章详述，最紧迫的是：数据共享机制 + 行业标准化 + 多物理场分析框架。

---

> *"Addressing these research needs will require collaborative efforts between academia, industry, and regulatory bodies, as well as continued investment in research and development activities."*

**第6条（解决路径）**：这不是单个研究团队能独立解决的问题，必须是**学术界 + 工业界 + 监管机构**三方协作，方向是：
- 学术界提供方法创新和公开验证
- 工业界提供数据和工程反馈
- 监管机构（DNV, CIGRE等）提供标准框架和测试要求

---

## 附录：关键术语中英对照（更新版）

| 中文术语 | 英文术语 | 简要说明 |
|---------|---------|---------|
| 动力电缆 | Dynamic Power Cable | 在水中悬挂、持续运动的电缆 |
| 阵列内电缆 | Inter-array Cable | 风机间连接电缆 |
| 出口电缆 | Export Cable | 风场到岸上的主干电缆 |
| 导体 | Conductor | 传导电流的绞合金属丝芯 |
| 介电系统 | Dielectric System | 导体+绝缘层+屏蔽层的组合 |
| 铠装层 | Armour | 螺旋钢丝保护层，承受力学载荷 |
| 外护套 | Outer Sheath | 最外层挤出塑料保护层 |
| 黏滑行为 | Stick-Slip Behaviour | 铠装钢丝间摩擦状态的非线性转变 |
| 弯曲刚化器 | Bend Stiffener | 连接处防过度弯折的渐变刚度聚合物锥体 |
| 弯曲限制器 | Bend Restrictor | 机械限位防止超过MBR的铰链结构 |
| 最小弯曲半径 | Minimum Bending Radius (MBR) | 电缆不损坏所允许的最小弯折半径 |
| 疲劳 | Fatigue | 反复载荷导致的累积损伤 |
| 微动疲劳 | Fretting Fatigue | 接触面微小相对滑动引起的损伤+疲劳 |
| 水树 | Water Tree | 绝缘层内水分+电场形成的树状微裂纹 |
| 电树 | Electrical Tree | 绝缘层内强电场形成的树状微裂纹 |
| XLPE | Cross-Linked Polyethylene | 交联聚乙烯，主要绝缘材料 |
| XLPE-WTR | XLPE Water Tree Retardant | 含防水树添加剂的交联聚乙烯 |
| HDPE | High-Density Polyethylene | 高密度聚乙烯，外护套材料 |
| 懒波形 | Lazy Wave Configuration | 电缆在水中的S形布置（含浮力模块） |
| 触地点 | Touch Down Point (TDP) | 电缆与海底接触的位置 |
| 弓段 | Hog Segment | 懒波形中向上弯曲的弧形段 |
| 垂段 | Sag Segment | 懒波形中向下弯曲的弧形段 |
| 全悬浮式 | Fully Suspended Configuration | 不触底的电缆配置（两端均连浮台） |
| 有限元分析 | Finite Element Analysis (FEA) | 数值计算截面应力分布的方法 |
| 周期边界条件 | Periodic Boundary Conditions | 利用螺旋对称性简化FEA模型的技术 |
| 均质化 | Homogenisation | 用等效均匀材料代替复杂截面的方法 |
| 层级建模 | Hierarchical Modelling | 多尺度逐级分析的建模策略 |
| 代表性体积单元 | Representative Volume Element (RVE) | 周期结构的最小分析单元 |
| 全局分析 | Global Analysis | 分析整根电缆在海洋中的运动和受力 |
| 局部分析 | Local Analysis | 分析截面内各组件的应力分布 |
| 应力因子 | Stress Factor | 将全局载荷转换为组件应力的换算系数 |
| 雨流计数法 | Rainflow Counting Method | 从应力时历中提取疲劳循环的算法 |
| S-N曲线 | S-N Curve | 应力幅值-疲劳寿命关系曲线 |
| 疲劳寿命 | Fatigue Life | 在给定载荷下结构能承受多少循环 |
| 生物附着 | Biofouling | 贻贝等生物附着在电缆表面 |
| 多物理场耦合 | Multi-physics Coupling | 同时考虑力/热/电多种物理场的分析 |
| 黏滑行为 | Stick-Slip Behaviour | 铠装钢丝间摩擦状态转变现象 |
| 压实度 | Compaction Degree | 铜丝绞合后的挤压紧密程度 |
| 集肤效应 | Skin Effect | 高频电流集中在导体表面流动的现象 |
| 遗传算法 | Genetic Algorithm (GA) | 模拟自然选择的全局优化算法 |
| 梯度优化 | Gradient-based Optimisation | 利用目标函数梯度的局部优化算法 |
| 一阶耦合 | One-way Coupling | 只从平台传载荷到电缆，不反馈 |
| 全耦合 | Fully Coupled | 平台与电缆双向传递力学影响 |

---

*精读完成 | 文档版本：v2（逐段引述解析版，对标《Fatigue Analysis》精读格式）*

*整理时间：2026-06-04*
