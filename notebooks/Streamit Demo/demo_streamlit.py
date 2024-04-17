#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
from joblib import load


# In[9]:


data_file_path = r'C:\Users\Élio Vieira\Desktop\IronHack\final_project\data\cleaned data\df_clicks_filtered_3_countries.csv'
#data_file_path = r'..\data\cleaned data\df_clicks_filtered_3_countries.csv'
df_clicks_filtered_3_countries = pd.read_csv(data_file_path)

data_file_path2 = r'C:\Users\Élio Vieira\Desktop\IronHack\final_project\data\data_for_model.csv'
df_encoded_3_countries = pd.read_csv(data_file_path2)


# In[10]:


loaded_model = load(r'C:\Users\Élio Vieira\Desktop\IronHack\final_project\notebooks\best_gb_regressor_model.pkl')

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

        st.write(f"Predicted cost_per_goal: {rounded_prediction}€")


if __name__ == '__main__':
    main()


# In[11]:




# In[ ]:




