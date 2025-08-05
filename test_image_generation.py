#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import time
from config import Config

def test_image_generation():
    """测试图像生成API"""
    
    # 获取API密钥
    api_key = Config.QWEN_API_KEY
    print(f"使用API密钥: {api_key[:10]}...{api_key[-10:] if len(api_key) > 20 else api_key}")
    
    # 设置请求头
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
        'X-DashScope-Async': 'enable'
    }
    
    # 设置请求数据
    data = {
        "model": "wanx2.1-t2i-turbo",
        "input": {
            "prompt": "一个温馨的场景，柔和的粉色世界中，一群温柔的生物围绕着朋友坐在漂浮的云朵上。闪闪发光的光线碎片在温暖的粉色、黄色和红色中旋转，形成一道温柔的彩虹。"
        },
        "parameters": {
            "size": "1024*1024",
            "n": 1
        }
    }
    
    print("正在创建图像生成任务...")
    print(f"请求数据: {json.dumps(data, ensure_ascii=False, indent=2)}")
    
    try:
        # 步骤1: 创建异步任务
        response = requests.post(
            'https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis',
            headers=headers,
            json=data,
            timeout=30
        )
        
        print(f"任务创建响应状态码: {response.status_code}")
        print(f"响应头: {dict(response.headers)}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"任务创建响应: {json.dumps(result, ensure_ascii=False, indent=2)}")
            
            task_id = result.get('output', {}).get('task_id')
            if task_id:
                print(f"任务ID: {task_id}")
                
                # 步骤2: 轮询查询任务结果
                max_attempts = 30
                for attempt in range(max_attempts):
                    time.sleep(2)
                    
                    query_url = f'https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}'
                    query_response = requests.get(
                        query_url,
                        headers={'Authorization': f'Bearer {api_key}'},
                        timeout=10
                    )
                    
                    print(f"查询任务状态 (第{attempt+1}次): {query_response.status_code}")
                    
                    if query_response.status_code == 200:
                        query_result = query_response.json()
                        task_status = query_result.get('output', {}).get('task_status')
                        print(f"任务状态: {task_status}")
                        
                        if task_status == 'SUCCEEDED':
                            results = query_result.get('output', {}).get('results', [])
                            if results:
                                image_url = results[0]['url']
                                print(f"图像生成成功: {image_url}")
                                return image_url
                            else:
                                print("任务成功但未找到图像结果")
                                break
                        elif task_status == 'FAILED':
                            error_msg = query_result.get('output', {}).get('message', '未知错误')
                            print(f"任务失败: {error_msg}")
                            break
                        elif task_status in ['PENDING', 'RUNNING']:
                            print(f"任务进行中...")
                            continue
                        else:
                            print(f"未知任务状态: {task_status}")
                            print(f"完整响应: {json.dumps(query_result, ensure_ascii=False, indent=2)}")
                    else:
                        print(f"查询失败: {query_response.status_code} - {query_response.text}")
                        
                print("任务超时或失败")
            else:
                print("未获取到task_id")
        else:
            print(f"API调用失败: {response.status_code}")
            print(f"错误响应: {response.text}")
            try:
                error_json = response.json()
                print(f"错误详情: {json.dumps(error_json, ensure_ascii=False, indent=2)}")
            except:
                pass
                
    except Exception as e:
        print(f"请求异常: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    test_image_generation()