from stories import story
from flask import Flask, render_template, request
# from flask_debugtoolbar import DebugToolbarExtension
app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret'


@app.route('/')
def index():
    prompts = story.prompts
    return render_template('index.html', prompts=prompts)


@app.route('/story')
def generate_story():
    text = story.generate(request.args)

    return render_template('story.html', text=text)
