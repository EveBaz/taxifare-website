import streamlit as st
import datetime
import requests


'''
# TaxiFareModel By Eve
'''

if st.button('Welcome to my app 🎈🎈🎈 !'):
    st.balloons()



pickup_date = st.date_input(
    "Pick-up date",
    datetime.date(2025, 3, 7))

pickup_time = st.time_input(
    "Pick-up time",
    datetime.time(8,0,0))

pickup_longitude = st.number_input("Pickup Longitude", value=0.0, format="%.6f")
pickup_lattitude = st.number_input("Pickup Lattitude", value=0.0, format="%.6f")
dropoff_longitude = st.number_input("Dropoff Longitude", value=0.0, format="%.6f")
dropoff_lattitude = st.number_input("Dropoff Lattitude", value=0.0, format="%.6f")



# this slider allows the user to select a number of passengers
# the selected value is returned by st.slider
line_count = st.slider('Number of passengers (between 1 and 8):', 1, 8, 3)


pickup_datetime=f"{pickup_date}+{pickup_time}"

url = 'https://wagon-data-tpl-image-110241198688.europe-west1.run.app/predict'
querry =f"{url}?pickup_datetime={pickup_datetime}&\
pickup_longitude={pickup_longitude}&pickup_latitude={pickup_lattitude}&\
dropoff_longitude={dropoff_longitude}&dropoff_latitude={dropoff_lattitude}&\
passenger_count={line_count}" 


if st.button("Estimation of the fare :"):
    response = requests.get(querry)
    st.write("Fare estimation :")
    st.write(round(response.json()["fare"],2))

