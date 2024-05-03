import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
from chatgpt_ops import ChatGPT_Proxy
from config.brand_scores import brand_scores


def run_app():

    st.set_page_config(page_title = "GrantAI", page_icon = ":rainbow:")
    nav_bar()
    with st.container(border = True):
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image("./assets/logo3.svg")
        with col2:
            st.title("Just Like Us - GrantAI")
        col1, col2 = st.columns([1, 1])
        with col1:
            feature_options = get_target_features()
            category_selection = st.multiselect("Select feature", options = feature_options)
        with col2:
            all_brand_options = None
            brand_options = get_brand_options(brand_scores)
            brand_selection = st.selectbox("Select brand", options = brand_options)

        # uploaded_file = st.file_uploader("File to be attached", accept_multiple_files=False)
        generate_email_prososal_button = st.button("Generate Proposal")

        if generate_email_prososal_button:
            chatgpt_ops = ChatGPT_Proxy()
            with st.spinner("Generating proposal ..."):
                brand_mvv = chatgpt_ops.get_brand_mvv(brand_selection)
                with st.expander("Target Brand Mission-Vision-Values"):
                    st.markdown(brand_mvv)
                
                sentiment_analysis = chatgpt_ops.generate_sentiment_analysis(brand_selection, category_selection)
                with st.expander("Target Brand Public Perception Analysis"):
                    st.markdown(sentiment_analysis)

                email_proposal = chatgpt_ops.generate_email_proposal(brand_selection, brand_mvv)
                with st.expander(f"Email Proposal to {brand_selection}"):
                    st.markdown(email_proposal)


def nav_bar():

    pages = [""]
    styles = {
        "nav": {
            "background-color": "royalblue",
            "justify-content": "left",
        },
        "span": {
            "color": "white",
            "padding": "14px",
        },
    }
    options = {
        "show_menu": False,
        "show_sidebar": False,
    }

    page = st_navbar(
        pages,
        styles=styles,
        options=options,
    )


def get_target_features() -> list:

    options = [
        "Inclusivity Driven",
        "Allyship Driven",
        "Reputationally Driven"
    ]
    return(options)


def get_brand_options(brand_scores: dict) -> list:

    sorted_brands = dict(sorted(brand_scores.items(), key=lambda item: item[1], reverse = True))
    return(sorted_brands)
    
