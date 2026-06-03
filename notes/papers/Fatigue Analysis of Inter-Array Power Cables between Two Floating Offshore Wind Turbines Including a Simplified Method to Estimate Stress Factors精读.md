# 论文逐段精读笔记

> **论文：** Fatigue Analysis of Inter-Array Power Cables between Two Floating Offshore Wind Turbines Including a Simplified Method to Estimate Stress Factors
> **作者：** Beier D., Schnepf A., Van Steel S., Ye N., Ong M.C.
> **期刊：** J. Mar. Sci. Eng. 2023, 11, 1254
> **阅读方式：** 严格按原文段落顺序，逐段引述 + 逐段深度解析，面向基础薄弱的读者

---

## 摘要（Abstract）

---

### 【摘要·第1句】

> *"The use of floating offshore wind farms for electrical energy supply is expected to rise significantly over the coming years."*

**解析：**
作者用一句话交代了整篇文章最大的时代背景——**浮式海上风电的大规模发展是未来趋势**。为什么要特别提"浮式（floating）"？因为传统的海上风电机组是把桩打入海底固定的（bottom-fixed），只能建在水深60米以内的浅水区。而全球真正丰富的风资源往往在水深超过60米的深海区域，这些地方无法打桩，必须用浮式结构。所以"浮式"是海上风电走向深远海的关键技术。

---

### 【摘要·第2句】

> *"Suspended inter-array power cables are a new design to connect floating offshore wind turbines (FOWTs) with shorter cable lengths than conventional setups."*

**解析：**
这句话引出了本文研究的具体对象——**悬浮式阵列间动力电缆（Suspended Inter-Array Power Cable）**。

先拆解术语：
- **Inter-array（阵列间）**：风电场内部风机与风机之间的连接，不是连接到岸上的输出电缆。
- **Suspended（悬浮）**：电缆悬挂在水中，**既不触碰海底，也不触碰海面**。
- **Conventional（传统）**：传统做法是把电缆铺在海底。

为什么悬浮式更短？传统海底电缆必须铺得很长，因为两台风机都在运动，如果电缆太紧就会被拉断，所以要留出"余量"让电缆弯曲缓冲。悬浮式电缆直接在水中悬挂，两端附在风机上，不需要绕道海底，**几何路径本身就短**。

---

### 【摘要·第3–5句】

> *"The present study investigates the fatigue life of a suspended power cable with attached buoys connecting two spar-type FOWTs. Typical environmental conditions for the North Sea are applied. The nonlinear bending behavior of the power cable is considered in the analysis."*

**解析：**
这三句话交代了本文的**研究对象、研究场景、关键物理特性**：

1. **研究对象**：带有浮筒（buoys）的悬浮电缆，连接两台Spar型浮式风机。
   - **Spar型**：一种细长圆柱形浮式平台，深吃水（约120m），靠下方配重保持稳定，类似一根竖立的铅笔漂在水中。
   - **浮筒（Buoys）**：附在电缆中段的大型浮球，提供额外浮力，防止电缆过度下垂，同时减小电缆两端的张力。

2. **研究场景**：北海典型环境条件。北海以风浪条件恶劣著称，是全球海上风电发展最成熟的区域，用北海条件做分析具有代表性。

3. **非线性弯曲（Nonlinear bending）**：这是电缆力学中一个重要而复杂的特性。普通的梁或杆弯曲时，弯矩与曲率成正比（线性关系）。但动力电缆内部有多层螺旋缠绕的铜丝和钢丝，弯曲时各层之间会相互**摩擦、挤压、滑动**，导致小曲率时很硬、大曲率时变软——这就是非线性。如果忽略这一特性，计算出的疲劳损伤会有严重误差。

---

### 【摘要·第6–8句】

> *"Fatigue assessment is performed using the numerical software OrcaFlex based on stress factors obtained from cross-section analysis. An effective method for obtaining the stress factors is proposed for early engineering design stages and compared with the finite element software UFLEX simulation results. The simplified method delivers similar results for axial tension loads and conservative results for bending loads compared with results obtained from the finite element software."*

**解析：**
这三句话是全文**第一个创新点**的说明：

**什么是应力因子（Stress Factor）？**
疲劳分析的核心是计算电缆内部各组件（铜导线、铠装钢丝）的应力。但OrcaFlex做全局动力分析时，只能输出电缆整体的**轴向张力T**和**弯曲曲率C**，无法直接得到铜丝里面的应力。"应力因子"就是一个换算系数，把整体载荷（T和C）转换成各组件的局部应力：

```
铜丝应力 = Kt × 张力T + Kc × 曲率C
```

**本文的创新**：提出了一种**简化方法**，在没有有限元软件的情况下，用解析公式直接估算Kt和Kc。结果表明：
- 对**张力载荷**：简化方法与有限元结果几乎相同 ✓
- 对**弯曲载荷**：简化方法比有限元偏高（保守侧），适合初步设计 ✓

---

### 【摘要·最后2句】

> *"Stress components resulting from curvature variation are identified as the main contributors to fatigue damage. The most critical locations along the power cable for fatigue life are close to the hang-off points."*

**解析：**
这是全文**最重要的两个结论**：

1. **弯曲是主要疲劳原因**：电缆受到的拉伸力虽然也会产生应力，但波浪让浮式风机不断摇摆，引起电缆反复弯曲，这个弯曲产生的应力幅值比拉伸大得多，是导致疲劳积累的主要机制。

2. **Hang-off点是最危险位置**：所谓Hang-off点，是电缆从浮式平台引出的出口位置（类似插头从插座引出的地方）。风机在波浪中不断运动，这个出口位置的电缆既被固定约束，又跟着平台晃动，每次晃动都产生弯曲变化——这里的曲率变化幅度最大，因此疲劳损伤最严重。

---

## 第1章 引言（Introduction）

---

### 【引言·第1段】

> *"To achieve the goal of limiting global warming to 1.5°C set by the United Nations in the Paris Climate Agreement, renewable energy sources, including wind energy, must be extended in the future. Since offshore locations have vast wind potential and are not as constrained by populated or protected areas as onshore locations, particularly offshore wind farms, they are expected to grow substantially. While most offshore wind farms are bottom-fixed platforms installed in shallow waters, a few projects are already implemented in deeper waters, such as the floating wind farms Hywind Scotland, WindFloat Atlantic, and Hywind Tampen. In all implemented projects, the power cables connecting the FOWTs are laid on the seabed. However, the power cables can also be suspended, which means they are submerged but do not touch the seabed. These suspended configurations can reduce the length compared to cables laying on the seabed. This length reduction has the advantages of reduced inter-array energy loss and lower investment costs for the power cables. This work analyzes the fatigue damage of suspended inter-array power cables between two floating offshore wind turbines using a stress factor-based fatigue analysis approach."*

**解析：**
这一段是论文的**宏观背景和研究切入点**，信息量很大，逐句拆解：

**"1.5°C目标 → 风能必须扩展"**
《巴黎协定》是2015年全球196个国家签署的气候协议，核心目标之一是将全球平均气温升幅控制在1.5°C以内。要达到这个目标，到2050年全球必须实现净零排放，风能是最主要的替代能源之一。

**"陆上受限 → 海上有潜力"**
陆上风电面临：居民投诉（噪音、视觉影响）、土地稀缺、自然保护区限制等问题。海上风速更大更稳定，面积广阔，是理想的风能开发地。

**"浅水 → 深水：固定式 → 浮式"**
现有已运营的海上风电几乎都是固定桩基式，适用水深通常在30~60m。但水深超过60m后打桩成本急剧上升，必须改用浮式平台。作者提到了三个已建成的浮式风电场：
- **Hywind Scotland**（2017年，全球首个，苏格兰）：水深95~120m，5台2.3MW风机
- **WindFloat Atlantic**（2019年，葡萄牙）：水深100m，3台8.4MW风机
- **Hywind Tampen**（2022年，挪威）：水深260~300m，11台8.6MW风机

**关键信息：这三个项目的电缆全都铺在海底！**

**"但电缆可以悬浮"**
这里作者提出了一种不同于现有实践的新思路：让电缆悬浮在水中，不触底。优点很具体：
- 更短的电缆 → 减少阵列间的电力损耗（电缆越长，电阻越大，损耗越大）
- 更少的材料用量 → 降低采购和安装成本

