import sqlite3
import os
from config import Config

# 连接数据库
config = Config()
conn = sqlite3.connect(config.DATABASE_PATH)
cursor = conn.cursor()

print('修复头像数据...')

# 更新所有avatar_type为NULL或空的记录为'initial'
cursor.execute('''
    UPDATE characters 
    SET avatar_type = 'initial' 
    WHERE avatar_type IS NULL OR avatar_type = ''
''')

# 清空所有avatar_value为NULL的记录
cursor.execute('''
    UPDATE characters 
    SET avatar_value = NULL 
    WHERE avatar_type = 'initial'
''')

conn.commit()

print('检查修复后的数据:')
cursor.execute('SELECT id, name, avatar_type, avatar_value FROM characters')
for row in cursor.fetchall():
    print(f'ID: {row[0]}, Name: {row[1]}, Type: {row[2]}, Value: {"有值" if row[3] else "无值"}')

conn.close()
print('头像数据修复完成！')