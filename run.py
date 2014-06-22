from flask import Flask, render_template
from database import db_session

app = Flask(__name__)

app.config.from_object('config.default')
app.config.from_envvar('YOURAPP_SETTINGS')

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/explore")
def explore():
    return render_template("explore.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run()