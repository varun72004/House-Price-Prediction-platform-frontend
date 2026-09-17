import streamlit as st
import requests
import os
from dotenv import load_dotenv

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="House Price AI",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# ENVIRONMENT
# ============================================================
load_dotenv()

API_URL = os.getenv(
    "API_URL",
    "https://cloud-basedai-platform-backend.onrender.com"
)

# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:

    st.title("🏠 House Price AI")
    st.caption("Machine Learning Prediction Platform")

    st.divider()

    st.subheader("About")

    st.write(
        "Estimate the median house value using property and "
        "neighbourhood-level information."
    )

    st.divider()

    st.subheader("🔗 System")

    st.success("Prediction API ready")

    st.caption(
        "Your inputs are sent to the connected machine-learning "
        "backend for prediction."
    )

    st.divider()

    st.subheader("🧠 Model Inputs")

    st.caption("The model uses 7 features:")

    st.write(
        """
        1. Housing Median Age
        2. Total Rooms
        3. Total Bedrooms
        4. Population
        5. Households
        6. Median Income
        7. Ocean Proximity
        """
    )

    st.divider()

    st.caption(
        "Streamlit • FastAPI • Machine Learning"
    )


# ============================================================
# MAIN HEADER
# ============================================================
st.title("🏠 House Price Prediction")

st.write(
    "Enter the area and housing details below to get an "
    "AI-based estimate of the median house value."
)

st.divider()


# ============================================================
# QUICK OVERVIEW
# ============================================================
c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "📥 Inputs",
        "7 Features"
    )

with c2:
    st.metric(
        "⚙️ Engine",
        "ML Model"
    )

with c3:
    st.metric(
        "📤 Output",
        "House Value"
    )

st.write("")


# ============================================================
# INPUT SECTION
# ============================================================
st.subheader("Property & Area Details")

st.caption(
    "Each field includes a short explanation so you know exactly "
    "what information to enter."
)

with st.container(border=True):

    # ========================================================
    # FIRST ROW
    # ========================================================
    col1, col2 = st.columns(2)

    with col1:

        st.markdown("**Housing Median Age**")

        housing_median_age = st.number_input(
            "Housing Median Age",
            min_value=1,
            max_value=52,
            value=25,
            step=1,
            label_visibility="collapsed",
            help="Median age of houses in the area, measured in years."
        )

        st.caption(
            "Typical age of homes in the area, measured in years."
        )

    with col2:

        st.markdown("**Population**")

        population = st.number_input(
            "Population",
            min_value=3,
            max_value=35682,
            value=1166,
            step=1,
            label_visibility="collapsed",
            help="Number of people living in the area."
        )

        st.caption(
            "Number of people living in the area."
        )

    # ========================================================
    # SECOND ROW
    # ========================================================
    col1, col2 = st.columns(2)

    with col1:

        st.markdown("**Total Rooms**")

        total_rooms = st.number_input(
            "Total Rooms",
            min_value=2,
            max_value=39320,
            value=2127,
            step=1,
            label_visibility="collapsed",
            help="Total rooms across the housing units represented by the area."
        )

        st.caption(
            "Total rooms across the housing units in the area."
        )

    with col2:

        st.markdown("**Households**")

        households = st.number_input(
            "Households",
            min_value=1,
            max_value=6082,
            value=409,
            step=1,
            label_visibility="collapsed",
            help="Number of separate households in the area."
        )

        st.caption(
            "Number of separate households living in the area."
        )

    # ========================================================
    # THIRD ROW
    # ========================================================
    col1, col2 = st.columns(2)

    with col1:

        st.markdown("**Total Bedrooms**")

        total_bedrooms = st.number_input(
            "Total Bedrooms",
            min_value=1,
            max_value=6445,
            value=438,
            step=1,
            label_visibility="collapsed",
            help="Total bedrooms across the housing units represented by the area."
        )

        st.caption(
            "Total bedrooms across the housing units in the area."
        )

    with col2:

        st.markdown("**Median Income**")

        median_income = st.number_input(
            "Median Income",
            min_value=0.5,
            max_value=15.0,
            value=3.5,
            step=0.1,
            format="%.2f",
            label_visibility="collapsed",
            help="Median household income represented in units of $10,000."
        )

        st.caption(
            "Income is represented in $10,000 units. "
            "For example, 3.5 ≈ $35,000."
        )

    # ========================================================
    # LOCATION
    # ========================================================
    st.markdown("**Ocean Proximity**")

    ocean_proximity = st.selectbox(
        "Ocean Proximity",
        [
            "<1H OCEAN",
            "INLAND",
            "ISLAND",
            "NEAR BAY",
            "NEAR OCEAN",
        ],
        label_visibility="collapsed",
        help="Geographical relationship of the area to the ocean."
    )

    ocean_descriptions = {
        "<1H OCEAN": "The area is classified as less than one hour from the ocean.",
        "INLAND": "The area is classified as inland.",
        "ISLAND": "The area is classified as an island.",
        "NEAR BAY": "The area is classified as being near a bay.",
        "NEAR OCEAN": "The area is classified as being near the ocean.",
    }

    st.caption(
        ocean_descriptions[ocean_proximity]
    )


