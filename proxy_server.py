from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json
import os
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

# 加载环境变量
load_dotenv()

# 智普API配置 - 使用新的官方API端点
API_URL = 'https://open.bigmodel.cn/api/paas/v4/chat/completions'
API_KEY = os.environ.get('OPENAI_API_KEY', '')

def test_api_direct():
    """直接测试API，获取详细响应"""
    print("[代理服务器] 测试API连接...")
    try:
        test_data = {
            "model": "chatglm_turbo",
            "messages": [
                {
                    "role": "system",
                    "content": "你是可爱的双双哈基米AI助手，要以友好、活泼的语气回答用户问题，使用可爱的表情符号。"
                },
                {
                    "role": "user",
                    "content": "你好，测试一下API连接"
                }
            ],
            "temperature": 0.7,
            "max_tokens": 500
        }
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        
        response = requests.post(API_URL, headers=headers, json=test_data, timeout=30)
        print(f"[代理服务器] API响应状态: {response.status_code}")
        print(f"[代理服务器] API响应内容: {response.text[:200]}...")
        return response
    except Exception as e:
        print(f"[代理服务器] API测试错误: {e}")
        return None

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        # 获取前端发送的数据
        data = request.json
        user_message = data.get('message', '')
        print(f"[代理服务器] 收到用户消息: {user_message}")
        
        # 准备API请求数据 - 使用新的官方OpenAI兼容格式
        request_data = {
            "model": "chatglm_turbo",
            "messages": [
                {
                    "role": "system",
                    "content": "你是可爱的双双哈基米AI助手，要以友好、活泼的语气回答用户问题，使用可爱的表情符号。"
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            "temperature": 0.7,
            "max_tokens": 1024
        }
        
        # 发送API请求
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        
        print(f"[代理服务器] 发送API请求到: {API_URL}")
        response = requests.post(API_URL, headers=headers, json=request_data, timeout=30)
        
        # 检查响应状态
        print(f"[代理服务器] API响应状态: {response.status_code}")
        print(f"[代理服务器] API响应内容: {response.text[:300]}...")
        
        if not response.ok:
            # 如果API请求失败，抛出异常
            raise Exception(f"API请求失败: {response.status_code} - {response.text}")
        
        # 解析响应数据
        api_data = response.json()
        print(f"[代理服务器] API响应结构: {json.dumps(api_data, indent=2)[:500]}...")
        
        # 尝试获取AI回复 - 使用OpenAI兼容格式
        if 'choices' in api_data and len(api_data['choices']) > 0:
            choice = api_data['choices'][0]
            if 'message' in choice and 'content' in choice['message']:
                ai_response = choice['message']['content']
                if ai_response:
                    print(f"[代理服务器] 成功获取AI回复")
                    return jsonify({'response': ai_response})
                else:
                    # 如果AI回复为空，抛出异常
                    raise Exception("AI回复为空")
        else:
            # 如果没有获取到有效的回复，抛出异常
            raise Exception("无法解析AI回复")
        
    except Exception as e:
        print(f"[代理服务器] API请求错误: {e}")
        # 返回指定的错误消息
        error_message = '无法连接大语言模型，休息一下吧！'
        return jsonify({'response': error_message})

if __name__ == '__main__':
    # 启动前测试API连接
    test_api_direct()
    print("[代理服务器] 启动中...")
    app.run(port=5000, debug=True)