import streamlit as st
import datetime, time, os
from Database import Database
from streamlit_option_menu import option_menu
import pro

class Page1:
    def __init__(self):
        st.markdown("""
                                <h1 style='text-align: center;'>Hotel <span style='color:red;'>Krishna</span></h1>
                                """, unsafe_allow_html=True)
        self.page_selection = None
        self.image = None
        self.username = None
        self.email = None
        self.contact = None
        self.db = Database()
        self.initialize()
        self.selected = None
    def initialize(self):
        self.selected = option_menu(
            menu_title=None,
            options=["Login", "Register"],
            icons=["box-arrow-in-right", "r-square-fill"],
            default_index=1,
            orientation="horizontal",
        )
        if self.selected == "Login":
            self.login()
        if self.selected == "Register":
            self.register()
        if self.selected == "Current account":
            self.current_user()

    def login(self):
        st.markdown(''' 
            ### Login
            ''', True)
        log_email = st.text_input("Enter your email address")
        log_passw = st.text_input("Enter your password", type='password')
        print(log_email, log_passw)
        co1, co2 = st.columns(2)
        log_sub_button = co1.button('LOG-IN')
        if log_sub_button:
            if str(log_email).endswith('@gmail.com') and not str(log_email).startswith('@gmail.com'):
                email_exists = self.db.check_present(log_email, log_passw, 'User', 'email', 'Password')
                if email_exists:
                    st.write('Login successfully👍')
                    st.write('Redirecting to Hotel site')
                    progress_bar = st.progress(0)
                    for i in range(100):
                        time.sleep(0.05)
                        progress_bar.progress(i + 1)
                    name, mail, contact = self.db.get_data(log_email)
                    self.username = name
                    self.email = mail
                    self.contact = contact
                    self.current_user()
                    pro.head(self.username)
                else:
                    st.write('Invalid username or password❌; new user? Go to Register')
            else:
                st.write('Invalid username')
        return log_passw, log_email

    def register(self):
        st.markdown(''' 
                    ### Register
                    ''', True)
        col1, col2 = st.columns(2)
        name = col1.text_input("Enter your name")
        email = col2.text_input("Enter you email address")
        phone = col1.text_input("Enter Phone Number")
        pass1 = col2.text_input("Enter one time password", type='password')
        pass2 = col1.text_input("Confirm password", type='password')
        sub_button = col1.button('SIGN-UP')
        if sub_button:
            if name != '':
                email_exists = self.db.check_email(email, 'User', 'email')
                if str(email).endswith('@gmail.com') and not str(email).startswith('@gmail.com'):
                    if not email_exists:
                        if pass1 == pass2 and pass1 != '' and phone != '':
                            print(name, phone, email, pass2)
                            self.db.user_table(name, email, phone, pass2)
                            st.write("Your Account has been registered successfully👍")
                            st.write('Redirecting to Hotel site')
                            progress_bar = st.progress(0)
                            for i in range(100):
                                time.sleep(0.05)
                                progress_bar.progress(i + 1)
                            self.username = name
                            self.email = email
                            self.contact = phone
                            self.selected = "Current account"
                            self.current_user()
                            pro.head(self.username)
                        else:
                            st.write('Password mismatch')
                    else:
                        st.write('User with this email already exists go to login')
                else:
                    st.write('Invalid email address')
            else:
                st.write("Invalid name")
        return name, phone, email, pass2

    def current_user(self):
        if self.username is None:
            st.write('No User Found')
            st.write('Go to login if you already have an account')
            st.write('Go to Register if you dont have an account')
        else:
            st.header(
                f"Name of the user : {self.username}"
            )
            st.subheader(
                f"Contact Details:"
            )
            st.write(
                f"Email of User {self.email}"
            )
            st.write(
                f"Contact Number of User {self.contact}"
            )

