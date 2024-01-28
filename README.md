# Body Fat Prediction Streamlit App

This is a beginner machine learning application designed to predict body fat percentage based on various body measurements. It uses a RandomForestRegressor model hosted on AWS SageMaker and is interactively accessible through a Streamlit web app. Users input their body measurements, and the app provides an estimation of their body fat percentage. 

![Alt Text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzVyOGhnNnpxZWZpa2dlNHhuN2gzNDhpMDk4cGQ1MGR0YTBrbGJsYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/lKSyGfpujc2Qv6hXcq/giphy.gif)

## Usage
### Running the Streamlit App
```streamlit run deployment.py```
### Access the Web App
Open your browser and navigate to http://localhost:8501.

Input the required body measurements and click on 'Predict Body Fat'.

## Installation
### Prerequisites
- Python 3.6 or later
- AWS CLI (optional, for AWS setup)
- Boto3
- Streamlit

## Acknowledgments
Dataset Source: https://www.kaggle.com/datasets/fedesoriano/body-fat-prediction-dataset/data
