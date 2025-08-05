# ChatPersona - AI人格社交实验平台

## 项目简介

ChatPersona 是一个基于大模型的多角色对话应用，专为Z世代年轻人设计的AI人格社交实验平台。用户可以创建具有独特性格的AI角色，并与多个角色进行群聊互动。

## 功能特色

### 🧠 人格创建器（Persona Maker）
- **标签式配置**：通过选择性格关键词、语言风格、角色类型自动生成角色提示词
- **自定义Prompt**：手动填写完整的系统提示词，享受更高的自由度
- **实时预览**：支持角色效果预览功能

### 👥 多角色群聊（Multi-Agent Role Chat）
- **多角色互动**：可邀请多个AI角色组成聊天室
- **实时对话**：支持轮流发言，模拟真实群聊体验
- **动画效果**：头像跳动、"正在输入..."动画等丰富的视觉反馈

### 🔐 API Key 管理
- **灵活配置**：支持用户自填阿里云百炼API Key
- **默认支持**：提供默认API Key供体验使用
- **安全存储**：API Key安全存储在本地数据库

### ⚠️ 风险预警机制
- **话题锚定**：监控对话是否偏离原始主题
- **人格一致性**：确保AI角色保持设定的性格特征

## 技术架构

- **后端**：Flask + SQLite
- **前端**：HTML + Tailwind CSS + JavaScript
- **AI服务**：阿里云百炼·千问大模型
- **数据库**：SQLite（轻量级，易部署）

## 安装指南

### 环境要求
- Python 3.8+
- pip 包管理器

### 安装步骤

1. **克隆项目**
```bash
cd d:\工作\WPS\AI\trae\Chatbot
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **配置API Key（可选）**
```bash
# 设置环境变量（推荐）
set QWEN_API_KEY=your_qwen_api_key_here

# 或者在应用中通过界面设置
```

4. **启动应用**
```bash
python app.py
```

5. **访问应用**
打开浏览器访问：http://localhost:5001

## 使用指南

### 1. 创建AI角色

#### 标签式创建
1. 点击"创建新角色"
2. 选择"标签式配置"
3. 从预设标签中选择性格、语言风格、角色类型
4. 系统自动生成角色提示词
5. 点击"创建角色"

#### 自定义Prompt创建
1. 选择"自定义Prompt"
2. 在文本框中输入详细的角色设定
3. 可点击"预览效果"查看角色表现
4. 确认后创建角色

### 2. 开始群聊
1. 在首页点击"开始聊天"
2. 点击"选择角色"选择参与聊天的AI角色
3. 输入话题或问题
4. 观看AI角色们的精彩互动

### 3. API Key设置
1. 点击导航栏的"API设置"
2. 输入你的阿里云百炼API Key
3. 保存设置

## 默认角色介绍

应用内置了三个示例角色：

| 角色 | 性格特点 | 简介 |
|------|----------|------|
| 吉伊 | 敏感、胆小、善良 | 努力想变强，时常哭但很可爱 |
| 小八 | 搞笑、机灵、温和 | 反应快，是气氛担当 |
| 乌萨奇 | 热血、冲动、自信 | 喜欢冒险和主导谈话 |

## API接口文档

### 角色管理
- `GET /api/characters` - 获取所有角色列表
- `POST /api/create-character` - 创建新角色
- `POST /api/generate-preview` - 生成角色预览

### 聊天功能
- `POST /api/chat` - 发送消息并获取AI回复
- `POST /api/set-api-key` - 设置API Key

### 风险控制
- `POST /api/topic-anchor-check` - 检查话题偏离度
- `POST /api/persona-score` - 评估人格一致性

## 项目结构

```
Chatbot/
├── app.py                 # Flask主应用
├── requirements.txt       # Python依赖
├── README.md             # 项目文档
├── chatpersona.db        # SQLite数据库（运行时生成）
└── templates/            # HTML模板
    ├── index.html        # 首页 - 角色列表
    ├── create.html       # 创建角色页面
    └── chat.html         # 群聊界面
```

## 开发说明

### 数据库结构

#### characters 表
- `id`: 角色ID（主键）
- `name`: 角色名称
- `personality`: 性格标签
- `description`: 角色描述
- `system_prompt`: 系统提示词
- `avatar_url`: 头像URL（预留）
- `created_at`: 创建时间

#### chat_history 表
- `id`: 消息ID（主键）
- `session_id`: 会话ID
- `character_id`: 角色ID
- `message`: 消息内容
- `sender`: 发送者
- `timestamp`: 时间戳

#### api_config 表
- `id`: 配置ID（主键）
- `user_session`: 用户会话
- `api_key`: API密钥
- `model_name`: 模型名称
- `created_at`: 创建时间

### 自定义配置

可以通过修改以下变量来自定义应用：

```python
# app.py 中的配置
app.secret_key = 'your_secret_key'  # 会话密钥
DEFAULT_API_KEY = 'your_default_api_key'  # 默认API Key
DEFAULT_MODEL = 'qwen-plus'  # 默认模型
```

## 注意事项

1. **API Key安全**：请妥善保管你的阿里云API Key，不要在代码中硬编码
2. **模型限制**：请注意阿里云百炼的API调用限制和费用
3. **数据备份**：重要的角色和聊天记录请及时备份
4. **网络环境**：确保网络能够访问阿里云API服务

## 故障排除

### 常见问题

**Q: API调用失败怎么办？**
A: 检查API Key是否正确，网络是否正常，API额度是否充足

**Q: 角色回复不符合预期？**
A: 尝试优化角色的系统提示词，使其更加详细和具体

**Q: 数据库错误？**
A: 删除 `chatpersona.db` 文件，重启应用会自动重新创建

**Q: 页面样式异常？**
A: 检查网络连接，确保能够加载Tailwind CSS CDN

## 更新日志

### v1.0.0 (2024-01-XX)
- 初始版本发布
- 支持角色创建和多角色群聊
- 集成阿里云百炼API
- 实现基础的风险控制机制

## 贡献指南

欢迎提交Issue和Pull Request来改进项目！

## 许可证

本项目采用 MIT 许可证。

## 联系方式

如有问题或建议，请通过以下方式联系：
- 项目地址：[GitHub Repository]
- 邮箱：[your-email@example.com]

---

**享受与AI角色们的精彩对话吧！** 🎭✨