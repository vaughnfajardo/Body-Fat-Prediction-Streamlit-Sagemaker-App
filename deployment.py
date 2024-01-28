import streamlit as st
import pandas as pd
import boto3
import json

# Function to send data to AWS endpoint and get prediction
def get_prediction(data):
    client = boto3.client('sagemaker-runtime', region_name='######')
    formatted_data = [list(data.values())]
    response = client.invoke_endpoint(
        EndpointName='######',
        ContentType='application/json',
        Body=json.dumps(formatted_data)
    )
    result = json.loads(response['Body'].read().decode())
    return result

# Streamlit app layout
st.title('Body Fat Prediction')

# Creating input fields for each measurement
wrist = st.number_input('Wrist', min_value=0.0)
age = st.number_input('Age', min_value=0)
weight = st.number_input('Weight', min_value=0.0)
height = st.number_input('Height', min_value=0.0)
neck = st.number_input('Neck', min_value=0.0)
chest = st.number_input('Chest', min_value=0.0)
abdomen = st.number_input('Abdomen', min_value=0.0)
hip = st.number_input('Hip', min_value=0.0)
thigh = st.number_input('Thigh', min_value=0.0)
knee = st.number_input('Knee', min_value=0.0)
ankle = st.number_input('Ankle', min_value=0.0)
biceps = st.number_input('Biceps', min_value=0.0)
forearm = st.number_input('Forearm', min_value=0.0)

if st.button('Predict Body Fat'):
    # Prepare data in the format expected by your AWS model
    data = {
        "Wrist": wrist,
        "Age": age,
        "Weight": weight,
        "Height": height,
        "Neck": neck,
        "Chest": chest,
        "Abdomen": abdomen,
        "Hip": hip,
        "Thigh": thigh,
        "Knee": knee,
        "Ankle": ankle,
        "Biceps": biceps,
        "Forearm": forearm
    }

    # Get prediction
    prediction = get_prediction(data)

    if isinstance(prediction, list) and len(prediction) > 0:
        predicted_value = prediction[0]
    else:
        predicted_value = prediction  # or handle unexpected format

    st.write(f'Predicted Body Fat: {predicted_value:.2f}%')
