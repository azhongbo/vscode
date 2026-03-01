"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const vscode = require("vscode");

const CursorMonitor = require("./cursorMonitor");


let monitor;

function activate(context) {
    console.log('擴充功能已啟動');

    // 建立實例並啟動 (設定 3000 毫秒)
    monitor = new CursorMonitor(3000);
    monitor.start(context);
}

exports.activate = activate;
// this method is called when your extension is deactivated
function deactivate() {
    if (monitor) {
        monitor.stop();
    }
}
exports.deactivate = deactivate;
