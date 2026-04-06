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

# Seat Type
st.write("Select Seat Type")
seat_type = st.radio(
    "",
    ["Standard", "Premium"],
    index=None   
)

#  Condition to enable button
is_valid = (
    customer_name.strip() != "" and
    movie_title != "-- Select Movie --" and
    show_time != "-- Select Time --" and
    seat_type is not None
)

# Button (disabled if not valid)
if st.button("Book Ticket", disabled=not is_valid):
    try:
        st.success(" Booking Successful!")
        st.write("###  Booking Details")
        st.write(f"**Customer Name:** {customer_name}")
        st.write(f"**Movie Title:** {movie_title}")
        st.write(f"**Show Time:** {show_time}")
        st.write(f"**Seat Type:** {seat_type}")

    except Exception as e:
        st.error(f" Unexpected Error: {e}")