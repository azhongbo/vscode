#!/usr/bin/python3
import subprocess
import json
import ollama
import ollama

# 1. 配置遠端伺服器資訊
REMOTE_SERVER = "http://192.168.5.107:11434"
MODEL_NAME = "llama3.1:latest"

# 初始化 Client
client = ollama.Client(host=REMOTE_SERVER)

# 2. 定義一個簡單的工具函數
def calculate_sum(a, b):
    return a + b

def run_conversation():
    # 3. 定義工具 Schema
    tools = [
        {
            'type': 'function',
            'function': {
                'name': 'calculate_sum',
                'description': '計算兩個數字的和',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'a': {'type': 'number', 'description': '第一個數字'},
                        'b': {'type': 'number', 'description': '第二個數字'},
                    },
                    'required': ['a', 'b'],
                },
            },
        },
    ]

    messages = [{'role': 'user', 'content': '請問 9876 加 1234 等於多少？'}]
    print(f"--- [連線至 {REMOTE_SERVER}] ---")
    print(f"--- 用戶提問: {messages[0]['content']} ---")

    # 4. 第一次請求：詢問 Llama 是否需要工具
    response = client.chat(
        model=MODEL_NAME,
        messages=messages,
        tools=tools,
    )

    # 檢查是否有工具呼叫請求
    if response.get('message', {}).get('tool_calls'):
        # 將 Llama 的回覆（包含 tool_calls）加入對話歷史
        messages.append(response['message'])

        for tool in response['message']['tool_calls']:
            if tool['function']['name'] == 'calculate_sum':
                args = tool['function']['arguments']
                
                # 執行本地 Python 函數
                result = calculate_sum(args['a'], args['b'])
                print(f"--- 執行工具: calculate_sum({args['a']}, {args['b']}) -> 結果: {result} ---")

                # 5. 將工具執行結果回傳給伺服器
                messages.append({
                    'role': 'tool',
                    'content': str(result),
                    'name': tool['function']['name']
                })

        # 6. 獲取最終總結回答
        final_response = client.chat(
            model=MODEL_NAME,
            messages=messages,
        )
        print(f"--- Llama 最終回答: {final_response['message']['content']} ---")
    else:
        print(f"--- Llama 直接回答: {response['message']['content']} ---")

if __name__ == '__main__':
    run_conversation()