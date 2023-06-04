from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

debug = DebugToolbarExtension(app)

@app.route("/home")
def add_story():
   
    arguments = story.prompts
    return render_template("home.html", arguments = arguments)

@app.route("/story")
def display_story():
    
    user_story = story.generate(request.args)
    return render_template("story.html", user_story = user_story)