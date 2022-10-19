import streamlit as st
import pandas as pd

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

        To see the code of Exploratory Data Analysis and Modelling please see the [github repo](https://github.com/Debojyoti-Choudhury/Music-Recommendation-System)
        """
    )
st.sidebar.image("images/music2.jpg")


# Choose model
model_type = st.sidebar.radio(
    "Choose Model",
    options=["Logistic Regression", "Support Vector Classifier", "Decision Tree Classifier", "Random Forest Classifier", "XGBoost Classifier", "LightGBM Classifier"],
    index=0,
    help="Check on any model to see its performance",
)

df = pd.read_csv("./output/model_output.csv", index_col=0)

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Precision", df.loc[model, "Precision"])
col2.metric("Recall", df.loc[model, "Recall"])
col3.metric("F1 score", df.loc[model, "f1score"])
col4.metric("Accuracy", df.loc[model, "accuracy"])
col5.metric("AUC ROC", df.loc[model, "AUC_ROC"])