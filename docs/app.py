from flask import Flask, render_template_string, send_from_directory
from threading import Thread
import os

# Create a Flask application
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <title>Flask App</title>
            <link rel="icon" href="/favicon.ico">
          </head>
          <body>
            <h1>Welcome to Flask App!</h1>
          </body>
        </html>
    ''')

# Route to serve the favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

# Function to run the Flask app
def run_app():
    app.run(port=5000)

# Run the Flask app in a separate thread
thread = Thread(target=run_app)
thread.start()

print("Flask app is running on http://127.0.0.1:5000")

