import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def get_response(input_prompt,short_term_memory):
    message = [
            {"role": "system", "content": "You are a helpful assistant."},
        ]
    
    for i in short_term_memory:
        message.append({"role": "user", "content":i['user']})
        message.append({"role": "assistant", "content":i['AI']})
    
    message.append({"role": "user", "content": input_prompt})
    res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=message
    )
    return res['choices'][0]['message']['content']

