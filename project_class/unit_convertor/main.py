import streamlit as st


def convert_units(value, unit_form, unit_to):

    conversion = {
        "meter_kilometer": 0.001,
        "kilometer_meter": 1000,
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000,
    }

    key = f"{unit_form}_{unit_to}"
    
    if key in conversion:
        conversion = conversion[key]
        return value * conversion
    else:
        "Conversion not Supported"
    
st.title("Unit Convertor")

value = st.number_input("Enter the value:")

unit_form = st.selectbox("Convert from:",["meter","kilometer","gram","kilogram"])
unit_to = st.selectbox("Convert to:",["meter","kilometer","gram","kilogram"])

if st.button("Convert"):
    result = convert_units(value, unit_form, unit_to)
    st.write(f"Converted value: {result}")
