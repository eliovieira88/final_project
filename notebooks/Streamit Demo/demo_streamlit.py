#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd
from joblib import load
import os

# Get the directory where the script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define relative paths to data files and model
data_file_path = os.path.join(current_directory, "df_clicks_filtered_3_countries.csv")
data_file_path2 = os.path.join(current_directory, "data_for_model.csv")
model_file_path = os.path.join(current_directory, "best_gb_regressor_model.pkl")

# Load data and model
df_clicks_filtered_3_countries = pd.read_csv(data_file_path)
df_encoded_3_countries = pd.read_csv(data_file_path2)
loaded_model = load(model_file_path)

# Define options
vertical_options = df_clicks_filtered_3_countries['vertical'].unique()
country_options = df_clicks_filtered_3_countries['advertiser_country'].unique()
platform_options = df_clicks_filtered_3_countries['advertising_platform_id'].unique()

def main():
    st.title('Cost per Goal Prediction')
    st.write('Please enter the following information:')

    vertical = st.selectbox('Vertical', options=vertical_options)
    country = st.selectbox('Advertiser Country', options=country_options)
    platform = st.selectbox('Advertising Platform ID', options=platform_options)

    if st.button('Predict'):
        user_data_encoded = pd.DataFrame(columns=df_encoded_3_countries.columns)
        user_data_encoded.loc[0] = 0
        user_data_encoded['vertical_' + vertical] = 1
        user_data_encoded['advertiser_country_' + country] = 1
        user_data_encoded['advertising_platform_id_' + platform] = 1
        
        # Remove the 'cost_per_goal' column if present
        user_data_encoded = user_data_encoded.drop(columns=['cost_per_goal'], errors='ignore')

        prediction = loaded_model.predict(user_data_encoded)
        rounded_prediction = round(prediction[0], 2)  # Round to 2 decimal places

        st.write(f"Predicted cost_per_goal: {rounded_prediction}")


if __name__ == '__main__':
    main()