# ============================================================
# VALIDATION
# ============================================================
validation_error = None

if total_bedrooms > total_rooms:

    validation_error = (
        "Total bedrooms cannot be greater than total rooms."
    )

elif households > population:

    validation_error = (
        "Households cannot be greater than population."
    )


# ============================================================
# LIVE PROPERTY SNAPSHOT
# ============================================================
st.write("")

st.subheader("Live Property Snapshot")

st.caption(
    "These values update automatically as you change the inputs."
)

snapshot1, snapshot2, snapshot3, snapshot4 = st.columns(4)

# Derived values
rooms_per_bedroom = (
    total_rooms / total_bedrooms
    if total_bedrooms > 0
    else 0
)

people_per_household = (
    population / households
    if households > 0
    else 0
)

income_dollars = median_income * 10000

bedroom_ratio = (
    total_bedrooms / total_rooms * 100
    if total_rooms > 0
    else 0
)

with snapshot1:

    st.metric(
        "🏠 Rooms",
        f"{total_rooms:,}"
    )

with snapshot2:

    st.metric(
        "🛏️ Bedrooms",
        f"{total_bedrooms:,}"
    )

with snapshot3:

    st.metric(
        "👥 People / Household",
        f"{people_per_household:.1f}"
    )

with snapshot4:

    st.metric(
        "💰 Median Income",
        f"${income_dollars:,.0f}"
    )


# ============================================================
# SIMPLE DATA QUALITY CHECK
# ============================================================
st.write("")

if validation_error:

    st.error(
        f"⚠️ {validation_error}"
    )

else:

    if bedroom_ratio > 45:

        st.warning(
            "Check the room and bedroom values. "
            "Bedrooms make up a relatively large share of total rooms."
        )

    elif people_per_household > 10:

        st.warning(
            "The population-to-household ratio is unusually high. "
            "Please verify the entered values."
        )

    else:

        st.success(
            "✓ Inputs look consistent and are ready for prediction."
        )


# ============================================================
# PREDICT BUTTON
# ============================================================
st.write("")

predict_button = st.button(
    "🚀 Predict House Price",
    type="primary",
    use_container_width=True,
    disabled=validation_error is not None,
)


# ============================================================
# PREDICTION
# ============================================================
if predict_button:

    # ========================================================
    # SAME PAYLOAD AS ORIGINAL PROJECT
    # ========================================================
    payload = {
        "housing_median_age": housing_median_age,
        "total_rooms": total_rooms,
        "total_bedrooms": total_bedrooms,
        "population": population,
        "households": households,
        "median_income": median_income,
        "ocean_proximity": ocean_proximity,
    }

    with st.spinner("🤖 Generating house price prediction..."):

        try:

            # =================================================
            # EXISTING BACKEND CONNECTION
            # =================================================

            response = requests.post(
                f"{API_URL}/predict",
                json=payload,
                timeout=30
            )

            response.raise_for_status()

            prediction = response.json()["predicted_price"]

            # =================================================
            # RESULT
            # =================================================

            st.divider()

            st.subheader("🎯 Prediction Result")

            result_col1, result_col2 = st.columns(
                [2, 1]
            )

            with result_col1:

                st.metric(
                    "Estimated Median House Value",
                    f"${prediction:,.2f}"
                )

            with result_col2:

                st.metric(
                    "Location",
                    ocean_proximity
                )

            st.success(
                "Prediction generated successfully."
            )

            # =================================================
            # SUBMITTED VALUES
            # =================================================

            with st.expander(
                "View submitted property details"
            ):

                r1, r2 = st.columns(2)

                with r1:

                    st.write(
                        f"**Housing Median Age:** "
                        f"{housing_median_age} years"
                    )

                    st.write(
                        f"**Total Rooms:** "
                        f"{total_rooms:,}"
                    )

                    st.write(
                        f"**Total Bedrooms:** "
                        f"{total_bedrooms:,}"
                    )

                    st.write(
                        f"**Population:** "
                        f"{population:,}"
                    )

                with r2:

                    st.write(
                        f"**Households:** "
                        f"{households:,}"
                    )

                    st.write(
                        f"**Median Income:** "
                        f"${income_dollars:,.0f}"
                    )

                    st.write(
                        f"**Ocean Proximity:** "
                        f"{ocean_proximity}"
                    )

        # =====================================================
        # ERROR HANDLING
        # =====================================================

        except requests.exceptions.HTTPError:

            st.error(
                f"Backend Error:\n{response.text}"
            )

        except requests.exceptions.ConnectionError:

            st.error(
                "Could not connect to the backend API."
            )

        except requests.exceptions.Timeout:

            st.error(
                "The backend request timed out."
            )

        except KeyError:

            st.error(
                "The backend response did not contain "
                "`predicted_price`."
            )

        except Exception as e:

            st.error(
                f"Unexpected error: {e}"
            )


# ============================================================
# FOOTER
# ============================================================
st.divider()

st.caption(
    "🏠 House Price AI • Machine Learning Prediction Dashboard"
)