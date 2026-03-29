import streamlit as st
#creating the page configuration:
st.set_page_config(
    page_title="Global Movers",
    page_icon = "🌎",
)

#creating a sidebar

def main():
    st.sidebar.title("Navigation")

    choice = st.sidebar.radio("Go to", ["Dashboard", "Tool"])

    if choice == "Dashboard":
        show_dashboard()
    elif choice == "Tool":
        show_converter()

 
#function to display the dashboard
def show_dashboard():
    st.header("Company Dashboard")
    st.info("Welcome to the Global Movers Driver's Portal")

    col1, col2 = st.columns(2)

    with col1: 
        st.subheader("Speeed Limits")
        st.write("Urbal: 50km/h")
        st.write("Highway: 90km/h")

    with col2:
        st.subheader("Cargo Load")
        st.write ("Max Load: 20,000 kg")
        st.write ("TAKE A BREAK EVERY 4 HOURS")


def show_converter():
    st.header("Weight Converter")
    st.write ("-----")

    weight = st.number_input("Enter weight", min_value = 0.0)

    conversion = st.selectbox ("Convert to", ["kg to lbs","lbs to kg"])

    if st.button("Calculate"):
        result = 0.0
        if conversion == "kg to lbs":
            result = weight * 2.20462
            st.success(f"{weight} kg is {round(result, 2)} lbs")
        elif conversion == "lbs to kg":
            result = weight / 2.20462
            st.success(f"{weight} lbs is {round(result, 2)} kg")
        
        
main ()