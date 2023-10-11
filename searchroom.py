import streamlit as st
import datetime
import math
from PIL import Image
from streamlit_option_menu import option_menu


class Calendar:

    def __init__(self):
        st.markdown("""
                                    <h1 style='text-align: center;'>Hotel <span style='color:blue;'>Krishna</span></h1>
                                    """, unsafe_allow_html=True)
        st.subheader(f"Welcome")
        st.markdown("""
                                <h2 style='text-align: left;'>Search Tables</h2>
                                """, unsafe_allow_html=True)
        self.room = 1
        self.show_payments = False
        self.banks_in_india = [
            "State Bank of India",
            "Bank of Baroda",
            "Bank of India",
            "Bank of Maharashtra",
            "Canara Bank",
            "Central Bank of India",
            "Indian Bank",
            "Indian Overseas Bank",
            "Punjab & Sind Bank",
            "Punjab National Bank",
            "UCO Bank",
            "Union Bank of India",
            "Axis Bank Ltd.",
            "Bandhan Bank Ltd.",
            "CSB Bank Ltd.",
            "City Union Bank Ltd.",
            "DCB Bank Ltd.",
            "Dhanlaxmi Bank Ltd.",
            "Federal Bank Ltd.",
            "HDFC Bank Ltd",
            "ICICI Bank Ltd.",
        ]
        self.months = ["January", "February", "March", "April", "May", "June", "July", "August",
                       "September", "October", "November", "December"]
        self.booking()

        if self.show_payments:
            self.payment()

    def booking(self):
        tmp_list = []
        today = datetime.datetime.now()
        print(today)
        date_in = st.date_input(
            "Select Date of Booking",
            min_value=today,
            format="DD.MM.YYYY",
        )
        time_in = st.time_input(
            label='Choose Time to visit'
        )
        print(date_in)
        col1, col2, col3 = st.columns(3)
        number = col1.number_input("Number of Persons", min_value=1, step=1)
        print("Added Person", tmp_list)
        btn_ok = st.button("OK")
        if btn_ok:
            st.text(f"You are going to book table/s for {number} people on date {date_in} and time {time_in}"
                    )
        self.payment()

    def payment(self):
        selected = option_menu(
            menu_title="Choose Payment Method",
            options=["UPI", "Credit Card", "Debit Card", "Net Banking"],
            icons=["paypal", "credit-card", "credit-card", "bank"],
            default_index=0,
            orientation="horizontal",
        )

        if selected == "UPI":
            pay_id = st.text_input("Enter your UPI ID")
            mo_no = st.text_input("Enter your Mobile Number")
        if selected == "Credit Card":
            pay_id = st.selectbox("Select Bank", options=self.banks_in_india)
            card_number = st.text_input("Enter your card number")
            card_name = st.text_input("Enter your name on your card")
            st.write("Expiry Date")
            col1, col2, col3 = st.columns(3)
            month = col1.selectbox("",
                                   options=self.months, )
            year = col2.selectbox("", options=[i for i in range(2023, 3000)])
            cvv = col3.text_input("Enter ccv number", type="password")
        if selected == "Debit Card":
            pay_id = st.selectbox("Select Bank", options=self.banks_in_india)
            card_number = st.text_input("Enter your card number")
            card_name = st.text_input("Enter your name on your card")
            st.write("Expiry Date")
            col1, col2, col3 = st.columns(3)
            month = col1.selectbox("",
                                   options=self.months, )
            year = col2.selectbox("", options=[i for i in range(2023, 2100)])
            cvv = col3.text_input("Enter ccv number", type="password")
        if selected == "Net Banking":
            pay_id = st.selectbox("Select Bank", options=self.months)
            col1, col2 = st.columns(2)
            acc = col1.text_input("Enter Bank Account Number")
            ifsc = col2.text_input("Enter Bank IFSC Code")
        st.checkbox("I agree to the Terms & Conditions")
