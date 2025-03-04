import streamlit as st

def convert_units(value, from_unit, to_unit, conversion_dict):
    if from_unit in conversion_dict and to_unit in conversion_dict:
        return value * (conversion_dict[to_unit] / conversion_dict[from_unit])
    return None

st.title("Unit Converter")
st.write("Convert Length, Weight, and Temperature")

conversion_type = st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])

if conversion_type == "Length":
    length_units = {"Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000, "Feet": 3.28084, "Inches": 39.3701}
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From", list(length_units.keys()))
    to_unit = st.selectbox("To", list(length_units.keys()))
    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit, length_units)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Weight":
    weight_units = {"Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274}
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From", list(weight_units.keys()))
    to_unit = st.selectbox("To", list(weight_units.keys()))
    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit, weight_units)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif conversion_type == "Temperature":
    value = st.number_input("Enter value:", format="%.2f")
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    if st.button("Convert"):
        result = None
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = (value - 273.15) * 9/5 + 32
        if result is not None:
            st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
        else:
            st.warning("Invalid conversion.")

st.info("Nabeel Akhter")
