import openai

class GPTAgent():
    def __init__(self):
        with open('openai_api.key') as f:
            api_key = f.read()
        self.client = openai.OpenAI(api_key=api_key)

    def prompt(self, message, model='gpt-3.5-turbo', max_tokens=1024, system='You are a helpful and harmless assistant.'):
        response = self.client.chat.completions.create(model=model, max_tokens=max_tokens, messages=[{"role": "system", "content": system}, {"role": "user", "content": message}])
        answer = response.choices[0].message.content
        return answer