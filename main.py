from flask import Flask, render_template, request
from pred import classify_url

import logging

# Create a logger
logger = logging.getLogger(__name__)

# Configure the logger
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a file handler and set the formatter
file_handler = logging.FileHandler('main.log')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pred', methods=['GET','POST'])
def predict():
    url = request.form['url']
    pred = classify_url(url)
    if pred == 0:
        result = "Safe"
    else:
        result = "Malicious"
    return render_template('result.html', url=url, result=result)

if __name__ == '__main__':
    logger.info("Starting the Flask app")
    app.run(debug=True)
    logger.info("Flask app started")