**"本文研究什么"**
全段结尾一句明确了本文的研究任务：**用应力因子方法，分析悬浮阵列间电缆的疲劳损伤**。

---

### 【引言·第2段（悬链线与懒波形电缆综述）】

> *"Ikhennicheu et al. [7] published various offshore dynamic power cable configurations connecting a floating platform and the seabed. The most common dynamic cable configurations described in the literature are the catenary and lazy-wave shapes. The lazy-wave shape distinguishes itself from the catenary shape through buoyancy modules attached to the hanging power cable."*

**解析：**
这段介绍了**两种最常见的动态电缆形状**，是理解本文研究背景的重要铺垫：

**悬链线形（Catenary Shape）：**
顾名思义，电缆像链条一样自然下垂，形成一个弧形。上端连接浮式平台，下端铺到海底。这种形状完全由重力和浮力决定，不需要额外附件，但缺点是：当平台大幅运动时，顶端张力会非常大。

**懒波形（Lazy-wave Shape）：**
在悬链线的中段附加若干**浮力模块（Buoyancy Modules）**，使电缆形成一个"S形"或"懒散波浪形"的轮廓。这些浮力模块把电缆中段向上托起，使顶端（挂出点处）的张力大幅减小，同时电缆能"储存"更多的变形余量，来缓冲平台运动。

```
悬链线（Catenary）：       懒波形（Lazy-wave）：
浮式平台                   浮式平台
   |                          |
    \                          \
     \                          ≈≈≈浮力模块拱起
      \                        /
       \____海底____          /
                          ___/海底
```

**与本文的关系：** 本文研究的是两端都连接浮式平台的"悬浮式"电缆，与上述两种连接平台到海底的配置有本质不同，这也是为什么说本文研究是新颖的。

---

### 【引言·第3–6段（相关文献逐一介绍）】

> *"Thies et al. [8] analyzed a dynamic umbilical's tension and fatigue life in lazy-wave and catenary configurations connecting a wave energy converter with a static power cable at the seabed. They showed that the lazy-wave configuration reduces the maximum tension and the number of fatigue cycles in the dynamic umbilical compared with the catenary configuration. A reduction in the maximum tension resulted in a significant extension of the fatigue life of the dynamic umbilical."*

**解析：**
这段引用Thies等人（2012年）的工作，研究对象是**波浪能转换器（Wave Energy Converter, WEC）**的脐带缆。关键结论：懒波形比悬链线**张力更小、疲劳寿命更长**。这为后来的悬浮电缆研究提供了思路——通过改变电缆形状来改善其动力特性。

> *"Thies et al. [9] obtained the tensions and fatigue of a 66 kV cable connecting a FOWT to the seabed in a lazy-wave shape. The platform's motion was the main contributor to the loads on the umbilical."*

**解析：**
同一作者组（2019年）研究了**66kV电缆**（注意：这与本文使用的电缆规格相同）在懒波形配置下的张力和疲劳。关键结论：**平台运动是电缆载荷的主要来源**，海流和波浪直接作用于电缆的力相对次要。这一发现对本文也适用——浮式平台的六自由度运动（前后、左右、上下平移 + 横摇、纵摇、偏航旋转）驱动电缆不断运动，产生循环载荷。

> *"Rentschler et al. [6] presented a design optimization method for inter-array cable configurations for FOWTs. Their study included an estimation of the fatigue life, the performance in extreme weather conditions, and selected economic parameters for lazy-wave power umbilical configurations."*

**解析：**
Rentschler等（2019年）做了**阵列间电缆配置的优化设计**，同时考虑疲劳寿命、极端天气表现和经济参数。这是为数不多同时涉及阵列间电缆（而非平台到海底的脐带缆）的研究，与本文研究场景最接近，但他们研究的是懒波形，不是悬浮式。

> *"Bakken [10] calculated the fatigue life of a dynamic power cable connecting a FOWT to the seabed using the numerical programs SIMA and Bflex. The lowest fatigue life occurred at the locations with the maximum tension range, and the main contributors to the fatigue of the copper conductor were local friction effects."*

**解析：**
Bakken（2019年，硕士论文）使用SIMA和Bflex两套软件分析电缆疲劳。他发现**铜导体的疲劳主要由内部摩擦效应引起**，而不是简单的轴向拉伸。这进一步说明电缆内部的摩擦接触是疲劳分析中不可忽视的因素。

---

### 【引言·第7–10段（电缆弯曲行为与疲劳机理文献）】

> *"Hu et al. [11] investigated the bending behavior of a copper conductor inside a dynamic power cable experimentally and numerically. They stated that the nonlinear bending of the power cable is the main factor leading to fatigue failures."*

**解析：**
Hu等（2022年）这篇文章非常重要，因为本文在计算非线性弯曲行为时直接引用了他们的结论。他们通过**实验和有限元双重方法**，验证了铜导体的非线性弯曲特性，并明确指出这是导致疲劳失效的**根本原因**。直觉上理解：如果电缆弯曲是线性的（弯一点给一点力），则循环载荷引起的应力可以精确估算；但因为非线性（一开始弯曲很难，后来渐渐容易），每次弯折的应力分布是复杂的，必须通过实验或数值方法才能获得。

> *"Prediction models for the fatigue of dynamic power cables were developed by Svensson [12] using experiments and finite element simulations. Interlayer friction forces were an important factor in the calculation of the fatigue life of the power cable."*

**解析：**
Svensson（2020年，硕士论文）进一步量化了层间摩擦力的贡献，证明忽略摩擦会导致疲劳寿命被高估。本文在敏感性分析中也专门对比了"含摩擦"与"不含摩擦"两种有限元模型（见结果第3.2节）。

> *"Zhao et al. [13] studied the behavior and fatigue of power cables in lazy-wave and double-wave configurations connected to a FOWT in shallow water. They detected the hang-off point as the most critical point regarding the tension and fatigue of the power cable for both shapes."*

**解析：**
Zhao等研究了两种形状（懒波形和双波形）在浅水中的电缆疲劳，发现**Hang-off点是两种形状下共同的最危险位置**。这与本文最终结论相呼应——无论何种电缆配置，挂出点都是设计重点。**双波形（Double-wave）** 是在懒波形基础上再加一段拱起的变体，文中提到双波形的第二段浮力区也是疲劳危险点。

> *"Ballard et al. [14] estimated the fatigue life of a lazy-wave-shaped umbilical attached to a wave energy converter. Curvature-induced fatigue was identified as the critical parameter in their setup, causing fatigue damage."*

**解析：**
Ballard等（2020年）明确指出：**曲率变化引起的疲劳是关键**。这与本文的结论完全一致，可以说本文是对这一规律在悬浮电缆配置上的进一步验证。

---

### 【引言·第11段（铜导体疲劳特性的专门研究）】

> *"The general fatigue properties of a copper conductor inside a dynamic subsea power cable were determined by Karlsen et al. [15]. They suggested using strain-cycle curves for copper conductors due to the limited applicability of traditional S–N curves for this material. Marta et al. [16] assessed a dynamic power cable's stresses and fatigue life at floating offshore renewable energy installations. Fretting was identified as a major crack initiation mechanism in copper conductors, causing fatigue failure. The governing failure mode in all their cases was fatigue. Nasution et al. [17] established the S–N curve of a copper conductor of power cables used in offshore wind farms through experimental data and finite element simulations. Nasution et al. [18] assessed the effects of tension and bending loads on copper power conductors. They identified inter-layer friction caused by curvature as the main reason for fatigue failures."*

**解析：**
这一段集中介绍了**铜导体疲劳特性**的专项研究，包含几个重要知识点：

**Karlsen等的争议：S-N曲线 vs 应变-寿命曲线（ε-N曲线）**
- **S-N曲线（应力-寿命曲线）**：传统疲劳分析工具，横轴是循环次数N，纵轴是应力幅值S。适用于高周疲劳（循环次数 > 10⁴~10⁵）。
- **ε-N曲线（应变-寿命曲线）**：用应变而不是应力来描述疲劳，更适合低周疲劳和弹塑性材料。
- Karlsen认为铜是韧性较强的金属，传统S-N曲线对铜的适用性有限，建议用ε-N曲线。
- **本文的选择**：仍然使用S-N曲线，理由是工程界主流做法如此，而且电缆制造商（如Nexans）通常只提供S-N曲线数据。

