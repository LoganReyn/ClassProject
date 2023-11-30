import requests
import helpers
from bs4 import BeautifulSoup
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__, static_folder='static')

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        if not request.form.get("article_url"):
            return "You must enter a valid URL"
        else:
            url = request.form.get("article_url")

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        tags = ['div', 'p']
        articleText = helpers.getSoup(url)

        return redirect(url_for('summary', articleText=articleText))
    
    elif request.method == 'GET':
        return render_template('index.html')
    
@app.route('/summary/<articleText>')
def summary(articleText):

    chatPrompt = f'''Goal:

    Assign a content rating to the provided article using the following scale:

    E: Suitable for Everyone
    T: Appropriate for Teens
    M: Intended for a Mature audience
    Summarize the key points of the article in no more than two paragraphs.

    Example Output Format:

    Maturity Rating: [Insert E, T, or M based on content assessment]
    Article Summary: [Provide a concise and informative summary, covering the main points of the article in up to two paragraphs.]
    Article for Reference:
    <<{articleText}>>'''
    summary = helpers.llm_response(chatPrompt)

    return render_template('summary.html', summary=summary)