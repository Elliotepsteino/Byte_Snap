from flask import Flask, request
from summarize import SummarizeAgent

app = Flask(__name__)

summarize_agent = SummarizeAgent()

@app.route('/', methods=['POST'])
def handle_post():
    data = request.get_json(force=True)
    print(data)
    text_page, url = data['text'], data['url']
    print('*** Successfully received text_page ***')

    out = summarize_agent.process(text_page)
    print('*** Successfully launched agent ***')
    title, summary, folder = out['title'], out['summary'], out['folder']
    return 'Success'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)