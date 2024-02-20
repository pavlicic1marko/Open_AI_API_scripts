import openai
import json
with open('config.json') as config_file:
    config = json.load(config_file)
    api_key = config['API_KEY']

openai.api_key = api_key

model_id = "gpt-3.5-turbo"
# Initial message to ask the first question
messages = [ {"role": "user", "content": "Where was the last olympics held? Just tell me the year & country?"} ]

# Call the API
completion = openai.chat.completions.create(model=model_id,
messages=messages)

# Print the answer we received for the 1st question
print(completion.choices[0].message.content)



