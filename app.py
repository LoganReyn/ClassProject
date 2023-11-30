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
        summary = ''

        for tag in soup.findAll('p'):
            print(tag)
            if tag.name not in tags:
                tag.replaceWith(tag.renderContents())
            else:
                summary = summary + tag.getText()

        return redirect(url_for('summary', summary=summary, title='title'))
    
    elif request.method == 'GET':
        return render_template('index.html')
    
@app.route('/summary/<title>')
def summary(summary, title):
    return render_template('summary.html', summary=summary)