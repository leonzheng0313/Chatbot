import sqlite3
import os

def check_avatar_data():
    db_path = 'chatpersona.db'
    if not os.path.exists(db_path):
        print(f"数据库文件 {db_path} 不存在")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # 检查表结构
        cursor.execute("PRAGMA table_info(characters)")
        columns = cursor.fetchall()
        print("Characters表结构:")
        for col in columns:
            print(f"  {col[1]} ({col[2]})")
        
        print("\n角色数据:")
        cursor.execute("SELECT id, name, avatar_type, avatar_value FROM characters")
        characters = cursor.fetchall()
        
        for char in characters:
            print(f"ID: {char[0]}, Name: {char[1]}, Avatar Type: {char[2]}, Avatar Value: {char[3][:50] if char[3] else 'None'}...")
        
        conn.close()
        
    except Exception as e:
        print(f"查询数据库时出错: {e}")

if __name__ == "__main__":
    check_avatar_data()