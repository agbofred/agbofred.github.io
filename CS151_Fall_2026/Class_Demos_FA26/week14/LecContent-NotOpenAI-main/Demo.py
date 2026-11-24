from notopenai import NotOpenAI
import json

CLIENT = NotOpenAI(api_key="bU1AoiUR2KPqKiV9BE1d")
chat_completion = CLIENT.chat.completions.create(
    messages= [
        {
            "role": "user",
            "content": "What is the capital of all countries in Europe? Reply in json where keys are countries"
        }
    ],
    model= "gpt-4o-mini",
    response_format={"type": "json_object"}
)

response_str= chat_completion.choices[0].message.content

print(response_str)
new_data = json.loads(response_str)
print(new_data)