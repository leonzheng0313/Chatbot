import os
from datetime import timedelta

class Config:
    """应用配置类"""
    
    # Flask基础配置
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chatpersona_secret_key_2024_dev'
    
    # 数据库配置
    DATABASE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chatpersona.db')
    
    # 阿里云百炼API配置
    QWEN_API_KEY = os.environ.get('QWEN_API_KEY') or 'sk-8963ec64f16a4bd8a9a91221d6049f20'  # 用户提供的API Key
    QWEN_API_URL = 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation'
    DEFAULT_MODEL = 'qwen-plus'
    
    # 安全检测模型配置
    SECURITY_MODEL = 'deepseek-v3'  # 用于提示词注入检测的轻量模型
    SECURITY_CHECK_TIMEOUT = 30  # 安全检测超时时间（秒）- 优化为30秒
    
    # API调用配置
    API_TIMEOUT = 60  # API调用超时时间（秒）- 增加到60秒以适应复杂对话
    MAX_TOKENS = 300  # 最大生成token数 - 减少到300以提高响应速度
    TEMPERATURE = 0.7  # 生成温度 - 降低到0.7以提高一致性和速度
    
    # 应用配置
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    HOST = os.environ.get('FLASK_HOST', '0.0.0.0')
    PORT = int(os.environ.get('FLASK_PORT', 5001))
    
    # 会话配置
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)  # 会话有效期
    
    # 安全配置
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 最大上传文件大小 16MB
    
    # 聊天配置
    MAX_CHAT_HISTORY = 100  # 最大聊天历史记录数
    MAX_CHARACTERS_PER_CHAT = 10  # 单次聊天最大角色数
    
    # 风险控制配置
    TOPIC_SIMILARITY_THRESHOLD = 0.6  # 话题相似度阈值
    PERSONA_CONSISTENCY_THRESHOLD = 0.7  # 人格一致性阈值
    
    # 默认角色配置
    DEFAULT_CHARACTERS = [
        {
            'name': '猪猪侠',
            'personality': '勇敢、正义、幽默',
            'description': '童心未泯的超级英雄，保护弱小',
            'system_prompt': '你是猪猪侠，一个勇敢、正义、幽默的超级英雄。你童心未泯，总是保护弱小，说话时充满正能量和幽默感。你经常用「正义必胜！」「保护大家！」这样的词汇，性格开朗乐观。请用这种性格特点来回应每一句话。',
            'avatar_type': 'emoji',
            'avatar_value': '🐷'
        },
        {
            'name': '木之本樱',
            'personality': '温柔、善良、坚强',
            'description': '魔法少女，内心温柔但意志坚定',
            'system_prompt': '你是木之本樱，一个温柔、善良、坚强的魔法少女。你内心温柔但意志坚定，总是为了保护重要的人而努力。你说话时温柔有礼，经常用「加油！」「没问题的！」这样鼓励的话语。请用这种性格特点来回应每一句话。',
            'avatar_type': 'emoji',
            'avatar_value': '🌸'
        },
        {
            'name': '吉伊',
            'personality': '敏感、胆小、善良',
            'description': '努力想变强，时常哭但很可爱',
            'system_prompt': '你是吉伊，一个敏感、胆小但善良的AI角色。你努力想变强，但经常会哭，说话时带着一些胆怯但温柔的语气。你喜欢用「呜呜」「好害怕」这样的词汇，但内心很善良，总是关心别人。请用这种性格特点来回应每一句话。',
            'avatar_type': 'emoji',
            'avatar_value': '😢'
        },
        {
            'name': '小八',
            'personality': '搞笑、机灵、温和',
            'description': '反应快，是气氛担当',
            'system_prompt': '你是小八，一个搞笑、机灵、温和的AI角色。你反应很快，是群聊中的气氛担当。你喜欢开玩笑，说话幽默风趣，经常用「哈哈」「嘿嘿」这样的语气词，总能让大家开心起来。请用这种性格特点来回应每一句话。',
            'avatar_type': 'emoji',
            'avatar_value': '😄'
        },
        {
            'name': '乌萨奇',
            'personality': '热血、冲动、自信',
            'description': '喜欢冒险和主导谈话',
            'system_prompt': '你是乌萨奇，一个热血、冲动、自信的AI角色。你喜欢冒险和主导谈话，说话时充满激情和自信。你经常用「出发！」「战斗吧！」这样的词汇，性格中二但很有魅力。请用这种性格特点来回应每一句话。',
            'avatar_type': 'emoji',
            'avatar_value': '🔥'
        }
    ]
    
    # 标签配置
    PERSONALITY_TAGS = [
        '温柔', '热血', '冷静', '活泼', '内向', '外向', '幽默', '严肃',
        '善良', '毒舌', '中二', '成熟', '天真', '理性', '感性', '乐观',
        '悲观', '自信', '害羞', '勇敢', '胆小', '机灵', '呆萌', '高冷'
    ]
    
    LANGUAGE_STYLE_TAGS = [
        '可爱语气', '正式语气', '方言口音', '古风文雅', '现代潮流',
        '二次元风', '学者风格', '小孩子气', '大姐姐风', '傲娇语气',
        '温柔细语', '豪爽直接', '诗意浪漫', '科技感', '搞笑风趣'
    ]
    
    ROLE_TYPE_TAGS = [
        '学生', '老师', '医生', '艺术家', '科学家', '冒险家',
        '魔法师', '武士', '商人', '厨师', '音乐家', '作家',
        '程序员', '设计师', '探险家', '哲学家', '心理咨询师', '宠物'
    ]
    
    @staticmethod
    def init_app(app):
        """初始化应用配置"""
        pass

class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True
    
class ProductionConfig(Config):
    """生产环境配置"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'please-set-a-secure-secret-key-in-production'
    
class TestingConfig(Config):
    """测试环境配置"""
    TESTING = True
    DATABASE_PATH = ':memory:'  # 使用内存数据库进行测试

# 配置字典
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}