**Fretting（微动磨损/微动疲劳）**：
Marta等发现，铜导线在弯曲时，相邻铜丝之间会发生**极小幅度的相对滑动（微动）**，这种微动会在接触点产生微小的磨损坑，成为裂纹萌生的起始点，大幅降低疲劳寿命。这解释了为什么铜导体比光滑均质金属棒更容易疲劳——内部的接触摩擦是加速失效的内因。

**Nasution等（2012, 2014年）**：
通过大量实验建立了海上风电用铜导体的S-N曲线（本文直接使用），并证明曲率引起的层间摩擦是疲劳失效的主要原因。

---

### 【引言·第12段（悬浮电缆的先行研究）】

> *"Yang et al. [19] presented the dynamic motions and fatigue damage of a power cable connecting a wave energy converter to a static hub in a freely hanging catenary configuration. They calculated a long fatigue life for a simplified cable, disregarding internal effects such as wear or fretting. Suspended power cables between FOWTs were described by Rapha and Domínguez [20]. Schnepf et al. [21] performed feasibility studies for different suspended power cable configurations. They identified configurations with buoys as more suitable than configurations with buoyancy modules. The behavior of a suspended power cable connecting a FOWT with a floating production storage and offloading unit (FPSO) was analyzed by Schnepf et al. [22]. The results showed that suspended configurations with buoys attached evenly over the power cable length could reduce its tension compared to a freely hanging configuration and a configuration with buoys attached to its middle section. Ahmad et al. [23] proposed a design method for suspended inter-array power cable configurations between two FOWTs. They concluded that attaching several buoys leads to lower maximum tensions in the power cable and that copper conductors might be more suitable for suspended power cables than aluminum conductors."*

**解析：**
这段是与本文**最直接相关**的先行研究。逐篇解读：

**Yang等（2018年）**：
研究了波浪能转换器的自由悬挂悬链线电缆，但**忽略了内部磨损和微动效应**，得到了过于乐观的疲劳寿命。本文研究类似的悬浮配置，但要更严格地考虑内部效应。

**Rapha和Domínguez（2021年）**：
首次描述了浮式风电场中浮机间悬浮电缆的概念，但只是概念性描述，没有详细的力学分析。

**Schnepf等（2023年，参考文献[21]，与本文作者重叠）**：
对不同悬浮电缆配置做了**可行性研究**，发现用**浮筒（Buoys）比用分布式浮力模块（Buoyancy Modules）更合适**。
- 浮力模块缺点：均匀分布在电缆上，增加水动力阻力；
- 浮筒优点：几个集中的大浮球，安装简单，效果好。
本文正是基于这一发现，选择了带浮筒的配置。

**Schnepf等（2023年，参考文献[22]，与本文作者重叠）**：
研究了悬浮电缆连接浮式风机与FPSO（海上浮式生产储油平台）的场景。发现把浮筒**均匀分布**在电缆全长上，比集中放在中段更能降低顶端张力。

**Ahmad等（2023年，与本文作者重叠）**：
提出了两台浮式风机之间悬浮电缆的设计方法，并得出：
- 多个浮筒→最大张力更小（本文配置采用3个浮筒）
- **铜导体比铝导体更适合悬浮电缆**（铝虽然更轻，但强度更低，动力响应下更容易失效）

---

### 【引言·第13段（研究空白的明确指出）】

> *"To the authors' knowledge, no work has yet been performed assessing the fatigue of a suspended power cable. Analyzing the fatigue life of a suspended power cable due to dynamic loading is important for identifying possible design optimizations and ensuring the reliability and cost-effectiveness of the proposed setup. Additionally, no study has yet been published on a simplified method to obtain stress factors for calculating the fatigue of power cables."*

**解析：**
这段是整篇引言的**核心，也是本文存在意义的直接说明**，点明了两个研究空白：

**空白1：悬浮电缆的疲劳从未被研究过**
前面引用了大量文献，但它们研究的都是"平台—海底"电缆的疲劳，或者只是对悬浮电缆做了静力/准静力分析。**没有人研究过悬浮阵列间电缆在动态载荷下的疲劳寿命**——这正是本文填补的空白。

**空白2：没有简化的应力因子估算方法**
现有文献计算应力因子都依赖UFLEX或Bflex等专业有限元软件，门槛高、耗时长。**在工程设计初期，没有一种快速估算的方法**——这是本文的第二个贡献。

---

### 【引言·第14段（论文结构说明）】

> *"This work is organized as follows: Section 2 describes the software used, the setup of the FOWTs and the connecting suspended power cable in deep water, the environmental conditions applied, and the fatigue assessment. Section 3 presents and discusses the results of the stress actor calculations and the fatigue analyses of the case study. Conclusions are drawn in Section 4."*

**解析：**
这是标准的论文结构说明段，告知读者：
- 第2章：方法（软件、模型、工况、计算流程）
- 第3章：结果与讨论
- 第4章：结论

没有特别的技术内容，但有一个注意点："stress actor"是原文中的一个小印刷错误，应为"stress factor"（应力因子）。

---

## 第2章 方法论与数值设置（Methodology and Numerical Setup）

---

### 【2.1节·第1段：OrcaFlex介绍】

> *"The present study uses the numerical software OrcaFlex version 11.2d in combination with Python v3.10. This software can perform global static and dynamic analyses of marine systems, including analyses of the behavior of wind turbines. A time-domain solution procedure determines the interactions between floating structures and the environmental loads (including wave, wind, and current loads). Moreover, fatigue calculations can be carried out based on the results of dynamic simulations. Line structures such as power cables can be modeled with finite elements."*

**解析：**
**OrcaFlex**是英国Orcina公司开发的海洋工程分析软件，是全球浮式结构分析领域的主流工具之一。逐句解析：

**"global static and dynamic analyses"（全局静力和动力分析）**
- **静力分析（Static）**：计算系统在静止状态下的平衡位形（如：电缆在自重和浮力下的悬挂形状）
- **动力分析（Dynamic）**：考虑时间变化的运动，计算在波浪、风、流等环境载荷作用下系统随时间的运动响应

**"time-domain solution procedure"（时域求解）**
时域方法的意思是：把时间切成很小的步长（本文每步0.1秒），一步一步往前推算系统的状态。这与频域方法不同（频域是用频率空间的数学变换直接求统计结果）。时域方法更精确，但计算量更大。

**"Python v3.10 combination"**
OrcaFlex支持Python脚本自动化操作，本文使用Python批量运行30个工况×6个方向=180次仿真，并自动后处理数据。

**"Line structures modeled with finite elements"（线结构用有限元建模）**
电缆在OrcaFlex中被离散化成一段一段的有限元单元，每段有自己的质量、刚度、阻力等属性，相邻段通过节点连接。单元越短，结果越精确，但计算量越大。本文在危险的挂出点附近使用0.1m的细密单元，在中段使用1.0m的粗单元，这是一种计算效率优化。

---

### 【2.1节·第2段：UFLEX介绍】

> *"The finite element software UFLEX version 2.8 is used to determine cable properties. The software assumes that the problem is two-dimensional with respect to tension and torsion, while bending loads, including their three-dimensional extent, are considered. Filled bodies can be modeled as beam elements and tubular bodies as shell elements. UFLEX provides modeling capabilities for complex cross-section geometries, contact and friction stresses, nonlinear relationships between curvature and bending moment, cross-section geometry ovalization, and nonlinear material models. This software has been validated by other finite element software as well as experiments described by Sævik and Bruaseth [27], Dai [28], Sævik and Gjøsteen [29], and SINTEF [30]."*

**解析：**
**UFLEX**（UFlexible）是挪威SINTEF Ocean开发的专业电缆/脐带缆截面分析软件，与OrcaFlex的分工完全不同：

| | OrcaFlex | UFLEX |
|--|----------|-------|
| **分析尺度** | 全局（整根电缆在海洋中的运动） | 局部（电缆截面内各层的应力） |
| **输出** | 电缆整体张力、曲率、运动轨迹 | 铜丝、钢丝等各组件的应力分布 |
| **计算时间** | 时域动力，分钟~小时级 | 截面静力，秒~分钟级 |

