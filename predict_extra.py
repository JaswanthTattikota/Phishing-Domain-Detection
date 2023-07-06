import pandas as pd
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from url_extra import url_to_columns
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pickle

import logging

# Create a logger
logger = logging.getLogger(__name__)

# Configure the logger
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a file handler and set the formatter
file_handler = logging.FileHandler('predict_extra.log')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

data = pd.read_csv('dataset_full.csv')
X = data[["qty_slash_url","length_url","domain_length","qty_dot_directory","qty_hyphen_directory","qty_underline_directory","qty_slash_directory","qty_questionmark_directory","qty_equal_directory","qty_and_directory","qty_exclamation_directory","qty_plus_directory","qty_hashtag_directory","qty_percent_directory","directory_length","qty_dot_file","qty_underline_file","qty_space_file","qty_tilde_file","qty_percent_file","time_response","asn_ip","time_domain_activation","time_domain_expiration","ttl_hostname"]]
y = data['phishing']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

def RF():
    logger.info("Training the ML model")
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    return rf

rf = RF()
y_train_rf = rf.predict(X_train)
y_test_rf = rf.predict(X_test)

logger.info("Model training completed")

acc_train_rf = metrics.accuracy_score(y_train, y_train_rf)
acc_test_rf = metrics.accuracy_score(y_test, y_test_rf)

print("Random Forest Classifier: Accuracy on training Data: {:.3f}".format(acc_train_rf))
print("Random Forest Classifier: Accuracy on test Data: {:.3f}".format(acc_test_rf))
print()

f1_score_train_rf = metrics.f1_score(y_train, y_train_rf)
f1_score_test_rf = metrics.f1_score(y_test, y_test_rf)
print("Random Forest Classifier: F1 Score on training Data: {:.3f}".format(f1_score_train_rf))
print("Random Forest Classifier: F1 Score on test Data: {:.3f}".format(f1_score_test_rf))
print()

precision_score_train_rf = metrics.precision_score(y_train, y_train_rf)
precision_score_test_rf = metrics.precision_score(y_test, y_test_rf)
print("Random Forest Classifier: Precision on training Data: {:.3f}".format(precision_score_train_rf))
print("Random Forest Classifier: Precision on test Data: {:.3f}".format(f1_score_test_rf))
print()

with open("rfc.pkl","wb") as f:
    pickle.dump(rf,f)

gbc = GradientBoostingClassifier(max_depth=5,learning_rate=0.7)
gbc.fit(X_train,y_train)

y_train_gbc = gbc.predict(X_train)
y_test_gbc = gbc.predict(X_test)

acc_train_gbc = metrics.accuracy_score(y_train,y_train_gbc)
acc_test_gbc = metrics.accuracy_score(y_test,y_test_gbc)
print("Gradient Boosting Classifier : Accuracy on training Data: {:.3f}".format(acc_train_gbc))
print("Gradient Boosting Classifier : Accuracy on test Data: {:.3f}".format(acc_test_gbc))
print()

f1_score_train_gbc = metrics.f1_score(y_train,y_train_gbc)
f1_score_test_gbc = metrics.f1_score(y_test,y_test_gbc)
print("Gradient Boosting Classifier : F1 Score on training Data: {:.3f}".format(f1_score_train_gbc))
print("Gradient Boosting Classifier : F1 Score on test Data: {:.3f}".format(f1_score_test_gbc))
print()

precision_score_train_gbc = metrics.precision_score(y_train,y_train_gbc)
precision_score_test_gbc = metrics.precision_score(y_test,y_test_gbc)
print("Gradient Boosting Classifier : Precision on training Data: {:.3f}".format(precision_score_train_gbc))
print("Gradient Boosting Classifier : Precision on test Data: {:.3f}".format(f1_score_test_gbc))
print()