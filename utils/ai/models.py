from openai import OpenAI
from env_config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_text_4o(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt},
        ],
    )

    return completion.choices[0].message.content

def generate_text_4o_mini(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt},
        ],
    )

    return completion.choices[0].message.content

def generate_image_url(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    return response.data[0].url
