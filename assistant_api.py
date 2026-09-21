import requests

def ask_chef(question, key):

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openrouter/free",
            "messages": [
                {
                    "role": "system",
                    "content": """
You are a Smart Chef Assistant.

Only answer questions related to cooking, recipes,
ingredients, substitutions, dietary restrictions,
cooking techniques, and food preparation.

Give clear and concise answers.
Return plain text only.
"""
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        }
    )

    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]