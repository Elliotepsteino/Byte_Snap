# ByteSnap
Browser extension to remember what read your online, frictionlessly. 

## Usage
Using the ByteSnap extension, you can save the text of any article you read online to your Notion workspace. The extension will automatically summarize the article and save the summary and categorize it to your Notion workspace.

## Instructions for running locally
1. Clone the repository:
```
git clone https://github.com/Elliotepsteino/Byte_Snap.git
```
2. Launch a Flask App to run the summarization server locally: 

```
python app.py
```
3. Add openai api key to openai_api.key.

4. Add notion integration key to notion_integration_token.key
You can create a new integration key at https://www.notion.com/my-integrations.
5. Create notion pages for Education, Startup, and Research:
After these pages are created, give access to the integration key to these pages (important) and copy the page id (the last part of the url) to the respective variables in the notion.py file.

6. Acitvate the extension in your browser.
Go to your extension, click manage extensions, and load the unpacked extension from the byte_snap_extension directory.

