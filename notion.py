from functools import partial
import requests

def create_notion_page(token, parent_page_id, title, content):
    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    data = {
        "parent": {"page_id": parent_page_id},
        "properties": {
            "title": {
                "title": [
                    {
                        "text": {
                            "content": title
                        }
                    }
                ]
            }
        },
        "children": [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": content
                            }
                        }
                    ]
                }
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

create_classes_page = partial(
    create_notion_page, 
    parent_page_id="c4d447fee57c416ab1975f836114128f"
)

create_research_page = partial(
    create_notion_page, 
    parent_page_id="9c22bc842d8d40d19f550f5a658d791d"
)

create_startup_page = partial(
    create_notion_page, 
    parent_page_id="19590499489040a8986921399dd52068"
)