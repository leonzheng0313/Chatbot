产品需求文档 PRD：ChatPersona

一、项目概述
项目名称：ChatPersona
项目类型：基于大模型的多角色对话应用 / AI人格社交实验平台
目标用户：Z世代年轻人（95后–10后），偏好虚拟互动、人格扮演与表达自我
使用场景：虚拟群聊、情绪倾诉、角色演绎、人格测试、社交陪伴

技术架构：
大模型服务：阿里云百炼API qwen-plus
前端：Tailwind CSS + HTML
后端：Flask + SQLite

二、功能设计与创新亮点
🧠 1. 人格创建器（Persona Maker）
两种方式创建角色人格：
1)标签式配置：选择性格关键词、语言风格、角色类型，自动生成 prompt
2)自定义 prompt：手动填写完整 system prompt，自由度高

支持 prompt 模拟预览功能

提示语默认内容：“你是一个有独特性格的 AI 角色，喜欢用「xx」的语气与人交流。”

🎭 默认内置角色（示例）
角色	个性	简介
吉伊	敏感、胆小、善良	努力想变强，时常哭但很可爱
小八	搞笑、机灵、温和	反应快，是气氛担当
乌萨奇	热血、冲动、自信	喜欢冒险和主导谈话

👥 2. 多角色群聊（Multi-Agent Role Chat）
用户可邀请多个已创建角色组成「人格聊天室」
支持输入话题、回复可控节奏（如一轮轮发言）

前端展示：
头像轻微跳动发言
“正在输入…”（...）动画
可选 emoji 漂浮（如激动回应）

💬 示例对话流程
用户输入话题：“我今天很焦虑怎么办？”

角色 A（温柔型）发言安慰

角色 B（理性型）分析建议

角色 C（毒舌型）讽刺一句，带出反差感

🔐 3. API Key 管理机制
支持用户自填阿里云 API Key，优先使用用户输入
默认使用占位 key（如 sk-XXXX），部署时管理员配置实际值
前端提示语：“你可以输入自己的百炼 Key，或使用默认通用 Key 体验功能。”

⚠️ 4. 风险预警机制（Prompt 失控防范）
话题锚定机制：
每轮对话传入原始主题进行话题重申
支持调用 /api/topic-anchor-check 监控语义偏离度

人格一致性控制：
每轮强制加入角色设定提示词（system prompt 重置）
可选加入 /api/persona-score 模块，判断输出内容是否符合角色风格

三、页面结构与前端样式设计（Tailwind 风格）
1. 首页 - 我的角色列表
html
复制
编辑
<div class="p-6">
  <h1 class="text-3xl font-bold mb-4">我的AI人格</h1>
  <div class="grid grid-cols-3 gap-4">
    <!-- 示例角色卡片 -->
    <div class="bg-white rounded-xl shadow p-4 hover:ring-2 ring-indigo-400 transition">
      <h2 class="text-xl font-semibold">乌萨奇</h2>
      <p class="text-gray-600 text-sm mt-2">热血中二，喜欢挑战</p>
    </div>
    <button class="border-2 border-dashed border-gray-300 rounded-xl text-gray-500 p-4 hover:bg-gray-50">
      + 创建新角色
    </button>
  </div>
</div>
2. 创建角色页面（标签 + 自定义 Prompt）
html
复制
编辑
<div class="p-6 space-y-4">
  <h1 class="text-2xl font-bold">创建你的AI角色</h1>

  <!-- 标签选项 -->
  <div>
    <label class="block font-semibold mb-1">性格关键词</label>
    <div class="flex flex-wrap gap-2">
      <span class="px-3 py-1 bg-indigo-100 text-indigo-800 rounded-full cursor-pointer hover:bg-indigo-200">中二</span>
      <span class="px-3 py-1 bg-pink-100 text-pink-800 rounded-full cursor-pointer">温柔</span>
    </div>
  </div>

  <!-- 自定义 prompt 输入 -->
  <div>
    <label class="block font-semibold mb-1">或直接填写完整Prompt</label>
    <textarea class="w-full p-2 border rounded bg-gray-50 h-32" placeholder="你是一个..."></textarea>
  </div>

  <button class="bg-indigo-600 text-white px-4 py-2 rounded">创建角色</button>
