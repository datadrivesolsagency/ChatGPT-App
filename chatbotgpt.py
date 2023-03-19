API_KEY = "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"

import openai
import os

os.environ['OPENAI_key']  = API_KEY

openai.api_key = os.environ['OPENAI_key']


# def getting_reponse():
#     keep_prompting = True

#     while keep_prompting:
#         prompt = input("How can I help you?Type exit to quit: ")
#         if prompt == "exit":
#             keep_prompting = False

#         else:
#             response = openai.Completion.create(engine="davinci-instruct-beta-v3", prompt=prompt,max_tokens=40-)
#             resp_text = response['choices'][0]['text']
#             return resp_text
        
def response_function(msg):
    query = msg
    response = openai.Completion.create(engine="text-davinci-003", prompt=msg,max_tokens=4000)
    resp_text = response['choices'][0]['text']
    return resp_text


