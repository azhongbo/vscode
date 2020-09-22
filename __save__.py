#!/usr/bin/python3
import random,os,sys
def makeCode(MyCodeTitle,MyCodeString,MyCodeName):

    package1 = '"onCommand:extension.MyCodeName",'.replace("MyCodeName",MyCodeName)

    package2 = '''
            {
                "command": "extension.MyCodeName",
                "title": "MyCodeTitle"
            },
    '''.replace("MyCodeName",MyCodeName).replace("MyCodeTitle",MyCodeTitle)

    extension = '''
        context.subscriptions.push(vscode.commands.registerCommand('extension.MyCodeName', () => {
            var codeStr = `MyCodeString`
            pasteData(codeStr)
        }));
    '''.replace("MyCodeName",MyCodeName).replace("MyCodeString",MyCodeString).replace("\\","\\\\")

    return package1,package2,extension


    