**关键能力：**
- **接触和摩擦应力（Contact and friction stresses）**：能精确模拟铜丝与铜丝之间、铜丝与钢丝之间的接触压力和摩擦力——这正是非线性弯曲行为的根源。
- **截面卵形化（Ovalization）**：电缆受压弯曲时，圆形截面会略微变成椭圆形，UFLEX能模拟这种几何非线性。
- **非线性材料模型**：铜在大变形时会发生塑性变形，UFLEX能处理弹塑性本构关系。

**验证说明**：作者特意列出了4篇UFLEX验证文献，说明这是经过实验和其他软件交叉验证的可靠工具，确保UFLEX结果可以作为简化方法的对比基准。

---

### 【2.2.1节·第1段：OC3-Hywind风机系统】

> *"The reference wind turbine in the present study is the 5MW OC3-Hywind FOWT based on Jonkman et al. [31] and Jonkman [32]. This FOWT uses a spar concept, and the stability of the platform is achieved through the large draft of the cylindrical buoy. Figure 1 shows the geometry of the FOWT, and Table 1 lists its general parameters. The setup of the FOWT in the dynamic analysis software is based on Schnepf et al. [21]."*

**解析：**
**为什么用OC3-Hywind这个模型？**

OC3-Hywind是由美国国家可再生能源实验室（NREL）定义的**标准参考风机模型**，全称是"Offshore Code Comparison Collaboration 3 - Hywind"。全球研究者广泛使用这个模型，原因是：
- **参数完全公开**：所有尺寸、质量、刚度数据均可在NREL报告中免费获取
- **可重复性高**：任何研究者使用同一模型，方便结果对比
- **代表性强**：基于Equinor公司真实的Hywind风机设计

**Spar型平台工作原理**：
Spar是一个细长的圆柱形浮筒，像一根漂浮的棍子。它的稳定性来自两个机制：
1. **深吃水（大吃水）**：平台吃水120m，使结构重心远低于水面，对波浪的运动响应小
2. **底部压载**：在圆柱底部填充重物（如铁矿石），将重心压得非常低，远低于浮力中心，形成"自扶正"力矩

关键参数梳理：
- 叶轮直径126m，高度相当于42层楼
- 轮毂高度90m（海面以上）
- 水深320m，平台总长（吃水）120m，即平台底端在海面以下120m处
- 3条系泊线，120°均布，固定平台位置但允许小幅运动

---

### 【2.2.2节·第1段：电缆基本属性与截面结构】

> *"This study uses a 66 kV dynamic power cable designed by Nexans [33]. Table 2 describes the general properties of the power cable, and Figure 2 shows its cross-section. The cable contains three copper conductors consisting of 19 copper wires, accumulating to a total copper cross-sectional area of 285 mm². Two layers of armored steel wires with a diameter of 4.2 mm are used to protect and stabilize the cable. The helically laid armor wires have a lay angle of 10° and −10°, respectively. A lay angle of 10° is used for the entire copper conductor, while the second and third copper wire layers have lay angles of 2° and 4°, respectively. The remaining insulation and binding components are made of polymer materials, such as cross-linked polyethylene (XLPE)."*

**解析：**
这段描述了电缆的**截面构造**，是理解疲劳机理的物质基础。

**为什么选66kV？**
66kV是海上风电场内部阵列间电缆的新兴标准电压等级（传统是33kV）。更高电压意味着：同样的功率传输，电流更小，损耗更少，电缆截面可以更细。欧洲海上风电正在向66kV迁移，因此研究66kV电缆非常有工程价值。

**截面结构逐层解析：**

```
① 铜导体（Copper Conductor）
   - 3相，每相1根导体
   - 每根导体由19根铜丝绞合而成（一根中心丝 + 6根第二层 + 12根第三层）
   - 绞合角：中心层10°，第二层2°，第三层4°
   - 总铜截面积：285mm²（约合直径19mm）
   - 绞合的目的：提高柔韧性，单根直铜棒会脆断，绞合后能弯曲

② 绝缘层（XLPE Insulation）
   - XLPE：交联聚乙烯，高压电缆标准绝缘材料
   - 隔绝三相铜导体之间及铜与外部的高压电场
   - 厚度决定了绝缘耐压等级

③ 填充层（Polyethylene Filler）
   - 聚乙烯材料填充三相导体之间的空隙
   - 作用：保持整体截面的圆形，防止压缩变形

④ 内护套（Inner Sheath）
   - 将三相导体束包裹在一起

⑤ 铠装钢丝层（Armor Wires）—— 两层
   - 每层由多根直径4.2mm的钢丝绞合缠绕
   - 第一层绞合角+10°，第二层绞合角−10°（反向绞合）
   - 反向绞合的重要意义：如果两层同向，拉伸时整根电缆会像弹簧一样发生扭转；反向绞合使两层的扭转效应相互抵消，保持轴向稳定
   - 作用：承受轴向张力、提供径向保护、防止挤压损伤

⑥ 外护套（Outer Sheath）
   - 聚合物材料，最外层防护
   - 防海水腐蚀、防机械磨损
```

**S-N曲线的选择**：

> *"Figure 3 shows the copper wires' stress–cycle curve (S–N curve) in the dynamic umbilical. The curve is similar to the one obtained by Nasution et al. [17]. The S–N curve for the armor steel wires is shown in Figure 3. It is similar to the S–N curves for steel with cathodic protection provided by DNV [34]. This study uses S–N curves and not strain-cycle curves as proposed by Karlsen et al. [15], based on the procedures of the majority of similar studies..."*

**解析：**
作者选择S-N曲线而非ε-N曲线的理由很务实：**工程界的主流做法，且制造商只提供S-N数据**。虽然Karlsen建议用ε-N曲线，但大多数类似研究（Marta、Ballard、Nasution等）都用S-N曲线，保持了与前人工作的可比性。

从图3可以看出：
- **铜丝的S-N曲线（蓝色虚线）**：相同循环次数下，铜的许用应力范围比钢小得多——铜更容易疲劳
- **钢丝的S-N曲线（红色实线）**：相同循环次数下，钢可以承受更大的应力幅值

这就是为什么最终疲劳寿命分析中铜导线先于铠装钢丝失效。

---

### 【2.2.2节·第2段：海洋生物附着效应】

> *"The power cable's diameter and weight increase during its lifetime because marine growth is dependent on the water depth. The calculation of the marine growth effects in this study is based on the information given by NORSOK [35] and DNV [36]. The start-of-life (SOL) state and the end-of-life (EOL) state power cable properties are specified in Table 4."*

**解析：**
**海洋生物附着（Marine Growth）** 是海洋工程中必须考虑的长期效应。

**附着规律（来自NORSOK N-003标准）：**
- 水深 0～50m：附着最厚，厚度可达30mm
- 水深 50～100m：附着次之
- 水深 > 100m：几乎没有生物附着（光照不足，温度低）

**对电缆的影响：**
- 外径增大（从0.116m增加到最大0.176m）→ 迎流面积增大 → 水动力阻力增大 → 动力响应增强
- 单位质量增大（从25kg/m增加到最大40.1kg/m）→ 重力增大 → 改变悬挂形状和张力分布

**SOL vs EOL：**
- **SOL（Start-of-Life，初始状态）**：刚安装时，无附着，电缆最轻最细
- **EOL（End-of-Life，寿命末期）**：附着最厚时，电缆最重最粗

本文通过对两种状态分别进行疲劳分析，量化了海洋生物附着对疲劳寿命的影响。

---

### 【2.2.3节·第1段：悬浮电缆配置详细说明】

> *"The inter-array power cable is suspended between the two FOWTs without touching the seabed or sea surface. Figure 4 shows an example of a suspended power cable setup. The distance between the wind turbines is 1134 m, equivalent to 9 times the rotor diameter of the FOWTs. The power cable is 1260 m long and divided into sections of different discretization sizes. A section of 10 m from the hang-off location has a segment length of 0.1 m, and the free-hanging cable sections have a segment length of 1.0 m. Attached to the power cable are three buoys with a distance of 300 m between them. The properties of the buoys are described in Table 5. The buoys have an anti-marine growth coating. Bend stiffeners to prevent excessive cable bending are attached to both ends of each buoy. The cable is discretized with a segment length of 0.31 m at the subsea buoys and 0.12 m at the bend stiffeners. The power cable hang-off consists of an I-tube, as shown in Figure 5. The center of its bell mouth is 70 m below the still-sea water level (SWL) at an 8 m radius from the spar center axis. It has a length of 7 m and is placed at an angle of 25° from the spar. The bell mouth opening has a diameter of 2.3 m and a minimum radius of 1.9 m. The mooring systems of the two FOWTs are mirrored, as shown in Figure 6. The nacelles of the wind turbines are always rotated towards the incoming wind direction."*

