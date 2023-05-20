from flask import render_template, send_from_directory
from app import app

from internal import profile


@app.route('/')
def index():
    context = profile.get_profile()
    return render_template('index.html', **context)


@app.route('/download_pdf')
def download_pdf():
    return send_from_directory('static/', 'pdf/Mark van Heeswijk CV - Python Developer 2023.pdf', as_attachment=True)