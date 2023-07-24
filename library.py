import openai
import os
#import panel as pn
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# OpenAI global config
openai.api_key  = os.getenv('OPENAI_API_KEY')
openai.api_type = "azure"
openai.api_base = "https://openai-experiment.openai.azure.com/"
openai.api_version = "2023-03-15-preview"


def get_completion(prompt, engine="gpt-3.5-turbo", temperature=0):
    messages = [{"role":"system","content":"You are an AI assistant that helps people find information."},
                {"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        engine="johan-dahl-test",
        messages=messages,
        temperature=0.1, # this is the degree of randomness of the model's output
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    return response.choices[0].message["content"]


def get_completion_from_messages(messages, engine="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        engine="johan-dahl-test",
        messages=messages,
        temperature=0.1, # this is the degree of randomness of the model's output
        max_tokens=5000,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    return response.choices[0].message["content"]


def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))
 
    return pn.Column(*panels)