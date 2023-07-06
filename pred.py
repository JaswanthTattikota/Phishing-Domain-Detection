from url_extra import url_to_columns
import pickle

import logging

# Create a logger
logger = logging.getLogger(__name__)

# Configure the logger
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a file handler and set the formatter
file_handler = logging.FileHandler('pred.log')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

with open("rfc.pkl", "rb") as f:
    rf = pickle.load(f)

def classify_url(url):
    """Classifies a URL as safe or malicious using a machine learning model."""
    logger.info(f"Predicting the safety of URL: {url}")
    df = url_to_columns(url)
    pred = rf.predict(df)
    return pred

if __name__ == "__main__":
    url = input("Enter a URL: ")
    pred = classify_url(url)
    if pred == 0:
        print("Safe")
    else:
        print("Malicious")
    logger.info("URL prediction completed")