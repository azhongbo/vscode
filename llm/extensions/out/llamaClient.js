"use strict";
const http = require("http");

class LlamaClient {
    constructor(endpoint = "192.168.5.105", port = 11434) {
        this.options = {
            hostname: endpoint,
            port: port,
            path: "/api/generate",
            method: "POST",
            headers: { "Content-Type": "application/json" }
        };
    }

    async getCompletion(prefix, suffix) {
        const prompt = `Context Prefix:\n${prefix}\n\nContext Suffix:\n${suffix}\n\nTask: Based on the code above, provide only the next line of code or a short suggestion. No explanations.`;
        const postData = JSON.stringify({
            model: "llama3.1:latest",
            prompt: prompt,
            stream: false // 設為 false 比較容易處理回傳字串
        });

        return new Promise((resolve, reject) => {
            const req = http.request(this.options, (res) => {
                let data = "";
                res.on("data", (chunk) => { data += chunk; });
                res.on("end", () => {
                    try {
                        const response = JSON.parse(data);
                        resolve(response.response || "");
                    } catch (e) { reject("Parse Error: " + e.message); }
                });
            });

            req.on("error", (e) => { reject("Ollama Error: " + e.message); });
            req.write(postData);
            req.end();
        });
    }
}
module.exports = LlamaClient;