import requests
import json
import base64

# 测试服务器地址
BASE_URL = 'http://127.0.0.1:5001'

def test_avatar_upload():
    print('测试头像上传功能...')
    
    # 1. 获取角色列表
    print('\n1. 获取角色列表:')
    response = requests.get(f'{BASE_URL}/api/characters')
    if response.status_code == 200:
        characters = response.json()
        print(f'获取到 {len(characters)} 个角色')
        for char in characters:
            print(f'  - {char["name"]}: avatar_type={char.get("avatar_type", "未设置")}, avatar_value={"有值" if char.get("avatar_value") else "无值"}')
    else:
        print(f'获取角色列表失败: {response.status_code}')
        return
    
    if not characters:
        print('没有角色可测试')
        return
    
    # 2. 测试更新第一个角色的头像
    test_character = characters[0]
    character_id = test_character['id']
    print(f'\n2. 测试更新角色 "{test_character["name"]}" 的头像:')
    
    # 创建一个简单的测试图片数据（1x1像素的红色PNG）
    test_image_data = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8/5+hHgAHggJ/PchI7wAAAABJRU5ErkJggg=='
    
    # 更新角色头像
    update_data = {
        'name': test_character['name'],
        'personality': test_character['personality'],
        'description': test_character['description'],
        'system_prompt': test_character['system_prompt'],
        'avatar_type': 'upload',
        'avatar_value': test_image_data
    }
    
    response = requests.put(
        f'{BASE_URL}/api/characters/{character_id}',
        headers={'Content-Type': 'application/json'},
        data=json.dumps(update_data)
    )
    
    if response.status_code == 200:
        print('头像更新成功!')
    else:
        print(f'头像更新失败: {response.status_code}, {response.text}')
        return
    
    # 3. 验证更新结果
    print('\n3. 验证更新结果:')
    response = requests.get(f'{BASE_URL}/api/characters/{character_id}')
    if response.status_code == 200:
        updated_character = response.json()
        print(f'更新后的头像类型: {updated_character.get("avatar_type")}')
        print(f'更新后的头像数据: {"有值" if updated_character.get("avatar_value") else "无值"}')
        
        if updated_character.get('avatar_type') == 'upload' and updated_character.get('avatar_value'):
            print('✅ 头像上传功能正常!')
        else:
            print('❌ 头像上传功能异常!')
    else:
        print(f'获取更新后角色信息失败: {response.status_code}')
    
    # 4. 测试表情头像
    print('\n4. 测试表情头像:')
    update_data['avatar_type'] = 'emoji'
    update_data['avatar_value'] = '😀'
    
    response = requests.put(
        f'{BASE_URL}/api/characters/{character_id}',
        headers={'Content-Type': 'application/json'},
        data=json.dumps(update_data)
    )
    
    if response.status_code == 200:
        print('表情头像更新成功!')
        
        # 验证表情头像
        response = requests.get(f'{BASE_URL}/api/characters/{character_id}')
        if response.status_code == 200:
            updated_character = response.json()
            if updated_character.get('avatar_type') == 'emoji' and updated_character.get('avatar_value') == '😀':
                print('✅ 表情头像功能正常!')
            else:
                print('❌ 表情头像功能异常!')
    else:
        print(f'表情头像更新失败: {response.status_code}, {response.text}')

if __name__ == '__main__':
    test_avatar_upload()