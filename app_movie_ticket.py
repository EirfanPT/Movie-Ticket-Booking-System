import streamlit as st

st.title(" Movie Ticket Booking System")

# Input Fields
customer_name = st.text_input("Enter Customer Name")

movie_title = st.selectbox(
    "Select Movie Title",
    ["-- Select Movie --", "Avengers", "Kung Fu Panda", "Frozen"]
)

show_time = st.selectbox(
    "Select Show Time",
    ["-- Select Time --", "10:00 AM", "2:00 PM", "8:00 PM"]
)

seat_type = st.radio(
    "Select Seat Type",
    ["-- Select Seat Type --", "Standard", "Premium"]
)

# Button
if st.button("Book Ticket"):
    try:
        # Validation
        if customer_name.strip() == "":
            raise ValueError("Customer name cannot be empty!")

        if movie_title == "-- Select Movie --":
            raise ValueError("Please select a movie!")

        if show_time == "-- Select Time --":
            raise ValueError("Please select show time!")

        if seat_type == "-- Select Seat Type --":
            raise ValueError("Please select seat type!")

        # Output
        st.success(" Booking Successful!")
        st.write("###  Booking Details")
        st.write(f"**Customer Name:** {customer_name}")
        st.write(f"**Movie Title:** {movie_title}")
        st.write(f"**Show Time:** {show_time}")
        st.write(f"**Seat Type:** {seat_type}")

    except ValueError as ve:
        st.error(f" Error: {ve}")
    except Exception as e:
        st.error(f" Unexpected Error: {e}")