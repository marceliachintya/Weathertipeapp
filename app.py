import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('weather_rf_model.pkl', 'rb'))

st.title('Weather Type Prediction')
with st.form(key='weather_form'):
    st.header('Input Weather Features')
    temperature = st.number_input('Temperature', min_value=-50.0, max_value=60.0, value=20.0)
    humidity = st.number_input('Humidity', min_value=0, max_value=100, value=50)
    wind_speed = st.number_input('Wind Speed', min_value=0.0, max_value=100.0, value=10.0)
    precipitation = st.number_input('Precipitation (%)', min_value=0, max_value=100, value=0)
    atmospheric_pressure = st.number_input('Atmospheric Pressure', min_value=900.0, max_value=1100.0, value=1013.0)
    uv_index = st.number_input('UV Index', min_value=0, max_value=11, value=0)
    visibility = st.number_input('Visibility (km)', min_value=0.0, max_value=100.0, value=10.0)
    season_spring = st.checkbox('Season_Spring')
    season_summer = st.checkbox('Season_Summer')
    season_winter = st.checkbox('Season_Winter')
    location_inland = st.checkbox('Location_inland')
    location_mountain = st.checkbox('Location_mountain')
    cloud_cover_cloudy = st.checkbox('Cloud Cover_cloudy')
    cloud_cover_overcast = st.checkbox('Cloud Cover_overcast')
    cloud_cover_partly_cloudy = st.checkbox('Cloud Cover_partly cloudy')

    submit_button = st.form_submit_button(label='Predict')

if submit_button:
    input_data = pd.DataFrame({
        'Temperature': [temperature],
        'Humidity': [humidity],
        'Wind Speed': [wind_speed],
        'Precipitation (%)': [precipitation],
        'Atmospheric Pressure': [atmospheric_pressure],
        'UV Index': [uv_index],
        'Visibility (km)': [visibility],
        'Season_Spring': [int(season_spring)],
        'Season_Summer': [int(season_summer)],
        'Season_Winter': [int(season_winter)],
        'Location_inland': [int(location_inland)],
        'Location_mountain': [int(location_mountain)],
        'Cloud Cover_cloudy': [int(cloud_cover_cloudy)],
        'Cloud Cover_overcast': [int(cloud_cover_overcast)],
        'Cloud Cover_partly cloudy': [int(cloud_cover_partly_cloudy)]
    })

    prediction = model.predict(input_data)
    
    st.write(f'Predicted Weather Type: {prediction[0]}')
