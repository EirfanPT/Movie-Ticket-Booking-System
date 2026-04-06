import streamlit as st

st.title(" Movie Ticket Booking System")

# Input Fields
customer_name = st.text_input("Enter Customer Name")

movie_title = st.selectbox(
    "Select Movie Title",
    ["Avengers", "Kung Fu Panda", "Frozen"]
)

show_time = st.selectbox(
    "Select Show Time",
    ["10:00 AM", "2:00 PM", "8:00 PM"]
)

seat_type = st.radio(
    "Select Seat Type",
    ["Standard", "Premium"]
)

# Button
if st.button("Book Ticket"):
    try:
        # Validation
        if customer_name.strip() == "":
            raise ValueError("Customer name cannot be empty!")

        # Display Output
        st.success(" Booking Successful!")
        st.write("### Booking Details")
        st.write(f"**Customer Name:** {customer_name}")
        st.write(f"**Movie Title:** {movie_title}")
        st.write(f"**Show Time:** {show_time}")
        st.write(f"**Seat Type:** {seat_type}")

    except ValueError as ve:
        st.error(f" Error: {ve}")
    except Exception as e:
        st.error(f" Unexpected Error: {e}")