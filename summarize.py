from gpt import GPTAgent

class SummarizeAgent():
    def __init__(self):
        self.gpt_agent = GPTAgent()
        self.folders = ['EDUCATION', 'START-UP', 'RESEARCH']
        self.system_prompt_summary = "You are an AI assistant skilled at summarizing the key information from web pages into concise bullet points. When given some web page content, your task is to analyze the page and identify the most essential and relevant details. Present this information in a clear, organized list of bullet points with no title, omitting any unnecessary fluff or tangential details. Return immediately at most five bullet points with no introductory sentence and no title, in a structured format that is easy to read and understand."
        self.system_prompt_title = "You are an AI assistant tasked with providing a clear, concise title that summarizes the main topic of given text content. Read the content, analyze it and output only the title, without any additional text or explanations."
        self.system_prompt_folder =  \
            f"""
            You are a helpful AI assistant that can classify text content into different categories based on the following provided list of folder names: {', '.join(self.folders)}

            Your task is as follows:

            1. The user will provide you with some text content to analyze.
            2. You will read and understand the provided content.
            3. Based on your analysis, you will classify the content into one of the categories represented by the folder names in the `folders` list.
            4. You will output the name of the folder (category) that best represents the content.

            Please remember to be concise and provide only the folder name as your output, without any additional explanations or comments.
            """
        self.system_prompt_summary = "You are an AI assistant skilled at summarizing the key information from web pages into concise bullet points. When given some web page content, your task is to analyze the page and identify the most essential and relevant details. Present this information in a clear, organized list of bullet points preceded by a title, omitting any unnecessary fluff or tangential details. Return the title followed by at most five bullet points immediately in a structured format that is easy to read and understand, with no introductory sentence."
        self.model = 'gpt-3.5-turbo'

    def create_title(self, text_page):
        print('Creating title...')
        title = self.gpt_agent.prompt(text_page, model=self.model, system=self.system_prompt_title)
        return title

    def summarize(self, text_page):
        print('Summarizing...')
        summary = self.gpt_agent.prompt(text_page, model=self.model, system=self.system_prompt_summary)
        return summary

    def detect_folder(self, summary):
        print('Detecting folder...')
        folder = self.gpt_agent.prompt(summary, model=self.model, system=self.system_prompt_folder)
        if folder not in self.folders: folder = self.folders[0]
        return folder

    def process(self, text_page):
        title = self.create_title(text_page)
        summary = self.summarize(text_page)
        folder = self.detect_folder(summary)
        return {'title': title, 'summary': summary, 'folder': folder}