**解析：**
这段包含了大量配置参数，逐一解析：

**风机间距：1134m = 9×叶轮直径（126m）**
海上风电场的风机间距通常是叶轮直径的7～10倍，9倍是典型的工程取值，在减少风机间尾流干扰和控制成本之间取得平衡。

**电缆长度：1260m > 风机间距1134m**
电缆比两风机直线距离长约126m（多了约10%），这是必要的"松弛量"。如果两台风机运动时距离增大，松弛量可以防止电缆被绷断。

**网格划分策略（有限元离散化）：**
| 位置 | 单元长度 | 原因 |
|------|---------|------|
| 挂出点附近10m范围 | 0.1m（最密） | 应力梯度最大，需要精细计算 |
| 浮筒处 | 0.31m | 局部约束变化，中等精度 |
| 弯曲刚化器处 | 0.12m | 几何突变，需要较细划分 |
| 自由悬挂段 | 1.0m（最粗） | 应力变化平缓，粗单元足够 |

**三个浮筒，间距300m：**
浮筒均匀布置在电缆上，将1260m电缆分为大致均匀的四段。参考Ahmad等（2023）的优化结论，均匀分布是降低顶端张力的最优方案。

**弯曲刚化器（Bend Stiffeners）：**
在每个浮筒两端安装，是一种渐变截面的聚合物锥形保护件，其作用是**阻止电缆在浮筒端部产生过于急剧的弯折**（类似于充电线末端的橡胶保护套）。浮筒处是局部约束突变点，没有弯曲刚化器的话电缆可能在这里急剧弯折失效。

**I-tube（I型管）出线系统：**
电缆从Spar平台侧面的I型导管引出，I型管的出口端有一个**Bell mouth（喇叭口/弯曲导向器）**，直径2.3m，最小半径1.9m（大于电缆最小弯曲半径1.8m），防止电缆在出口处过度弯折。I型管安装在水面以下70m处，一方面避开了近海面的大波浪运动区域，另一方面朝25°斜向引导电缆，与电缆自然悬挂方向一致。

**系泊系统镜像对称：**
两台风机的系泊线布置完全对称（Figure 6中展示了6个方向的载荷方向及概率），这确保了两台风机的动力特性相同，仿真设置合理。

**风机迎风旋转：**
机舱（Nacelle）始终面向来风方向——这是现代风机的偏航控制（Yaw Control）功能。这意味着不同载荷方向下，两台风机的相对位置会改变，电缆所受载荷也随之变化。

---

### 【2.3节·第1、2段：环境条件】

> *"The wave, wind, and current conditions are based on a location in the North Sea on a latitude of 61° N with a water depth of 320 m... Table 6 presents all environmental parameters for the 30 load cases used in the present study, along with their occurrence probabilities. Load case 30 represents extreme weather when the wind turbine is idling. The FOWT is in operation in all other load cases. The Torsethaugen spectrum is applied to model irregular waves, and the NPD spectrum is used to simulate the wind. The current velocity at a specific height z is estimated through the following formula given by DNV..."*

**解析：**
**研究位置**：北纬61°、水深320m，这个位置与Hywind Tampen（挪威浮式风电场，2022年投运）非常接近，具有实际工程参考价值。

**30个工况的组织方式：**
这30个工况是对北海**全年海况统计分布**的离散化表示。每个工况代表一类海况（由波高Hs、周期Tp、流速、风速四个参数定义），并给出该类海况一年内出现的**概率**。疲劳计算时，各工况的损伤按概率加权叠加，得到年均损伤率，进而推算疲劳寿命。

| 典型工况举例 | Hs (m) | Tp (s) | 风速 (m/s) | 概率 |
|------------|--------|--------|-----------|------|
| 工况1（最常见） | 1.2 | 8.3 | 3.7 | 21.0% |
| 工况10 | 4.5 | 13.4 | 11.4 | 3.84% |
| 工况30（极端暴风） | 11.9 | 13.8 | 30 | 0.13% |

**注意工况30的特殊性：**
工况30是极端暴风（Hs=11.9m，几乎是10年一遇大浪），此时风速超过25m/s（切出风速），风机停止发电、空转（Idling）。虽然出现概率极低（0.13%），但其产生的载荷可能远大于其他工况，对疲劳损伤仍有贡献。

**Torsethaugen波浪谱**：
普通工程中常用JONSWAP谱（单峰），但北海经常同时存在本地风浪和远处涌浪（Swell），谱形是**双峰**的。Torsethaugen谱是专门为北海这种混合海况设计的双峰谱，比JONSWAP更准确。

**NPD（挪威石油局）风谱**：
描述风速随时间的脉动特性，OrcaFlex用此模拟风的湍流分量对风机的动态激励。

**海流速度剖面（公式1）**：

$$v_c(z) = v_{c,SWL}(0) \cdot \left(\frac{d+z}{d}\right)^{1/7}$$

其中z是水深（负数向下），d是总水深（320m），$v_{c,SWL}$是海面处流速。

**解读**：这个1/7次方公式描述了海流速度随水深的变化——海面处流速最大，越深越慢。这是经验公式（来自DNV规范），物理上对应于海底摩擦层的速度剖面。

**6个载荷方向**（Figure 6）：
环境载荷（波浪+风+流对齐方向）从6个不同方向作用于系统，概率最大的是Direction 3（28.7%），大致沿连接两台风机的轴线方向。**风浪同向**是保守假设，实际中风向和浪向可能有角度偏差，同向时对电缆的激励最强。

---

### 【2.4节·开篇段：疲劳评估四步流程总述】

> *"The fatigue assessment in this study is carried out in four steps. First, the nonlinear bending behavior of the power cable is determined. Second, dynamic analyses of the entire setup are performed to obtain the axial tension and the bending curvatures of the power cable. Third, the stresses of the cable components are calculated through stress factors. This work proposes a simplified and effective method to estimate these stress factors for dynamic power cables. Fourth, fatigue damage is determined by applying the rainflow counting method and the Miner–Palmgren rule."*

**解析：**
作者在这里清晰地给出了疲劳计算的**四步流水线**：

```
步骤①  UFLEX
        ↓ 电缆非线性弯曲刚度（弯矩-曲率关系）
步骤②  OrcaFlex 全局动力分析
        ↓ 每个时间步：各节点的张力T(t)、曲率C(t)
步骤③  应力因子换算
        ↓ 铜丝/钢丝的应力时历σ(t)
步骤④  雨流计数 + Miner-Palmgren
        → 累积损伤D → 疲劳寿命（年）
```

**为什么步骤①要先做？**
因为步骤②的OrcaFlex需要知道电缆的弯曲刚度（弯矩-曲率关系），才能正确模拟电缆的动力响应。如果把电缆的弯曲刚度设为线性（常数），会导致平台运动对电缆曲率的影响被误估，进而使步骤④的疲劳结果失真。

---

### 【2.4.1节·第1段：非线性弯曲行为估算】

> *"Dynamic power cables show nonlinear bending behavior due to friction, contact, and slip effects between the wires in the same layer and between wires of different layers [11]. The nonlinear bending behavior of the power cable is determined through finite-element analysis in UFLEX. A stepwise curvature is applied to the cable, and each step's corresponding bending moment is calculated. The obtained relationship between the bending curvature and the bending moment is applied to the power cable in the dynamic analyses."*

**解析：**
**非线性弯曲的物理机理（深度解释）：**

想象电缆截面是一束铅笔捆在一起。当你弯曲这束铅笔时：
- **小弯曲（初始阶段）**：各根铅笔紧密接触，相互摩擦约束，整束就像一根粗铅笔一样硬——**弯曲刚度大**
- **大弯曲（后期阶段）**：各根铅笔之间发生了相对滑动，摩擦被克服了，整束变得更柔软——**弯曲刚度减小**

