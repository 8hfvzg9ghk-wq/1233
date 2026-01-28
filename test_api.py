import requests
import json
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 智普API配置 - 使用正确的OpenAI兼容格式
API_URL = 'https://open.bigmodel.cn/api/paas/v4/chat/completions'
API_KEY = os.environ.get('OPENAI_API_KEY', '')

def test_api():
    print("开始测试智普LLM API...")
    print(f"API地址: {API_URL}")
    print(f"API密钥: {API_KEY[:10]}...")
    print("=" * 50)
    
    try:
        # 准备测试数据
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
        
        # 发送请求
        print("发送API请求...")
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        
        response = requests.post(API_URL, headers=headers, json=test_data, timeout=30)
        
        # 检查响应
        print(f"响应状态码: {response.status_code}")
        
        if response.status_code == 200:
            print("API请求成功！")
            data = response.json()
            print("=" * 50)
            print("AI回复:")
            print(data.get("choices", [{}])[0].get("message", {}).get("content", "无回复内容"))
            print("=" * 50)
            print("测试完成: API调用正常")
            return True
        else:
            print(f"API请求失败: {response.status_code}")
            print(f"响应内容: {response.text}")
            print("测试完成: API调用失败")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"网络错误: {e}")
        print("测试完成: 网络连接失败")
        return False
    except Exception as e:
        print(f"其他错误: {e}")
        print("测试完成: 未知错误")
        return False

if __name__ == "__main__":
    test_api()