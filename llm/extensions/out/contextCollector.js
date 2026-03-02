"use strict";
const vscode = require("vscode");

class ContextCollector {
    static getContext(editor) {
        if (!editor) return { prefix: "", suffix: "" };

        const position = editor.selection.active;
        const document = editor.document;

        // 計算範圍：前 10 行到後 10 行
        const startLine = Math.max(0, position.line - 10);
        const endLine = Math.min(document.lineCount - 1, position.line + 10);

        // 取得游標前的內容
        const prefixRange = new vscode.Range(startLine, 0, position.line, position.character);
        const prefix = document.getText(prefixRange);

        // 取得游標後的內容
        const suffixRange = new vscode.Range(position.line, position.character, endLine, document.lineAt(endLine).text.length);
        const suffix = document.getText(suffixRange);

        return { prefix, suffix };
    }
}
module.exports = ContextCollector;