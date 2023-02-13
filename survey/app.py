from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey


app = Flask(__name__)
app.debug = True

app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

responses_key = "responses"

#  When the user goes to the root route, render a page that shows the user the title of the survey, 
#  the instructions, and a button to start the survey. 
# The button should serve as a link that directs 
# the user to /questions/0 (the next step will define that route).

@app.route('/')
def start_page():
    """Home page to start/select a survey"""
    return render_template("start.html", survey=survey)

@app.route("/start", methods=["POST"])
def begin():
    """Begin the survey, clear responses"""
    session[responses_key] = []
    return redirect("questions/0")


@app.route("/questions/<int:qid>")
def questioning(qid):
    """Start asking questions from the survey"""
    responses = session.get(responses_key)

    if (responses is None):
        #handle questions asked too soon
        return redirect("/")
    
    if (len(responses) != qid):
        #handle a question accessed out of order
        flash(f"Invalid question id: {qid}")
        return redirect(f"/questions/{len(responses)}")
    
    question = survey.questions[qid]
    return render_template(
        "questions.html", question_num=qid, question=question)

@app.route("/answer", methods=["POST"])
def handle_question():
    """Save response and redirect to next question."""
    choice = request.form['answer']
    text = request.form.get("text", "")

    # # get the response choice
    # choice = request.form['answer']

    # add this response to the list in the session
    responses = session[responses_key]
    responses.append({"choice": choice, "text":text})

    # add this response to the session
    session[responses_key] = responses
    

    if (len(responses) == len(survey.questions)):
        # They've answered all the questions! Thank them.
        return redirect("/complete")

    else:
        return redirect(f"/questions/{len(responses)}")

@app.route("/complete")
def complete():
    """Survey complete. Show completion page."""
    
    responses = session[responses_key]

    return render_template("complete.html", survey=survey, responses=responses)





