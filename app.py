# app.py
from flask import Flask, render_template, request
from summarize import summarize_text

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def summarize():
    input_text = request.form['text']
    summary = summarize_text(input_text)
    return render_template('result.html', summary=summary, original=input_text)

if __name__ == '__main__':
    app.run(debug=True)
