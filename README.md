# Phishing-Domain-Detection
Used to detect phishing website URLs using ML algorithms.
The site is live here: http://15.207.88.119:8080/

I have made this project using python language. I have used scikit-learn's RandomForestClassifier to classify URLs as safe or malicious.
The features from the url are extracted and passed as a dataframe to the Random Forest Classifier which then classifies it as Safe or Malicious.

The dataset used here can be found here: https://data.mendeley.com/datasets/72ptz43s9v/1

The dataset has 111 features out of which the last feature tells whether the website is sae or malicious.To use the dataset for predicting whether 
the URL is safe or malicious, we need to select the best features which help in identifying whether the URL is safe or malicious. If we use all the 
features for predicting, the model will definitely overfit. So, we need to select the best features. So in this project, there is a program which 
selects the top 20 features and those top 20 features will be used for the model building. 

So, whenever a URL is given as input to the program, we need to extract the features from the URL so that the model can use those features for the 
prediction. In this project, there is a program which exactly does this thing i.e. extracting the features from the URL. Now, those features are 
passed as a dataframe to the ML model which then classifies it as "Safe" or "Malicious". 

