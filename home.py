import streamlit as st

class HomePage:
    def __init__(self):
        st.markdown("""
                                    <h1 style='text-align: center;'>Hotel <span style='color:blue;'>Krishna</span></h1>
                                    """, unsafe_allow_html=True)
        self.home()

    def home(self):
        st.image('logo.jpg')
        st.subheader(
            "अन्नपुर्णे सदापुर्णे शंकर प्राण वल्लभे|  "
            "ज्ञान वैराग्य सिध्यर्थ भिक्षा देही च पार्वती||"
        )
