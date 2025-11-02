from google import genai

def chat_wit_llm(prompt):
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )

    return response.text


