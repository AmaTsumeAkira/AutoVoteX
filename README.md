# 投票系统自动化工具

## 项目简介

本项目包含两个Python脚本，用于投票系统的自动化操作和票数统计展示，支持多种投票模式配置。

## 功能说明

### 核心脚本
- `toupiao.py` - 自动化投票脚本
  - 支持多种投票模式：固定投票、随机投票、混合投票、权重投票
  - 模拟真实用户行为（随机请求头、间隔时间）
  - 多账号批量操作
  - 实时成功率统计

- `piaoshu.py` - 票数统计看板
  - 实时可视化投票数据
  - 候选人高亮显示
  - 自动排序+分页显示
  - 票数总和统计

## 使用说明

### 环境配置
```bash
pip install -r requirements.txt
```
requirements.txt 内容：
```
requests>=2.28
beautifulsoup4>=4.11
fake-useragent>=1.1
rich>=13.3
```

### 配置文件
1. `user.csv` 格式：
```csv
学号1,密码1
学号2,密码2
```

2. 候选人ID对照表（运行piaoshu.py可查看）

### 投票模式配置
修改 `toupiao.py` 中以下代码段：
```python
# ===== 投票模式选择 =====
# 模式1：完全固定投票（示例）
final_elements = ["28", "24", "16"]  

# 模式2：固定+随机混合（推荐）
fixed_elements = ["28", "24", "16"]  
random_elements = random.sample(其他候选人列表, 7)
final_elements = fixed_elements + random_elements

# 模式3：完全随机投票
final_elements = [str(random.randint(1, 34)) for _ in range(10)]

# 模式4：权重投票（需配置weights数组）
```

### 运行参数
```bash
# 查看实时票数
python piaoshu.py

# 启动投票程序（建议后台运行）
nohup python toupiao.py > vote.log 2>&1 &
```

## 高级功能
1. 请求间隔配置：
```python
time.sleep(random.uniform(1, 5))  # 修改toupiao.py中的延迟时间
```

2. 异常重试机制：
```python
# 默认已包含失败统计和重试逻辑
```

## 注意事项
1. 请合理设置投票间隔（建议≥3秒）
2. 单个账号每日投票次数有限制
3. 高频请求可能导致临时封禁
4. 请遵守所在网络的使用政策

## 免责声明
本工具仅用于Python自动化技术学习，使用者应自行承担相关责任。开发者不建议将其用于任何可能违反规定的场景。
