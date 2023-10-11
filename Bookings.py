import streamlit as st

class Booking:
    def __init__(self):
        st.markdown("""
                                            <h1 style='text-align: center;'>Hotel <span style='color:blue;'>Krishna</span></h1>
                                            """, unsafe_allow_html=True)
        st.subheader(f"Welcome")
        st.markdown("""
                                        <h2 style='text-align: left;'>Your Bookings</h2>
                                        """, unsafe_allow_html=True)

    def table(self):
        pass
