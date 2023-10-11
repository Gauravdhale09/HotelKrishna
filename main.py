import streamlit as st

from streamlit_option_menu import option_menu
import home, user, searchroom, Bookings

st.set_page_config(
    page_title="Hotel Krishna",
)

text_new = ''


def head(text):
    global text_new
    st.sidebar.header(
        text,
    )
    text_new = text







class MultiApp:

    def __init__(self):
        self.apps = []
        head(text_new)
    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:
            app = option_menu(
                menu_title='Hotel Krishna',
                options=['Home', 'User Account', 'SearchTables', 'YourBooking', 'Contact'],
                icons=['house-fill', 'person-circle', 'house', 'journals', 'person-lines-fill'],
                menu_icon='House',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "15px"},
                    "nav-link": {"color": "white", "font-size": "15px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "lightgreen"},
                    "nav-link-selected": {"background-color": "#02ab21"}, }

            )

        if app == "Home":
            home.HomePage()
        if app == "User Account":
            user.Page1()
        if app == "SearchTables":
            searchroom.Calendar()
        if app == "YourBooking":
            Bookings.Booking()

    run()
