const vscode = require('vscode');
const axios = require('axios');

function activate(context) {
    let disposable = vscode.commands.registerCommand('extension.getCodeSuggestion', async function () {
        const editor = vscode.window.activeTextEditor;
        if (!editor) return;

        const selection = editor.selection;
        const text = editor.document.getText(selection);

        try {
            const response = await axios.post('http://127.0.0.1:8000/generate_code/', { prompt: text });
            vscode.window.showInformationMessage("Suggested Code:\n" + response.data.generated_code);
        } catch (error) {
            vscode.window.showErrorMessage("API Error: " + error.message);
        }
    });

    context.subscriptions.push(disposable);
}

function deactivate() {}

module.exports = { activate, deactivate };
