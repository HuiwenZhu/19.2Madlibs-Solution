from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)


@app.route('/')
def index():
    """fill in forms."""
    prompts = story.prompts
    return render_template("form.html", prompts=prompts)


@app.route('/story')
def tell_stories():
    """tell a story with input"""
    text=story.generate(request.args)
    return render_template("tell_story.html",story_text=text)