这就是非线性的直觉理解。对于真实的动力电缆，这个机制更复杂，因为有多层、多材料、不同绞合角度，各层之间的摩擦系数也不同。

**UFLEX如何计算非线性弯曲刚度：**
在UFLEX中建立精细的电缆截面有限元模型，然后逐步施加曲率（从0增加到0.1 m⁻¹），每一步计算此刻截面内的所有接触力、摩擦力，并求出截面承受的总弯矩。最终得到一条"弯矩-曲率"关系曲线。这条曲线再以表格形式输入OrcaFlex，代替线性弯曲刚度。

---

### 【2.4.2节·第1~7段：应力因子计算（本文核心公式推导）】

> *"The stresses to determine damage are obtained by the following formula: S = KtT + Kc(Cx sinθ − Cy cosθ)"*

**解析（公式2）：**

| 符号 | 全称 | 物理意义 |
|------|------|---------|
| S | Stress | 某组件某位置的应力（MPa） |
| Kt | Tension stress factor | 张力应力因子（kPa/kN）：每kN张力产生多少kPa应力 |
| T | Effective Tension | 有效轴向张力（kN）——来自OrcaFlex的输出 |
| Kc | Curvature stress factor | 曲率应力因子（kPa/(1/m)）：每单位曲率产生多少kPa应力 |
| Cx, Cy | Curvature components | x、y方向的曲率分量（1/m）——来自OrcaFlex的输出 |
| θ | Circumferential angle | 截面上计算点的角度（°），一圈检查多个θ值取最大 |

**通俗理解**：就像把税前工资（张力T）乘以税率（Kt）得到应缴税款（应力），再加上额外扣款（弯曲贡献）。

---

> *"In the following part, this study proposes a simplified method for estimating the stress factors in a dynamic power cable in the early design stages when results from validated software or experiments are unavailable. If the power cable has a relatively low axial tension but a high bending utilization during its operation, the tension stress factors can be derived using the equations for the simple area stress of composite beams. When axially loaded, the strain is continuous across the cross-section of a composite beam, but the stress is discontinuous [42]."*

**解析：**
这是简化方法的**适用条件说明**：

**"低轴向张力、高弯曲利用率"**
本文的悬浮电缆配置中，电缆张力通常在50kN左右（相比屈服张力885kN，只有5.6%的利用率），而弯曲在fatigue分析中占主导。因此，张力贡献小，用简单的复合梁理论估算张力应力因子就足够精确。

**复合梁（Composite Beam）理论：**
当一个截面由两种不同材料（如铜和钢）组成，在轴向载荷下：
- **应变连续**：整个截面的轴向应变ε是均匀的（各层一起伸长，协调变形）
- **应力不连续**：但由于铜（E=95GPa）和钢（E=200GPa）弹性模量不同，相同的应变在钢里产生的应力（σ=Eε）比铜里大得多

这就是为什么铠装钢丝的张力应力因子（489 kPa/kN）比铜导线（232.3 kPa/kN）大得多——弹性模量之比约为200/95≈2.1，应力比也大致如此。

---

> *"From Hook's law: ε = σ₁/E₁ = σ₂/E₂ ... T = σ₁A₁ + σ₂A₂ ... combining gives Kt1 and Kt2"*

**解析（公式3~6的推导逻辑）：**

**第一步（公式3）**：胡克定律（应变=应力/弹性模量），因为应变连续，所以 σ/E 对两种材料相等。

**第二步（公式4）**：力平衡——整体拉力T必须等于两种材料各自承受的力之和（应力×面积）。

**第三步（公式5）**：联立上面两个方程，解出各材料的应力σ与T的关系。

**第四步（公式6）**：Kt定义为单位张力对应的应力，即 Kt = σ/T。

**结果**：铜导线Kt₁ = 232.3 kPa/kN，铠装钢丝Kt₂ = 489.0 kPa/kN（均与UFLEX结果完全一致！）。

---

> *"An assumption is made to derive the equation for the curvature stress factor for copper and armor wires. A total of 100% utilization of the cable capacity with zero tension is assumed to be equal to reaching the limit of any of the materials in the cable due to curvature. From the capacity curve, the maximum curvature of the cable can be determined. The following formulas are established for estimating a conservative curvature stress factor: Kc1 = Y1/Cmax, Kc2 = Y2/Cmax"*

**解析（公式7）：**

**假设的含义：**
当电缆弯曲到制造商规定的最小弯曲半径（1.8m，对应最大曲率Cmax=1/1.8≈0.556 m⁻¹）时，某种材料恰好达到屈服强度Y。

**Kc的推导：**
如果曲率达到Cmax时应力达到屈服强度Y，那么每单位曲率对应的应力就是：
$$K_c = Y / C_{max}$$

**为什么这个方法保守？**
Cmax是制造商的安全限制，其中已经包含了安全系数（可能是2倍或以上）。所以真实材料屈服时的曲率比Cmax大得多，这意味着真实的Kc比公式给出的值小很多——公式高估了Kc，使计算出的应力偏高，疲劳寿命偏低，设计更安全。

---

### 【2.4.3节：动力分析与疲劳损伤】

> *"Dynamic analyses are performed for all load cases in each loading direction in OrcaFlex. All load-case simulations have a duration of one hour and a time step of 0.1 s. Each simulation uses a different random seed to enable independent wave and wind conditions. All load cases are considered for the fatigue analysis with their occurrence probabilities. Furthermore, all cases of one loading direction are scaled to the appearance probability of each loading direction. The simulations determine the axial tensions and the curvatures for each node along the power cable. Marine growth is considered by running two different fatigue analyses with the power cable in the SOL and EOL states."*

**解析：**
**仿真规模估算：**
- 30个工况 × 6个方向 = 180次OrcaFlex仿真
- 每次1小时，时步0.1s → 每次36,000个时间步
- SOL和EOL各一套 → 总计360次仿真

**随机种子（Random Seed）：**
波浪和风是随机过程，每次仿真用不同的随机种子，意味着虽然统计特性（Hs、Tp等）相同，但具体的波形不同，这模拟了真实海况的随机性。

**概率加权方式：**
最终年疲劳损伤 = Σ（各工况损伤 × 该工况出现概率 × 所在方向出现概率）

---

> *"The fatigue analysis is performed using the rainflow counting method [43]. This method uses the stress time history resulting from the dynamic analyses to calculate the fatigue damage. The stress reversal points are grouped into different stress ranges. In the rainflow counting method, four reversal points are considered to detect stress cycles. If the outer points bind the inner points, a cycle is counted, and the difference between the stress ranges of the inner points is assigned as the amplitude of this cycle. This method assumes that the fatigue damage resulting from a closed cycle in the irregular amplitude loading equals the fatigue damage caused by one cycle in a constant amplitude test. The damage caused by half-cycles is neglected in this procedure because there are few of them in every realistic case."*

**解析：**
**雨流计数法（Rainflow Counting）深度解析：**

想象把应力时历图纸**旋转90°**变成一座"山峰和山谷"的地形图，让"雨水"从各个高点顺着斜面往下流：

1. 每一段"雨水流淌的路径"对应一次疲劳循环
2. 路径的起止高差就是这次循环的应力幅值
3. 统计所有路径的幅值分布，得到不同Δσ下的循环次数n

**"四个反转点"规则：**
算法取应力序列中的局部极值点（峰值和谷值），每次考察4个连续极值点。若中间两点的范围被外侧两点完全包含，则计一个循环，循环幅值为内侧两点的差值。

**关键假设（Miner假设）：**
不规则幅值载荷下一个闭合循环的损伤 = 恒定幅值试验中同幅值一个循环的损伤。这是一个线性假设，实际上材料的损伤是有顺序效应的（先大后小 vs 先小后大的结果不同），但工程中普遍认可这种简化。

---

> *"The cumulative damage is calculated according to the Miner–Palmgren rule [44]:"*

$$D = \sum_{i=1}^{k} \frac{n_i}{N_i}$$

**解析（公式8）：**

