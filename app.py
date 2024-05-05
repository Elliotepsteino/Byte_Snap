from flask import Flask, request
from summarize import SummarizeAgent

app = Flask(__name__)

summarize_agent = SummarizeAgent()

@app.route('/', methods=['POST'])
def handle_post():
    data = request.get_json()
    text_page = data['text']
    print('*** Successfully received text_page ***')

    out = summarize_agent.process(text_page)
    print('*** Successfully launched agent ***')
    for key, value in out.items():
        print(f'{key}: {value}')
    # Process the POST request data
    return 'Success'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)