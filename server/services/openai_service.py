from dotenv import load_dotenv
load_dotenv()

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_lesson(topic: str) -> dict:
    with open("server/prompts/lesson_prompt.txt", "r") as f:
        prompt_template = f.read()

    prompt = prompt_template.format(topic=topic)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for creating educational content."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    content = response.choices[0].message.content
    return {"lesson": content}