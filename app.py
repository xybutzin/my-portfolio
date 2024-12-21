import os
from datetime import datetime
from flask import Flask, redirect, render_template, url_for, flash, request, abort
from flask_mail import Mail, Message
from dotenv import load_dotenv
from forms import ContactForm
import requests


load_dotenv() # Load environment variables from .env file

# Configure application
app = Flask(__name__)

app.config["SECRET_KEY"] = 'b01b04a1f0243c8d3090d23343327e64'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

posts = [
    {
        'id': 1,
        'title': 'Understanding Data Science',
        'date': datetime(2024, 12, 1),
        'content': 'Data science is an interdisciplinary field that uses scientific methods, processes, algorithms, and systmes to extract knowledge and insights from structured and unstructured data.'
    },
    {
        'id': 2,
        'title': 'Python for beginners',
        'date': datetime(2024, 12, 10),
        'content': 'Python is a versatile programming language that allows you to work on various applications from web development to machine learning.'
    }
]

# initialize a global counter variable
# visitor_count = 0

@app.route("/")
def index():
    # global visitor_count
    # visitor_count += 1
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        msg = Message("New Contact Message",
                      sender="xuan.butzin@gmail.com",
                      recipients=["xuan.butzin@gmail.com"])
        
        msg.body = f"From: {form.name.data} <{form.email.data}>\nSubject: {form.subject.data}\nMessage:{form.message.data}"

        # Send the email
        mail.send(msg)

        flash("Thank you! Message sent.", "success")
        return redirect(url_for('index'))
        
    return render_template("contact.html", form=form)

@app.route("/thank_you")
def thank_you():
    return render_template("thank_you.html")

if __name__ == "__main__":
    app.run(debug=os.getenv('FLASK_DEBUG', 'false') == 'true')