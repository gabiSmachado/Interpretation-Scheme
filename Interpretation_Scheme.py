from openai import OpenAI

client = OpenAI(api_key="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")

intent = input("")

response = client.chat.completions.create(
    model="ft:gpt-4o-mini-2024-07-18:gabriela:orion-teste:BVWo6sKm",
    messages=[
        {"role": "user", "content": intent}
    ]
)

text = response.choices[0].message.content
new_text = text.replace(") ", ")\n").replace("}: ", "}:\n")
print(new_text)

import random
num = random.randint(1, 10)
test = new_text.replace("{ID}", str(num))
print(test)