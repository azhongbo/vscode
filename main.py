#!/usr/bin/python3
import random,os
# from bs4 import BeautifulSoup

os.system("./default.py")

package1  = ""
package2  = ""
extension = ""

# extensionFile = '/home/ubuntu-mate/.vscode/extensions/ryanCode/out/extension.js'
# packageFile   = '/home/ubuntu-mate/.vscode/extensions/ryanCode/package.json'

if os.name == 'posix':
    home_folder = os.environ['HOME']
    extensionFile = f'{home_folder}/.vscode/extensions/ryanCode/out/extension.js'
    packageFile   = f'{home_folder}/.vscode/extensions/ryanCode/package.json'


if os.name == 'nt':
    home_folder = os.environ['USERPROFILE']
    extensionFile = f'{home_folder}\\.vscode/extensions\\ryanCode\\out\\extension.js'
    packageFile   = f'{home_folder}\\.vscode\extensions\\ryanCode\\package.json'



def getData(name):
    global package1,package2,extension

    # 亂術檔案名稱
    MyCodeName = ""
    for i in range(1,6):
        MyCodeName = MyCodeName + chr(random.randint(65,89))

    with os.popen("./" + name + " package1 " + MyCodeName ) as myNet:  # <<--- 執行 os.system("./name.py")
        for myString in myNet.readlines():
            package1 = package1 + myString


    with os.popen("./" + name + " package2 " + MyCodeName ) as myNet:  # <<--- 執行 os.system("./name.py")
        for myString in myNet.readlines():
            package2 = package2 + myString


    with os.popen("./" + name + " extension " + MyCodeName ) as myNet:  # <<--- 執行 os.system("./name.py")
        for myString in myNet.readlines():
            extension = extension + myString



    # for p in BeautifulSoup( data , 'html.parser').find_all('div',id='package1'):
    #     package1 = package1 + p.text

    # for p in BeautifulSoup( data , 'html.parser').find_all('div',id='package2'):
    #     package2 = package2 + p.text

    # for p in BeautifulSoup( data , 'html.parser').find_all('div',id='extension'):
    #     extension = extension + p.text






#### 建立檔案 ##############################################
def saveFile():
    global package1,package2,extension,extensionFile,packageFile
    
    data1 = '''{
        "name": "helloworld",
        "displayName": "helloWorld",
        "description": "hello",
        "version": "1.0.8",
        "publisher": "premparihar",
        "engines": {
            "vscode": "^1.27.0"
        },
        "categories": [
            "Other"
        ],
        "activationEvents": [
            %s
            "onCommand:extension.sayHello"
        ],
        "main": "./out/extension",
        "contributes": {
            "commands": [
                %s
                {
                    "command": "extension.sayHello",
                    "title": "Hello World"
                }
            ]
        },
        "scripts": {
            "vscode:prepublish": "npm run compile",
            "compile": "tsc -p ./",
            "watch": "tsc -watch -p ./",
            "postinstall": "node ./node_modules/vscode/bin/install",
            "test": "npm run compile && node ./node_modules/vscode/bin/test"
        },
        "devDependencies": {
            "typescript": "^2.6.1",
            "vscode": "^1.1.21",
            "tslint": "^5.8.0",
            "@types/node": "^8.10.25",
            "@types/mocha": "^2.2.42"
        },
        "repository": {
            "type": "git",
            "url": "https://github.com/ppparihar/vse-hello.git"
        },
        "bugs": {
            "url": "https://github.com/ppparihar/vse-hello/issues"
        },
        "__metadata": {
            "id": "d0e241b2-996d-4925-8e66-52b9101dbd7d",
            "publisherId": "837b2939-3813-4e66-a4f8-9fffec5374fa",
            "publisherDisplayName": "Prem Parihar"
        }
    }
    ''' %(package1,package2)



    fp = open(packageFile,'w')
    fp.write(data1)
    fp.close


    data2 = '''"use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    // The module 'vscode' contains the VS Code extensibility API
    // Import the module and reference it with the alias vscode in your code below
    const vscode = require("vscode");
    // this method is called when your extension is activated
    // your extension is activated the very first time the command is executed

    function pasteData(myData){
        let editor = vscode.window.activeTextEditor, 
        document = editor.document, 
        selections = editor.selections;        

        editor.edit(function (editBuilder) {
            selections.forEach(function (selection) {
                if (!selection.isSingleLine) {
                    return;
                }
                let range = new vscode.Range(selection.start, selection.end);
                editBuilder.replace( selection,  myData  );
            });
        });    
    }

    function activate(context) {
        // Use the console to output diagnostic information (console.log) and errors (console.error)
        // This line of code will only be executed once when your extension is activated
        // console.log("Congratulations, your extension "helloworld" is now active!");
        // The command has been defined in the package.json file
        // Now provide the implementation of the command with  registerCommand
        // The commandId parameter must match the command field in package.json
        let disposable = vscode.commands.registerCommand("extension.sayHello", () => {
            // The code you place here will be executed every time your command is executed
            // Display a message box to the user
            vscode.window.showInformationMessage("Hello World!");
        });

        %s

        context.subscriptions.push(disposable);
    }
    exports.activate = activate;
    // this method is called when your extension is deactivated
    function deactivate() {
    }
    exports.deactivate = deactivate;
    //# sourceMappingURL=extension.js.map
    ''' %(extension)

    fp = open(extensionFile,'w')
    fp.write(data2)
    fp.close
    #### END 建立檔案 ##############################################




import os, sys,re


for mainCodefile in os.listdir( "./" ):
    if re.match("mainCode_",mainCodefile):
        getData(mainCodefile)

saveFile()


### make-default #################################################################################################################################



