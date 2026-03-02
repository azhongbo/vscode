"use strict";
const vscode = require("vscode");

class EditorWriter {
    constructor() {
        this.currentSuggestion = "";
    }

    /**
     * 註冊行內補全提供者
     */
    register(context) {
        const provider = {
            provideInlineCompletionItems: (document, position, context, token) => {
                if (!this.currentSuggestion) return [];

                // 建立一個補全項目
                const item = new vscode.InlineCompletionItem(this.currentSuggestion);
                
                // 設定插入範圍：從游標目前的下一行開始（如您要求）
                // 註：Inline Completion 通常是接在游標後，若要強制下一行，建議在內容前加 \n
                item.insertText = `\n${this.currentSuggestion}`;
                
                // 顯示後清空快取，避免重複觸發
                this.currentSuggestion = ""; 
                
                return [item];
            },
        };

        const disposable = vscode.languages.registerInlineCompletionItemProvider({ pattern: '**' }, provider);
        context.subscriptions.push(disposable);
    }

    /**
     * 更新目前的 AI 建議內容，並觸發 VS Code 顯示
     */
    setSuggestion(text) {
        this.currentSuggestion = text;
        // 觸發編輯器重新請求 Inline Completion
        vscode.commands.executeCommand('editor.action.inlineSuggest.trigger');
    }
}

module.exports = EditorWriter;