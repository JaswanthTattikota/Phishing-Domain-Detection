import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel

import logging

# Create a logger
logger = logging.getLogger(__name__)

# Configure the logger
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a file handler and set the formatter
file_handler = logging.FileHandler('feature_extract.log')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# Load the dataset
dataset = pd.read_csv("dataset_full.csv")

# Check for missing values
print(dataset.isna())

# Split the dataset into features (X) and target variable (y)
X = dataset.drop("phishing", axis=1)
y = dataset["phishing"]

# Initialize the Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X, y)

logger.info("Identifying useful features")

# Feature Importance
feature_importances = clf.feature_importances_
feature_importances_df = pd.DataFrame({'Feature': X.columns, 'Importance': feature_importances})
feature_importances_df = feature_importances_df.sort_values(by='Importance', ascending=False)
selected_features = feature_importances_df['Feature'].head(20)

logger.info("Feature identification completed")

print("Top 20 features in descending order of importance:")
for feature in selected_features:
    print(feature)

# Plotting Feature Importance using Matplotlib
plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=feature_importances_df.head(20))
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.title('Top 20 Features: Importance')
plt.show()

