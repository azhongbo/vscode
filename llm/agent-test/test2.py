#!/usr/bin/python3
import subprocess
import json
import ollama

llm01 = "llama3.2:3b"     ## NB Nvidia 1050 
llm02 = "codellama:7b"    ## code llama 開發   # curl http://localhost:11434/api/generate -d "{\"model\": \"codellama:7b\", \"keep_alive\": -1}"
llm03 = "gemma3:4b"       # gemma3:4b 圖片分析 # curl http://localhost:11434/api/generate -d "{\"model\": \"gemma3:4b\", \"keep_alive\": -1}" 
llm04 = "llama3.1:latest" # llama3.1  中文    # curl http://localhost:11434/api/generate -d "{\"model\": \"llama3.1:latest\", \"keep_alive\": -1}"

llm = llm04
server = "192.168.5.105"
client = ollama.Client(host=f"http://{server}:11434")  # 建立連接到遠端 ollama 伺服器的客戶端

# messages = [{"role": "user", "content": "在当前目录找 README 并总结要点"}]  # 初始化對話訊息列表，包含使用者指令
messages = [{"role": "user", "content": "Ubuntu 寫出一個查詢ip 的 python3 程式, 程式名稱為 okok.py"}]  # 初始化對話訊息列表，包含使用者指令



tools = [
    {
        'type': 'function',
        'function': {
            'name': 'bash',
            'description': '執行 bash 命令',
            'parameters': {
                'type': 'object',
                'properties': {
                    'command': {'type': 'string', 'description': '要執行的命令'},
                },
                'required': ['command'],
            },
        },
    },
    {
        'type': 'function',
        'function': {
            'name': 'sudo_bash',
            'description': '以 sudo 權限執行命令，修改系統設定或安裝軟體',
            'parameters': {
                'type': 'object',
                'properties': {
                    'command': {'type': 'string', 'description': '要執行的 sudo 命令'},
                },
                'required': ['command'],
            },
        },
    }
]

def execute_tools(tool_calls):
    results = []
    import subprocess
    for tool_call in tool_calls:
        name = tool_call['function']['name']
        args = tool_call['function']['arguments']
        
        if name == 'bash' or name == 'sudo_bash':
            cmd = args['command']
            print(f"--- 正在執行系統命令: {cmd} ---")
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            output = result.stdout if result.stdout else result.stderr
            results.append(f"Tool {name} output: {output}")
    return "\n".join(results)

count = 0
while True:
    count += 1
    resp = client.chat(model=llm, messages=messages, tools=tools)
    
    # 取得回傳訊息
    message = resp['message']
    
    # 3. 檢查是否有工具呼叫
    if not message.get('tool_calls'):
        print(f"## 回應第 {count} 次 # 沒有工具需求，輸出最終結果：")
        print(message['content'])
        break
    
    print(f"## 第 {count} 次迭代：模型要求執行工具 ##")
    # 將模型的 tool_calls 訊息加入歷史（這對維持對話脈絡很重要）
    messages.append(message)
    
    # 執行工具並取得結果
    tool_results = execute_tools(message['tool_calls'])
    
    # 將工具執行結果作為 'tool' 角色（或 user 角色）回饋給模型
    messages.append({"role": "tool", "content": tool_results}) 
    # 註：有些 Ollama 版本若不支援 role: tool，可暫時改回 role: user