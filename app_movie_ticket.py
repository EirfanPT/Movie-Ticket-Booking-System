import streamlit as st

st.title("Movie Ticket Booking System")

# Inputs
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
    ["Standard", "Premium"],
    index=None
)

# Button
if st.button("Book Ticket"):
    try:
        # Validation
        if customer_name.strip() == "":
            raise ValueError("Customer name cannot be empty")

        if movie_title == "-- Select Movie --":
            raise ValueError("Movie title must be selected")

        if show_time == "-- Select Time --":
            raise ValueError("Show time must be selected")

        if seat_type is None:
            raise ValueError("Seat type must be selected")

        # Success Output
        st.success("Booking successful")
        st.write("Booking Information:")
        st.write("Customer Name:", customer_name)
        st.write("Movie Title:", movie_title)
        st.write("Show Time:", show_time)
        st.write("Seat Type:", seat_type)

    except ValueError as ve:
        st.error(str(ve))   

    except Exception:
        st.error("An unexpected error occurred")