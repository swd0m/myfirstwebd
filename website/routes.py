from website import app
from flask import render_template, url_for

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/contacts")
def contact_page():
    return render_template('contact.html')
