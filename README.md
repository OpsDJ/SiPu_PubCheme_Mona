# 化学信息采集系统

一个自动化的化学化合物信息采集系统，用于从多个数据库（思普数据库、PubChem、MONA）抓取化合物详细信息、质谱数据，并自动整理保存。

## 项目简介

本项目实现了从多个化学数据库自动采集化合物信息的功能，包括：
- **思普数据库**：获取化合物的基本信息（CAS号、分子式、分子量、中英文名等）
- **PubChem数据库**：获取化合物的质谱数据（MS2谱图、碰撞能量、保留时间等）
- **MONA数据库**：获取化合物的QTOF质谱数据

所有采集的数据会自动保存为CSV和Excel格式，并支持将化合物图片插入到Excel文件中。

## 项目结构

```
化学信息采集/
├── main.py                 # 主程序入口
├── CreateFilePath.py       # 文件夹结构创建模块
├── transform.py            # 数据转换和Excel处理模块
├── not_find.png           # 未找到图片时的占位图
├── sipu/                  # 思普数据库模块
│   ├── GetDetailsInfo.py  # 获取化合物详细信息
│   ├── SaveData.py        # 保存思普数据
│   └── GetBasicInfo.py    # 基础信息获取
├── pucheme/               # PubChem数据库模块
│   ├── GetPubcheme.py     # PubChem数据获取主模块
│   ├── GetBasic.py        # 基础查询功能
│   ├── ParsePuchemeData.py # 数据解析
│   ├── SavePubChemeData.py # 数据保存
│   └── Donload.py         # SDF文件下载
├── mona/                  # MONA数据库模块
│   ├── GetMonaInfo.py     # MONA数据获取主模块
│   ├── ParseMona.py       # 数据解析
│   └── SaveMona.py        # 数据保存
├── tools/                 # 工具模块
└── CompoundLibrary/       # 数据存储目录
    └── [按分类组织的文件夹结构]
        ├── img/           # 化合物图片
        ├── id/            # 化合物ID列表
        └── doc/           # 文档数据
```

## 功能特性

### 1. 多数据源采集
- **思普数据库**：采集CAS号、分子式、分子量、中英文名、溶解性等基本信息
- **PubChem**：通过CAS号查询，获取质谱数据（MS2谱图、碰撞能量、保留时间、前体离子m/z值）
- **MONA**：通过化合物英文名搜索，获取QTOF质谱数据

### 2. 自动化流程
- 自动创建分类文件夹结构
- 自动读取化合物ID列表
- 按顺序采集每个化合物的多源数据
- 自动保存为CSV格式（支持追加写入）

### 3. 数据管理
- 按化合物分类组织文件夹结构
- 支持图片下载和存储
- 数据保存为CSV格式，便于后续处理
- 支持CSV转Excel（支持大数据量分Sheet）
- 支持将图片插入Excel文件

### 4. 错误处理
- 请求重试机制（最多3次）
- 详细的日志记录
- 异常捕获和错误标记
- 未找到数据时自动标记

## 安装依赖

### Python版本要求
- Python 3.7+

### 安装依赖包

```bash
pip install requests beautifulsoup4 pandas openpyxl tqdm
```

或者创建 `requirements.txt` 文件：

```txt
requests>=2.25.0
beautifulsoup4>=4.9.0
pandas>=1.3.0
openpyxl>=3.0.0
tqdm>=4.60.0
```

然后安装：

```bash
pip install -r requirements.txt
```

## 使用方法

### 1. 准备化合物ID列表

在每个分类文件夹的 `id/compound_ids.txt` 文件中，每行一个化合物ID（例如：`CN000083`）。

### 2. 配置分类ID

在 `main.py` 中的 `cat_id_list` 中配置需要采集的分类ID：

```python
cat_id_list = [54, 55, 56, ...]  # 修改为你需要的分类ID
```

### 3. 运行主程序

```bash
python main.py
```

程序将：
1. 自动创建文件夹结构
2. 遍历每个分类的化合物ID列表
3. 依次从思普、PubChem、MONA数据库采集数据
4. 保存数据到对应的CSV文件
5. 下载化合物图片到 `img/` 文件夹

### 4. 数据转换（可选）

如果需要将CSV转换为Excel并插入图片：

```python
python transform.py
```

或者使用 `transform.py` 中的函数：

```python
from transform import get_sheet_info_by_id, transform_excel, insert_images_to_excel

# 转换CSV为Excel
csv_file = get_sheet_info_by_id(root_dir, cat_id)
transform_excel(csv_file)

# 插入图片到Excel
img_dir = get_img_info_by_id(root_dir, cat_id)
insert_images_to_excel(excel_path, img_dir)
```

## 数据格式

### CSV文件格式

每个分类会生成一个CSV文件，包含以下列：
- `属性`：数据字段名（如：CAS号、分子式等）
- `值`：对应的数据值
- `图片路径`：化合物图片文件名

### 文件夹命名规则

文件夹命名格式：`{id}_{分类名称}`

例如：`54_单萜类`、`55_倍半萜类`

## 日志系统

程序运行时会自动生成日志文件，保存在 `logs/` 目录下，文件名格式：
```
log_YYYY-MM-DD_HH-MM-SS.log
```

日志包含：
- 程序启动/结束时间
- 每个化合物的采集状态
- 错误信息和异常堆栈
- 数据保存路径

## 注意事项

1. **网络连接**：确保能够访问以下网站：
   - 思普数据库：`https://www.push-herbchem.com`
   - PubChem：`https://pubchem.ncbi.nlm.nih.gov`
   - MONA：`https://mona.fiehnlab.ucdavis.edu`

2. **请求频率**：程序已内置重试机制和延迟，但请注意不要过于频繁请求，避免被封IP

3. **数据完整性**：
   - 如果某个数据库没有数据，会在CSV中标记"暂无数据"
   - 如果图片下载失败，会使用 `not_find.png` 作为占位图

4. **文件路径**：
   - 确保 `CompoundLibrary` 目录有写入权限
   - Windows系统路径中的特殊字符会被自动替换

5. **Excel文件大小**：
   - 如果数据量超过100万行，会自动分Sheet保存
   - 插入图片时注意Excel文件大小限制

## 分类ID说明

项目支持以下化合物分类（部分示例）：
- 54: 单萜类 (Monoterpenoids)
- 55: 倍半萜类 (Sesquiterpenoids)
- 56: 二萜类 (Diterpenoids)
- 57: 三萜类 (Triterpenoids)
- 62-68: 各类生物碱
- 27-38: 各类黄酮化合物
- ...（更多分类见 `CreateFilePath.py` 中的JSON数据）

## 开发说明

### 模块说明

- **sipu模块**：负责从思普数据库获取化合物详细信息
- **pucheme模块**：负责从PubChem获取质谱数据
- **mona模块**：负责从MONA数据库获取QTOF质谱数据
- **transform模块**：负责数据格式转换和Excel处理

### 扩展开发

如需添加新的数据源：
1. 创建新的模块文件夹
2. 实现数据获取和保存函数
3. 在 `main.py` 中调用新模块

## 常见问题

**Q: 程序运行中断怎么办？**  
A: 程序支持追加写入，可以重新运行，已采集的数据不会重复。

**Q: 如何只采集特定分类？**  
A: 修改 `main.py` 中的 `cat_id_list`，只包含需要的分类ID。

**Q: CSV文件如何转换为Excel？**  
A: 使用 `transform.py` 中的 `transform_excel()` 函数。
