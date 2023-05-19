from flask import render_template
from app import app

from internal import profile

@app.route('/')
def index():

    context = profile.get_profile()

    return render_template('index.html', **context)