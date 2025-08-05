#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ChatPersona 启动脚本

使用方法:
    python run.py                    # 开发模式启动
    python run.py --prod             # 生产模式启动
    python run.py --config testing   # 指定配置启动
"""

import os
import sys
import argparse
from app import app, init_db

def main():
    parser = argparse.ArgumentParser(description='ChatPersona AI人格社交平台')
    parser.add_argument('--config', 
                       choices=['development', 'production', 'testing'],
                       default='development',
                       help='指定配置环境 (默认: development)')
    parser.add_argument('--prod', 
                       action='store_true',
                       help='生产模式启动 (等同于 --config production)')
    parser.add_argument('--host', 
                       default=None,
                       help='指定主机地址')
    parser.add_argument('--port', 
                       type=int,
                       default=None,
                       help='指定端口号')
    parser.add_argument('--debug', 
                       action='store_true',
                       help='启用调试模式')
    
    args = parser.parse_args()
    
    # 设置配置环境
    if args.prod:
        config_name = 'production'
    else:
        config_name = args.config
    
    os.environ['FLASK_CONFIG'] = config_name
    
    # 重新加载配置
    from config import config
    app.config.from_object(config[config_name])
    
    # 初始化数据库
    print("正在初始化数据库...")
    init_db()
    print("数据库初始化完成！")
    
    # 获取运行参数
    host = args.host or app.config.get('HOST', '0.0.0.0')
    port = args.port or app.config.get('PORT', 5001)
    debug = args.debug or app.config.get('DEBUG', False)
    
    print(f"\n🚀 ChatPersona 正在启动...")
    print(f"📍 访问地址: http://{host}:{port}")
    print(f"🔧 运行模式: {config_name}")
    print(f"🐛 调试模式: {'开启' if debug else '关闭'}")
    print(f"💾 数据库路径: {app.config['DATABASE_PATH']}")
    
    if app.config['QWEN_API_KEY'] == 'sk-XXXX':
        print("⚠️  警告: 使用默认API Key，请在应用中设置你的阿里云百炼API Key")
    
    print("\n按 Ctrl+C 停止服务器\n")
    
    try:
        app.run(
            host=host,
            port=port,
            debug=debug,
            use_reloader=debug  # 只在调试模式下启用自动重载
        )
    except KeyboardInterrupt:
        print("\n👋 ChatPersona 已停止运行")
    except Exception as e:
        print(f"❌ 启动失败: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()