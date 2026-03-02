#!/usr/bin/python3
import ollama


def llama3(message_txt):
    client = ollama.Client(host='http://192.168.5.171:11434')
    response = client.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role":'user',
                "content": message_txt,
                # "content": "python hello world code , only code no common",
            }
        ]
    )
    return response['message']['content']
    # print(response['message']['content'])

# /etc/systemd/system/ollama.service
# 在 [Service] 區段加入 Environment="OLLAMA_HOST=0.0.0.0:11434"。
# sudo systemctl daemon-reload 
# sudo systemctl restart ollama
