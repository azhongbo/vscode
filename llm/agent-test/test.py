#!/usr/bin/python3
import os
import ollama  # 導入 ollama 套件

server = "192.168.5.105"

llm01 = "llama3.2:3b"     ## NB Nvidia 1050 
llm02 = "codellama:7b"    ## code llama 開發   # curl http://localhost:11434/api/generate -d "{\"model\": \"codellama:7b\", \"keep_alive\": -1}"
llm03 = "gemma3:4b"       # gemma3:4b 圖片分析 # curl http://localhost:11434/api/generate -d "{\"model\": \"gemma3:4b\", \"keep_alive\": -1}" 
llm04 = "llama3.1:latest" # llama3.1  中文    # curl http://localhost:11434/api/generate -d "{\"model\": \"llama3.1:latest\", \"keep_alive\": -1}"

client = ollama.Client(host=f"http://{server}:11434")  # 建立連接到遠端 ollama 伺服器的客戶端

# messages = [{"role": "user", "content": "在当前目录找 README 并总结要点"}]  # 初始化對話訊息列表，包含使用者指令
messages = [{"role": "user", "content": "查詢ip"}]  # 初始化對話訊息列表，包含使用者指令

tools = [
    {"name": "read_file", "description": "读取文件内容"},  # 保持原有的檔案讀取工具
    {"name": "bash", "description": "执行bash命令"},      # 保持原有的bash執行工具
    {"name": "sudo_bash", "description": "以sudo權限執行bash命令，用於安裝軟體和系統設定"},  # 新增sudo工具用於Ubuntu Desktop安裝
    {"name": "apt_update", "description": "更新apt套件庫索引"},  # 新增apt更新工具
    {"name": "apt_install", "description": "安裝套件，使用 sudo apt install"},  # 新增套件安裝工具
    {"name": "apt_remove", "description": "移除套件，使用 sudo apt remove"}   # 新增套件移除工具
]

def execute_tools(tool_calls):  # 定義執行工具的函數，接收模型的工具呼叫列表
    results = []  # 初始化儲存所有工具執行結果的列表
    for tool_call in tool_calls:  # 遍歷每個工具呼叫
        if tool_call['function']['name'] == 'read_file':  # 檢查工具名稱是否為 read_file
            filename = tool_call['function']['arguments']['filename']  # 從參數中提取檔案名稱
            with open(filename, 'r') as f:  # 開啟檔案以讀取模式
                content = f.read()  # 讀取檔案內容
            results.append(f"read_file({filename}): {content[:500]}...")  # 將結果加入列表（限制長度）
        elif tool_call['function']['name'] == 'bash':  # 檢查工具名稱是否為 bash
            cmd = tool_call['function']['arguments']['command']  # 從參數中提取命令
            import subprocess  # 導入 subprocess 模組
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)  # 執行 bash 命令
            results.append(f"bash({cmd}): {result.stdout or result.stderr}")  # 將命令結果加入列表
    return "\n".join(results)  # 將所有結果合併成單一字串返回


count = 0
# 開始代理迴圈，持續執行直到任務完成
while True:

    count = count + 1

    resp = client.chat(model=llm04, messages=messages, tools=tools)  # 呼叫模型執行對話，傳入訊息和工具
    
    # 檢查回應是否有工具呼叫需求
    if not hasattr(resp['message'], 'tool_calls') or not resp['message'].tool_calls:

        print("## 1 # 沒有工具呼叫，印出模型的最終回應並結束#########################")
        print(resp['message']['content'])  # 如果沒有工具呼叫，印出模型的最終回應並結束
        break  # 跳出迴圈，結束代理流程
    
    print(f"## 2 # 執行模型要求的工具呼叫 {count} #########################")
    print(resp['message'].tool_calls)
    results = execute_tools(resp['message'].tool_calls)  # 執行模型要求的工具呼叫
    messages.append({"role": "user", "content": results})  # 將工具執行結果加入對話歷史，繼續下一輪
    print("\n\n")
    
