# 🛒 电商用户消费行为分析

基于 Python 数据分析栈，对电商平台用户历史交易数据进行清洗、特征工程与 RFM 用户分层分析，旨在挖掘高价值用户群体并输出运营策略建议。

## 1.📂 项目结构

```markdown
ecommerce-user-consumption-analysis/
├── data/               # 原始数据与清洗后数据（已加入 .gitignore）
├── notebooks/          # 探索性分析 (EDA) 与可视化验证
├── src/                # 核心业务逻辑模块
│   ├── data_loader.py      # 数据加载与解析
│   ├── preprocessor.py     # 数据清洗与异常值处理
│   ├── analyzer.py         # RFM 模型与特征工程
│   └── visualizer.py       # 报表生成与图表输出
├── main.py             # 项目统一入口
├── requirements.txt    # 环境依赖清单
└── README.md           # 项目说明文档
```

## 2.🚀 快速开始

### 2.1.环境准备

确保你的电脑已安装 Python 3，并安装项目所需的依赖包：

```
pip install -r requirements.txt
```

### 2.2.运行项目

```
python main.py
```

## 3.📊 分析结论

本项目通过对电商用户消费行为的深度挖掘，得出以下核心结论：

### 3.1.数据集特征分析

- 日期格式需要进行转换
- 存在一个用户当天购买多笔订单的情况

---

### 3.2.数据集describe分析

- 用户购买数量均值 2.4 且标准差 2.3，有较小偏移但正常（波动较小）
- 50%分位在 2 但75分位数在 3，说明绝大多数订单购买量是不多的，最大数量为99，说明有大客户
- 用户购买金额中通过分位数可以看出大部分订单集中在 30 - 40 之间

![八大特征描述图](G:\C-CodeBases\ecommerce-user-lifecycle-analysis\images\describe_image.png)

## 4.🛠️ 技术细节