</div>
3. 群聊界面（角色交互）
html
复制
编辑
<div class="p-4 bg-gray-100 min-h-screen space-y-4">
  <div class="flex items-center gap-2">
    <img src="usagi.png" class="w-8 h-8 rounded-full animate-bounce" />
    <div class="bg-white p-3 rounded-lg shadow text-sm">
      <strong>乌萨奇：</strong>出发！去战斗吧💥
    </div>
  </div>
  <div class="text-xs text-gray-400">吉伊 正在输入...</div>

  <input class="w-full p-2 mt-4 border rounded" placeholder="输入话题或聊天内容..." />
</div>

四、后端接口设计（Flask）
接口	说明
POST /api/create-character	接收角色设定信息，生成 prompt 并保存
POST /api/chat	传入角色+话题，返回模型输出的对话内容
POST /api/generate-preview	用户填写自定义 prompt 时请求 preview 示例
POST /api/topic-anchor-check	检查话题偏离程度，返回偏移评分
POST /api/persona-score	输入回复内容和人设，判断人格一致性评分


2.0 版本 ChatSanctuary
我现在需要对 chat.html 和相关代码进行改版。以这个群聊功能为基础（保留这种选定AI角色并进行对话式+上下文理解功能），生成ChatSanctuary页面：

🧭 产品定位

一个基于AI人格群聊的互动式情绪陪伴与图像疗愈平台。用户通过表达内心困扰或情绪（树洞），AI角色进行多轮共情式讨论，最终形成一个情绪理解后的“集体祝福”图像，为用户带来被理解、被珍视的感受。

🎯 用户使用路径流程（核心闭环）

情绪输入（树洞）→ AI角色多轮对话共创 → 生成共识/建议 → 结构化为生图prompt → 图像生成 → 角色送图 & 画面展示 → 可收藏/保存/生成纪念卡片

🌱 页面流程结构（结合你现有界面）

Step 1｜用户树洞输入

UI引导文案建议：

"欢迎来到心灵小屋，留下你的声音吧～ 是心情的颜色，是今天的烦恼，还是一个说不出口的犹豫？"

输入框下建议增加提示词：

"例：我今天有点emo... | 我纠结要不要换方向 | 有点不被理解的感觉"

Step 2｜AI角色群聊（多轮上下文对话生成）

保留你当前的角色头像+颜色分栏气泡式对话风格

角色根据用户的输入的主题，以被设定的风格进行解决方案的讨论

Step 3｜达成共识 → 系统触发送图（新增模块）

系统判断角色达成结论后触发：

"🎨 吉伊、小八（用户选择的AI角色）坐下来认真讨论了你的话， 他们说：如果能把这种感觉变成一幅画，那也许你会感觉轻一点… 所以——这是我们共同为你画的。"（诸如此类的话语）

图像 + 对话总结展示卡片（如下）模型生成

🖼️ 【AI图像展示模块】

🎁 图名：静静的风里

🎨 Prompt生成语：a girl walking in soft wind with light blue scarf, white butterflies, warm light, emotional softness, healing（模型根据AI最终达成的结论进行总结，然后生成prompt给生图大模型）

🗨️ AI赠语（qwen-plus 模型生成）：

- 小八：“我希望风是轻的，像我们没说完的话。”

- 吉伊：“她会走下去的，只是需要一点点光。”

Step 4｜图像保存 & 纪念

收藏图像 → 我的心情图册

生成为纪念卡片（含图 + AI赠语 + 树洞原话）

✨ 界面优化建议（配合你的附件截图）

🎨 配色

整体基调建议从淡紫改为 治愈系渐变色 （淡蓝#B5C6E0 / 浅米黄#FAF4EC / 柔粉#FADADD）

🖼️ 聊天窗口

AI角色回复区域可加轻量弹性边框（圆角+柔阴影）

🎁 图像展示区

独立弹窗卡片：一张图+标题+AI赠语+“这幅图是为你画的”仪式感提示

图像生成完成动画：画笔图标旋转 → 淡入展示

💌 小细节增强仪式感：

“🎁 正在为你画画中...”打字状态反馈条

“图像已生成，来自3位AI朋友的共创祝福”文字缓显动画

🛠️ 技术推荐（你现有技术栈）

模块实现建议

AI角色对话

使用 qwen-plus ，每角色配置个性系统提示词（Persona Prompt）

多轮共创

角色轮流调用模型回复，统一管理上下文，群聊逻辑可本地控制

prompt生成

群聊完成后提取关键词 + 合成prompt模板（含风格）

图像生成

接入 阿里云百炼的 wanx2.1-t2i-turbo 图像接口，返回URL嵌入HTML展示

结果展示

图像 + 文字 +角色赠语 封装为html模板输出