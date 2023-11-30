import requests
import openai
from openai import OpenAI
import os
from os.path import join, dirname
from dotenv import load_dotenv
from bs4 import BeautifulSoup

api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def getSoup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    summary = ''

    for tag in soup.findAll('p'):
        for child in tag.contents:
            if child.name is None:
                summary = summary + child.strip()

    return summary

def llm_response(prompt):
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="gpt-4",
    )
    return response.choices[0].message.content
