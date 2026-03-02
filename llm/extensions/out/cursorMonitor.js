"use strict";
const vscode = require("vscode");
const ContextCollector = require("./contextCollector");
const LlamaClient = require("./llamaClient");
const EditorWriter = require("./editorWriter");

class CursorMonitor {
    constructor(delay = 3000) {
        this.delay = delay;
        this.timeout = null;
        this.aiClient = new LlamaClient();
        this.writer = new EditorWriter(); // 建立實例
    }

    start(context) {
        console.log('CursorMonitor 已啟動 (Copilot 模式)');
        
        // 註冊 Inline Provider
        this.writer.register(context);

        const disposable = vscode.window.onDidChangeTextEditorSelection(() => {
            this.resetTimer();
        });
        context.subscriptions.push(disposable);
    }

    resetTimer() {
        if (this.timeout) clearTimeout(this.timeout);
        this.timeout = setTimeout(() => {
            this.handleIdle();
        }, this.delay);
    }

    async handleIdle() {
        const editor = vscode.window.activeTextEditor;
        if (!editor) return;

        const { prefix, suffix } = ContextCollector.getContext(editor);
        const statusBar = vscode.window.setStatusBarMessage("$(sync~spin) Llama 正在生成建議...");

        try {
            const aiResult = await this.aiClient.getCompletion(prefix, suffix);
            if (aiResult) {
                // 將結果交給 writer，它會觸發淡灰色預覽
                this.writer.setSuggestion(aiResult.trim());
            }
        } catch (error) {
            console.error(error);
        } finally {
            statusBar.dispose();
        }
    }

    stop() {
        if (this.timeout) clearTimeout(this.timeout);
    }
}
module.exports = CursorMonitor;