| 符号 | 含义 | 举例 |
|------|------|------|
| D | 累积损伤度 | D=1时认为发生疲劳破坏 |
| i | 第i个应力幅值级别 | 如Δσ=50MPa这一级 |
| ni | 该幅值下实际发生的循环次数 | 一年内出现了1000次 |
| Ni | 该幅值下材料失效所需循环次数 | 从S-N曲线查：50MPa对应100,000次 |
| ni/Ni | 该幅值造成的损伤分数 | 1000/100000 = 0.01（消耗了1%寿命） |

**疲劳寿命估算：**
若每年的总损伤量为D_year，则疲劳寿命 = 1 / D_year 年。

---

## 第3章 结果与讨论（Results and Discussion）

---

### 【3.1节·第1段：非线性弯曲结果解读】

> *"Figure 7 shows the bending behavior for the selected power cable for curvatures from 0 to 0.1 m⁻¹ and different axial tension levels. The bending moment increases faster per unit curvature for small curvatures from 0 up to 0.015 m⁻¹ than for curvatures larger than this value for all applied tensions. The bending moment continues to increase linearly for curvatures higher than the ones stated in the figure until at least 0.2 m⁻¹. Based on the results from Hu et al. [11], it increases similarly until the minimum bending radius of the cable is reached. The bending moment increases with higher axial tensions. As the baseline in this study, the curve for 50 kN axial tension is selected for the cable behavior since the cable usually has tensions around this value."*

**解析：**
图7（曲率-弯矩图）是本章第一个关键结果，包含多层信息：

**曲率0~0.015 m⁻¹（初始段，陡峭上升）：**
电缆内部各层导线还没有发生相对滑动，所有摩擦约束都完整起作用，弯曲需要克服所有层间摩擦力——就像一束绑紧的木棍，整体很硬。这一段弯矩增长非常快（斜率大）。

**曲率 > 0.015 m⁻¹（大曲率段，接近线性增长但斜率更小）：**
层间滑动已经发生，各层导线可以相对独立地弯曲，整体弯曲刚度下降。此时弯矩仍在增加，但速率变慢。

**轴向张力越大，曲线越高：**
这是因为轴向张力会对各层导线产生正压力，增大摩擦力，使层间滑动更难发生，整体弯曲刚度增大。相当于绑绳越紧，一束木棍越难弯折。

**基准选50kN张力：**
实际运行中，悬浮电缆的张力分布在整根电缆上。经初步计算，大部分位置张力在50kN左右，因此选这条曲线最具代表性。

---

### 【3.1节·第2段：不同弯折方向的差异】

> *"Figure 8 shows the bending moment on different axes of the power cable. The bending moments are slightly higher for curvatures around the z-axis than for curvatures around the y-axis. These results align with the nonlinear bending behavior described by Hu et al. [11]. In their study, the layout of the cable cross-section with the three helically wounded copper wire layers is stated as the reason for this nonlinearity."*

**解析：**
图8比较了电缆绕不同轴弯曲时的弯矩-曲率关系：

- 绕z轴（垂直方向）弯曲 > 绕y轴（水平方向）弯曲
- 差异不大，但确实存在

**原因（Hu等2022年解释）：**
三相铜导体在截面内是非对称分布的（三个导体呈三角形排列），且铜丝本身以一定螺旋角缠绕。这种三重螺旋对称性（而非完全旋转对称）使得从不同方向弯折时，遇到的层间摩擦路径略有不同，产生微小的各向异性。

**工程意义：**
电缆在海中受三维弯曲，弯曲方向不固定。绕z轴略硬于绕y轴，意味着在z方向弯曲时产生的应力略高。本文选用绕y轴的曲线作为基准（已说明在保守侧）。

---

### 【3.2节·第1段：简化方法 vs UFLEX 对轴向载荷的结果】

> *"Based on the formulas proposed by the present study, the stress factors described in Table 7 are obtained. The stress factors obtained with the finite element simulations are listed in Table 8. Figure 9 shows the results from the finite element simulations for 50 kN axial loading and 0.1 m⁻¹ curvature loading. The stresses are higher for armored steel wires than copper wires. This is because steel has a higher Young's modulus and higher yield strength than copper. Figures 10 and 11 compare the stresses resulting from the calculations with the stress factors and the finite element simulations for different axial loadings. The stresses obtained from the different calculation methods are similar for the copper and steel armor wires."*

**解析：**
**图9（UFLEX有限元截面应力云图）解读：**
在50kN轴向拉力 + 0.1 m⁻¹曲率同时作用下，截面内各组件的Von Mises应力分布如彩色云图所示。颜色越红表示应力越高。从图中可以看到：铠装钢丝（外层环形）的应力（约50~60MPa）远高于铜导线（内层，约20~30MPa）——这与弹性模量之比（钢/铜 ≈ 200/95 ≈ 2.1倍）一致。

**图10、11（轴向载荷对比）关键发现：**
对于轴向载荷（T从0到100kN），简化应力因子方法与UFLEX的结果**几乎重合**（误差很小）。这验证了复合梁理论假设在轴向载荷下是成立的。

---

### 【3.2节·第2段：简化方法 vs UFLEX 对弯曲载荷的结果】

> *"Figures 12 and 13 show the stresses obtained by the two methods for different curvatures. A low axial load of 5 kN is applied in the finite element simulations to achieve faster convergence. The proposed stress factor method also assumes the same axial tension to enable a better comparison. The results show that the stresses obtained from the proposed stress factor calculation method are up to 218% higher for the copper and armor steel wires than those obtained from the finite element simulations. Considering that the calculation for the curvature stress factors is based on the maximum allowable curvature of the cable the manufacturer provides, which most likely contains a significant safety factor, higher values than obtained by finite element simulations can be expected. Additional curves assuming utilization factors as given in API 17J [45] are included in the figures. It can be concluded that the curvature stress factors are very conservative when calculated by the method proposed in the present study."*

**解析：**
**图12、13（弯曲载荷对比）关键发现：**
当施加曲率载荷时，简化方法给出的应力比UFLEX高出最多**218%（约3倍）**——这是一个很大的偏差。

**为什么偏差这么大？**
原因是 Kc = Y/Cmax 这个公式假设"达到最大曲率时材料恰好屈服"。但实际上：
- 制造商给出的最小弯曲半径（MBR=1.8m）已经包含了安全系数（通常为1.5~2倍）
- 真正让铜/钢达到屈服的曲率，比1/MBR大得多
- 因此真实的Kc比公式值小很多，简化方法大幅高估了弯曲应力

**API 17J标准的利用率因子（Utilization Factor）：**
图中还画了使用API 17J（针对柔性管规范）建议的利用率因子（0.85和0.67）修正后的曲线。这些曲线介于简化方法和UFLEX之间，可以理解为"适当保守"的中间选项。

**结论：简化方法在弯曲载荷下非常保守（偏安全）**，适合设计初期的快速筛查，但不适合精确疲劳寿命计算。

---

### 【3.2节·第3段：摩擦效应敏感性分析】

> *"A sensitivity study on the friction effects of the cable components in the finite element software is carried out. Table 9 shows the results from the finite element simulations for a model including friction effects between the internal components and for a model neglecting these effects. The results of the two models are similar, with the setup including friction always resulting in slightly higher stress values. The differences between the two models are larger for the copper wires than for the armor steel wires. Additionally, the percentual deviation of the stresses obtained with the model neglecting friction effects compared to the ones obtained with the other model seems to decrease for higher curvatures."*

**解析：**
这是一个**验证性的补充分析**，目的是量化摩擦的影响。

**敏感性分析（Sensitivity Study）的意义：**
在数值模拟中，我们常常不确定某个参数（如层间摩擦系数）的精确值，因此通过改变这个参数来观察结果的变化量，以判断这个参数的重要性。

**发现：**
- 含摩擦模型的应力比无摩擦模型**略高**（约高1%~14%），说明摩擦确实增大了应力，但影响不是决定性的
- 铜导线的摩擦影响（最大13.7%）比铠装钢丝（最大2.5%）大：因为铜导线层数多（三层），层间接触面多，摩擦影响叠加更明显
- **高曲率时差异缩小**：大曲率下层间已经充分滑动，摩擦是否存在对最终应力影响变小

**工程含义：**
对于铠装钢丝，忽略摩擦的误差小于3%，可以接受；对于铜导线，在小曲率工况下误差可达14%，需要注意。

---

### 【3.3节·第1段：疲劳分析主要结果】

