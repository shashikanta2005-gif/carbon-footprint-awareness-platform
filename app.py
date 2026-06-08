import streamlit as st

# Page layout configuration
st.set_page_config(
    page_title="EcoTrack - Carbon Footprint Platform",
    page_icon="🌍",
    layout="centered"
)

# Header Section
st.title("🌍 EcoTrack")
st.subheader("Understand, Track, and Reduce Your Carbon Footprint")
st.write("Small daily adjustments lead to significant environmental impacts. Use this calculator to estimate your daily footprint and unlock tailored reduction strategies.")

st.markdown("---")

# User Inputs (The Tracking Quiz)
st.header("📊 Daily Activity Tracker")

# Category A: Transportation
st.subheader("🚗 Transportation")
transport_type = st.selectbox(
    "Primary mode of transport today:",
    ["Electric Vehicle (EV)", "Public Transport (Bus/Train)", "Petrol/Diesel Car", "Two-Wheeler (Petrol)", "Walking/Bicycle"]
)
distance = st.number_input("Approximate distance traveled today (in km):", min_value=0.0, step=1.0)

# Category B: Energy & Home
st.subheader("⚡ Home Energy")
electricity = st.number_input("Estimated daily household electricity consumption (in kWh):", min_value=0.0, step=1.0)

# Category C: Diet
st.subheader("🍽️ Dietary Choice")
diet = st.selectbox(
    "Primary diet type today:",
    ["Heavy Meat Consumer", "Balanced (Meat & Veg)", "Vegetarian", "Vegan"]
)

st.markdown("---")

# Calculation constants (kg of CO2e per unit)
transport_factors = {
    "Electric Vehicle (EV)": 0.05,
    "Public Transport (Bus/Train)": 0.03,
    "Petrol/Diesel Car": 0.20,
    "Two-Wheeler (Petrol)": 0.10,
    "Walking/Bicycle": 0.0
}

diet_factors = {
    "Heavy Meat Consumer": 7.2,
    "Balanced (Meat & Veg)": 5.4,
    "Vegetarian": 3.8,
    "Vegan": 2.9
}

# Math logic
transport_emissions = distance * transport_factors[transport_type]
energy_emissions = electricity * 0.82  # Standard average grid intensity
diet_emissions = diet_factors[diet]

total_emissions = transport_emissions + energy_emissions + diet_emissions

# Execution Trigger
if st.button("Calculate My Footprint", type="primary"):
    st.header("📉 Your Daily Insights")
    
    # Display Total Score
    st.metric(label="Total Daily Carbon Footprint", value=f"{total_emissions:.2f} kg CO2e")
    
    # Breakdown Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("🚗 Transport", f"{transport_emissions:.2f} kg")
    col2.metric("⚡ Energy", f"{energy_emissions:.2f} kg")
    col3.metric("🍽️ Diet", f"{diet_emissions:.2f} kg")
    
    st.markdown("---")
    
    # Actionable Tips (Reduce element)
    st.header("🌱 Personalized Action Plan")
    st.write("Implement these simple shifts to immediately lower your impact tomorrow:")
    
    if transport_emissions > 5:
        st.info("💡 **Transport Tip:** Your commuting emissions are on the higher side today. Consider carpooling or using public transit to shave off up to 50% of this footprint.")
        
    if energy_emissions > 4:
        st.info("💡 **Energy Tip:** Remember to switch off background appliances at the plug points when idle to minimize phantom power drain.")
        
    if diet in ["Heavy Meat Consumer", "Balanced (Meat & Veg)"]:
        st.info("💡 **Diet Tip:** Swapping just one or two meals a week to plant-based options significantly drops your ongoing footprint.")
    else:
        st.success("🌟 **Great Job!** Your dietary choice is already keeping your food emissions highly optimized!")