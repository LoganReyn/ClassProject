import requests
import openai
from openai import OpenAI
import os
from bs4 import BeautifulSoup

os.environ['OPENAI_API_KEY'] = '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'
client = OpenAI(api_key='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')

def getSoup(url):
    response.requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    summary = ''

    for tag in soup.findAll('p'):
        for child in tag.contents:
            if child.name is None:
                summary = summary + child.strip()

    return summary

def llm_response(prompt):
    response = clint.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="gpt-4",
    )
    return response.choices[0].message.content
