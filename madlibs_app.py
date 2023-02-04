from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

@app.route("/")
def ask_questions():
    """Generate questions on html home page"""
    prompts = story.prompts
    return render_template("questions.html", prompts=prompts)

@app.route("/story")
def show_story():
    """Show a story from the asnwers to the questions"""
    text = story.generate(request.args)
    return render_template("story.html", text=text)

