import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os
import joblib

# Set page configuration
st.set_page_config(page_title="Mobile Price Prediction", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for styling
st.markdown("""
    <style>
    .main { background-color: #F5F5F5; padding: 20px; border-radius: 10px; }
    .stButton>button { background-color: #FF9800; color: white; border-radius: 5px; }
    .stButton>button:hover { background-color: #FB8C00; }
    .stNumberInput { background-color: white; border: 1px solid #4CAF50; border-radius: 5px; }
    .stSuccess { background-color: #E8F5E9; border: 1px solid #4CAF50; padding: 10px; border-radius: 5px; }
    .stMarkdown h1 { color: #4CAF50; }
    .stMarkdown h2 { color: #4CAF50; }
    .stExpander { background-color: white; border: 1px solid #E0E0E0; border-radius: 5px; }
    .footer { text-align: center; color: #666; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

# Ensure session state initialization
if not hasattr(st.session_state, 'new_data'):
    st.session_state.new_data = []

# Cache model and scaler loading
@st.cache_resource(show_spinner=False)
def load_model():
    try:
        return joblib.load('rf_model.pkl')
    except FileNotFoundError:
        st.error("Model file 'rf_model.pkl' not found. Please ensure it is in the same directory as app.py.")
        st.stop()

@st.cache_resource(show_spinner=False)
def load_scaler():
    try:
        with open('scaler.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        st.error("Scaler file 'scaler.pkl' not found. Please ensure it is in the same directory as app.py.")
        st.stop()

# Load model and scaler
model = load_model()
scaler = load_scaler()

# Streamlit UI
st.title("📱 Mobile Price Prediction")
st.markdown("Predict the price of a mobile phone based on its specifications. Enter details below to get started.", unsafe_allow_html=True)

# Placeholder for company logo
st.image("https://via.placeholder.com/150x50.png?text=Company+Logo", use_column_width=False)

# Form for input fields
with st.form(key="prediction_form"):
    # Currency conversion input
    st.subheader("💸 Currency Conversion")
    default_exchange_rate = 83.50
    exchange_rate = st.number_input("USD to INR Exchange Rate", min_value=1.0, value=default_exchange_rate, step=0.1, format="%.2f", help="Enter the current USD to INR exchange rate (default: 83.50)", key="exchange_rate")

    # Input features in expanders
    st.subheader("📋 Input Features")
    
    # Group features into categories
    with st.expander("Display Features", expanded=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            resolution = st.number_input("Resolution (inches)", min_value=1.4, max_value=12.2, value=5.2, step=0.1, format="%.1f", help="Screen size in inches (Range: 1.4 to 12.2)", key="resolution")
        with col2:
            ppi = st.number_input("PPI", min_value=121.0, max_value=806.0, value=335.0, step=1.0, format="%.0f", help="Pixels per inch (Range: 121 to 806)", key="ppi")
        with col3:
            sale = st.number_input("Units Sold", min_value=10, max_value=9807, value=621, step=1, format="%d", help="Number of units sold (Range: 10 to 9807)", key="Sale")

    with st.expander("Hardware Features", expanded=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            cpu_core = st.number_input("CPU Core", min_value=0, max_value=8, value=5, step=1, format="%d", help="Number of CPU cores (Range: 0 to 8)", key="cpu_core")
            cpu_freq = st.number_input("CPU Frequency (GHz)", min_value=0.0, max_value=2.7, value=1.5, step=0.1, format="%.1f", help="CPU speed in GHz (Range: 0 to 2.7)", key="cpu_freq")
        with col2:
            ram = st.number_input("RAM (GB)", min_value=0.0, max_value=6.0, value=2.2, step=0.1, format="%.1f", help="RAM in GB (Range: 0 to 6)", key="ram")
            battery = st.number_input("Battery (mAh)", min_value=800.0, max_value=9500.0, value=2842.0, step=1.0, format="%.0f", help="Battery capacity in mAh (Range: 800 to 9500)", key="battery")
        with col3:
            st.empty()

    with st.expander("Camera & Physical Features", expanded=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            rear_cam = st.number_input("Rear Camera (MP)", min_value=0.0, max_value=23.0, value=10.4, step=0.1, format="%.1f", help="Rear camera resolution in MP (Range: 0 to 23)", key="RearCam")
            front_cam = st.number_input("Front Camera (MP)", min_value=0.0, max_value=20.0, value=4.5, step=0.1, format="%.1f", help="Front camera resolution in MP (Range: 0 to 20)", key="Front_Cam")
        with col2:
            thickness = st.number_input("Thickness (mm)", min_value=1.1, max_value=18.5, value=8.9, step=0.1, format="%.1f", help="Thickness in mm (Range: 5.1 to 18.5)", key="thickness")
        with col3:
            st.empty()

    # Submit buttons
    col1, col2 = st.columns(2)
    with col1:
        predict = st.form_submit_button("Predict Price", use_container_width=True)
    with col2:
        save_data = st.form_submit_button("Save Input Data", use_container_width=True)

# Process form submission
if predict:
    input_data = [sale, resolution, ppi, cpu_core, cpu_freq, ram, rear_cam, front_cam, battery, thickness]
    input_array = np.array(input_data).reshape(1, -1)
    with st.spinner("Predicting..."):
        try:
            input_scaled = scaler.transform(input_array)
            prediction_usd = model.predict(input_scaled)[0]
            prediction_inr = prediction_usd * exchange_rate
            st.success(f"Predicted Price: ${prediction_usd:.2f} (₹{prediction_inr:.2f})")
        except Exception as e:
            st.error(f"Error during prediction: {e}")

if save_data:
    input_data = [sale, resolution, ppi, cpu_core, cpu_freq, ram, rear_cam, front_cam, battery, thickness]
    new_entry = dict(zip(['Sale', 'resolution', 'ppi', 'cpu core', 'cpu freq', 'ram', 'RearCam', 'Front_Cam', 'battery', 'thickness'], input_data))
    st.session_state.new_data.append(new_entry)
    new_data_df = pd.DataFrame([new_entry])
    try:
        new_data_df.to_csv('new_data.csv', mode='a' if os.path.exists('new_data.csv') else 'w', header=not os.path.exists('new_data.csv'), index=False)
        st.success("Input data saved to 'new_data.csv'.")
        st.balloons()
    except Exception as e:
        st.error(f"Error saving data: {e}")

# Display saved data
if st.session_state.new_data:
    st.subheader("📊 Saved Input Data")
    st.dataframe(pd.DataFrame(st.session_state.new_data), use_container_width=True)

# Footer
st.markdown("""
    <div class="footer">
        <p><b>Model Details</b>: RandomForestRegressor (R² = 83.93%, MAE ≈ 136).<br>
        Developed by [Your Company Name]. Contact: info@company.com</p>
    </div>
""", unsafe_allow_html=True)