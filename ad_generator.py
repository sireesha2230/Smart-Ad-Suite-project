# ad_generator.py

import openai

def generate_ad_copy(product, tone="Professional", platform="Google", api_key=None):
    if not api_key:
        return "OpenAI API key is missing."

    client = openai.OpenAI(api_key=api_key)

    prompt = f"""
You are a professional ad copywriter.
Write a short, engaging, and {tone.lower()} ad for a {platform} ad campaign.
Product/Service: {product}
Length: 1-2 sentences.
Style: Text-only, catchy, and conversion-focused.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=80
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error generating ad copy: {e}"
