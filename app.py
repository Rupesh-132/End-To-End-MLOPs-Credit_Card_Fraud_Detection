import os

import streamlit as st
import pandas as pd
from Credit_Card_Fraud_Detection.pipeline.prediction_pipeline import PredictionPipeline
import numpy as np


def main():

    st.title("CREDIT CARD FRAUD DETECTION")

    # Create text boxes for input features
    st.write("Enter values for the 30 columns:")

    input_data = []
    # Use the provided column names
    column_names = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
                    'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
                    'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount']

    for i, column in enumerate(column_names):
        input_value = st.number_input(column)
        input_data.append(input_value)

    data = np.array(input_data).reshape(1, 30)
    if st.button("Train"):
        os.system("python main.py")

    if st.button("Predict"):
        # Make predictions
        predict_fraud = PredictionPipeline()
        prediction =  predict_fraud.predict(data)
        print(prediction)
        st.write(f"Prediction: {'Fraud' if prediction[0] == 1 else 'Not Fraud'}")


if __name__ == "__main__":
    main()
