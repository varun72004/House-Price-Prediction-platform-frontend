import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv(
    "API_URL",
    "https://cloud-basedai-platform-backend.onrender.com"
)

st.title("🏠 House Price Prediction")

st.write("Enter the house details below.")

housing_median_age = st.number_input("Housing Median Age", value=25)

total_rooms = st.number_input("Total Rooms", value=5)

total_bedrooms = st.number_input("Total Bedrooms", value=5)

population = st.number_input("Population", value=1200)

households = st.number_input("Households", value=5)

median_income = st.number_input("Median Income", value=4.5)

ocean_proximity = st.selectbox(
    "Ocean Proximity",
    [
        "<1H OCEAN",
        "INLAND",
        "ISLAND",
        "NEAR BAY",
        "NEAR OCEAN"
    ]
)

if st.button("Predict House Price"):

    payload = {
        "housing_median_age": housing_median_age,
        "total_rooms": total_rooms,
        "total_bedrooms": total_bedrooms,
        "population": population,
        "households": households,
        "median_income": median_income,
        "ocean_proximity": ocean_proximity
    }

    try:

        response = requests.post(
            f"{API_URL}/predict",
            json=payload,
            timeout=30
        )

        response.raise_for_status()

        prediction = response.json()["predicted_price"]

        st.success(f"Estimated House Price : ${prediction:,.2f}")

    except requests.exceptions.HTTPError:
        st.error(f"Backend Error:\n{response.text}")

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the backend API.")

    except requests.exceptions.Timeout:
        st.error("The backend request timed out.")

    except Exception as e:
        st.error(f"Unexpected error: {e}")