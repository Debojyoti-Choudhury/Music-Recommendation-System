import streamlit as st
# Page config setup
st.set_page_config(
    page_title="Music Recommendation System",
    page_icon=":music:",
    layout="wide",
    menu_items={
        "About": """
        ## Thanks for using the app
        Made with ❤️ by [Debojyoti Choudhury](https://github.com/Debojyoti-Choudhury)
        """,
        "Get Help": "https://twitter.com/DebojyotiChou",
        "Report a Bug": "https://github.com/Debojyoti-Choudhury/Music-Recommendation-System/issues",
    },
)


# ----------------------------------------- UI ---------------------------------------------

# Sidebars
# Title "Dry bean Classifier"

st.markdown(
    """
    <center>
        <h1>
            <i>Music Recommendation System</i>
        </h2>
    </center>""",
    unsafe_allow_html=True,
)

with st.expander(label="The app is created by", expanded=True):
    st.info(
        """
        1. Created By: Debojyoti Choudhury

        2. Enrollment Number: 40AIML137-21/2

        3. Programme: Diploma in AI and ML
        """
    )

with st.expander(label="Using the app"):
    st.write(
        """
        This app will show the model performance of the KK Box Music Recommendation Challenge.

        The data is obtained from [Kaggle WSDM-KKBox's Music Recommendation Challenge](https://www.kaggle.com/competitions/kkbox-music-recommendation-challenge/data). 
        """
    )
st.sidebar.image("images/music1.gif")