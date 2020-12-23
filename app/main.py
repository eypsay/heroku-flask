from flask import Flask

app= Flask(__name__)

@app.route('/')
def index():
  return "<h1>eyp herouku ile flask isleri...</h1>"