> *"Table 10 shows the fatigue analysis results performed in OrcaFlex using the stress factors obtained by the method proposed in the present study and from the finite element software. The lowest fatigue life is identified for both marine growth states at the same location, close to the hang-off point. Very long fatigue lifetimes are obtained, indicating small tension and curvature ranges in the power cable. The failing components are the copper wires due to their lower resistance against long-cycle fatigue. The calculated lifetime for the EOL state is a maximum of 10% lower than for the SOL state."*

**解析：**
**核心数字：最小疲劳寿命约7万年！**

这个数字乍看令人惊讶——设计寿命通常是25年，疲劳寿命却高达7万年，说明在这种配置下电缆实际上几乎不会因疲劳而失效。

**原因分析——为什么载荷这么小？**
悬浮电缆两端都连接浮式平台，与悬链线/懒波形（一端固定在海底）不同。当两台风机同向运动（都随波浪前后摆）时，电缆两端的相对位移很小，张力和曲率变化幅度都非常小，循环应力幅值低，自然疲劳寿命极长。

**铜导线为何先失效？**
比较S-N曲线：在低应力幅值（高周疲劳区）时，铜的许用循环次数比钢少——铜的S-N曲线"下垂"更快。虽然铜承受的应力（约20~30MPa）比钢（约50~60MPa）小，但铜的S-N曲线更快衰减，导致铜导线的疲劳损伤累积速度更快。

**EOL比SOL寿命低10%：**
海洋生物附着增加了电缆的重量和迎流面积，使载荷略有增加。10%的差距说明附着效应对整体疲劳的影响相对较小。

---

### 【3.3节·第2、3段：沿电缆长度的疲劳寿命分布】

> *"Figures 14 and 15 show the fatigue life over the cable length for the armor steel wires and the copper conductor in the SOL state, while Figures 16 and 17 show the EOL state results. The fatigue damage is significantly lower for the armor wires along the entire cable length than for the copper wires. The critical locations are identical for all analyzed cases, with the largest fatigue damage occurring close to the hang-off points and the buoys. Figure 18 shows the locations with the largest fatigue damage along the suspended power cable. Close to the ends of the power cable, the lifetime for the EOL state is lower than for the SOL state since the cable is in a depth zone with marine growth effects. However, no difference between the two states occurs in the middle parts of the power cable because the deeper location prevents marine growth. Moreover, the figures show the results of the fatigue analyses performed with the stress factors obtained from the proposed simplified method and UFLEX. As expected, the fatigue life obtained using the new method's factors is lower for all components and marine growth states, confirming that it is a conservative approach. The lowest fatigue life occurs at the location with the largest curvature range. Therefore, bending is the main contributor to fatigue damage to the power cable in this configuration."*

**解析：**
**图14~17（疲劳寿命沿电缆分布图）解读：**

这些图的横轴是**弧长（Arc Length）**，即从一端Hang-off点到另一端的距离（0~1260m）；纵轴是**疲劳寿命（年）**，用对数坐标（10²~10²⁶年）。

**典型分布形状：**
```
疲劳寿命（对数尺度）
10²⁶ |         ___________   ___________
10²³ |       /             \ /             \
10²⁰ |      /               X               \
10¹⁷ | ____/                                  \____
10¹⁴ |      ↑              ↑↑              ↑
      0      浮筒1        浮筒2,3         浮筒/挂出
          (局部低谷)   (局部低谷)       (最低点)
```

**危险位置分类：**

| 位置 | 疲劳寿命量级 | 原因 |
|------|------------|------|
| **Hang-off点附近（约5.85m处）** | 最低（~10⁵年量级） | 平台运动直接作用，曲率变化幅度最大 |
| **浮筒两侧** | 较低（~10¹¹年量级） | 浮筒对电缆形成局部约束，此处曲率有突变 |
| **电缆中段自由悬挂段** | 极高（~10²³年量级） | 两端约束都不直接影响，载荷小 |

**SOL vs EOL的差异分布：**
- 端部（0~约100m和1160~1260m）：EOL寿命更低（约10%），这里处于水深50~100m，有明显海洋生物附着
- 中段（约200~1000m）：SOL和EOL曲线**完全重合**，因为这里水深超过100m，无附着

**简化方法 vs UFLEX疲劳寿命：**
用简化方法应力因子计算的疲劳寿命曲线整体**低于**UFLEX结果（因为Kc被高估，应力被高估，损伤被高估，寿命被低估），两条曲线趋势完全一致，危险位置判断完全相同——这验证了简化方法作为保守估计工具的有效性。

**最终结论**：弯曲（曲率变化）是疲劳损伤的主要驱动力，这与摘要和引言中的预判完全吻合，形成闭环。

---

## 第4章 结论（Conclusions）

---

### 【结论·第1段（总述）】

> *"The fatigue life of a suspended inter-array power cable connecting two FOWTs is investigated considering environmental conditions in the North Sea. The fatigue calculation is based on stress factors estimated through a simplified method proposed in the present work for preliminary design. This method is based on composite beam stress theory and the minimum bending radius of the power cable. The applicability of this method is shown by validation with results from finite element simulations."*

**解析：**
这段是对整篇论文工作的一句话总结：**北海环境 + 悬浮电缆 + 应力因子简化方法 + 有限元验证**。提炼出简化方法的两个理论基础：复合梁理论（用于Kt）和最小弯曲半径（用于Kc）。

---

### 【结论·应力因子方法的发现（三条）】

> *- The proposed stress factor calculation method delivers good results for the selected cable when only tension is applied, based on the comparison with the results from the established finite-element software.*
> *- The proposed stress factor calculation method delivers conservative results when curvature is applied in addition to tension.*
> *- The proposed stress factor estimation method gives conservative results for the preliminary design of the power cable before more reasonable stress factors are known. The fatigue life should be calculated again after the stress factors are obtained through finite element software or experiments.*

**解析：**

**第1条**（张力载荷：方法可靠）：复合梁理论对轴向载荷有理论支撑，结果精确。这说明在张力主导的工况下，简化方法完全可用。

**第2条**（弯曲载荷：方法保守）：Kc = Y/Cmax 这个公式因为安全系数的层叠导致过于保守（高估3倍）。这在设计初期没问题，但不能用于精确寿命评估。

**第3条**（使用建议）：简化方法是**初步设计工具**，当后续获得有限元或实验数据后，必须用精确Kc重新计算。这条建议给出了明确的设计流程：初步→精确，两阶段验证。

---

### 【结论·悬浮电缆疲劳分析的发现（四条）】

> *- The suspended inter-array power cable in the presented configuration has a very long fatigue life resulting from low cyclic loadings.*
> *- The critical areas with respect to fatigue damage are located next to the hang-off points and the buoys. Bending is identified as the main contributor to fatigue damage.*
> *- The estimated fatigue life of the power cable is dependent on the cable and buoy properties. Therefore, the fatigue life should be calculated for each power cable configuration individually.*
> *- The effects of marine growth on the power cable fatigue life are small because large parts of the power cable are located in depths where no marine growth occurs.*

**解析：**

**第1条**（极长寿命）：>6万年远超工程寿命（25~30年），说明本文研究的悬浮配置在疲劳方面具有很大的设计裕量，有进一步优化（减少材料、改变浮筒尺寸等）的空间。

**第2条**（危险位置+弯曲主导）：挂出点和浮筒附近是设计重点。工程实践上，这意味着应重点保护这些位置（更好的弯曲刚化器、优化I-tube几何形状等）。弯曲主导意味着降低这些位置的曲率变化幅度是延长寿命最有效的手段。

**第3条**（配置依赖性）：不同的浮筒尺寸、数量、位置，不同的电缆规格，都会显著改变疲劳结果。**没有通用的疲劳寿命**，每个项目必须单独分析。这也提示读者不能把本文的7万年结论直接套用到其他配置。

**第4条**（海洋生物附着影响小）：因为电缆中段位于100m以下深水区（占总长的大部分），海洋生物附着几乎没有影响。近海面的挂出点附近虽然有附着，但那里本来就是最危险的位置，额外10%的寿命降低在已有的巨大寿命裕量下并不关键。

---

*精读完成 | 文档版本：v2（段落严格对应版）*
*整理时间：2026-06-04*
