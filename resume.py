import streamlit as st
from pathlib import Path
import base64

st.set_page_config(page_title="Kishan Kumar Suresh Kumar",
                   page_icon=":memo:",
                   layout="wide",
                   initial_sidebar_state="expanded")


def img_to_bytes(img_path):
    img_path = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_path).decode()
    return encoded


def sidebar():
    st.sidebar.markdown(
        f'''<img src='data:image/png;base64,{img_to_bytes("kish.jpg")}' class='img-fluid' width=225 height=280>''',
        unsafe_allow_html=True
    )
    st.sidebar.title("Kishan Kumar Suresh Kumar")
    st.sidebar.markdown("Date of Birth: 13 / 01 / 2005")
    st.sidebar.markdown("Place: Salem")
    st.sidebar.markdown("Age: 19")
    st.sidebar.markdown("Mail: [krss132005@gmail.com](mailto:krss132005@gmail.com)", unsafe_allow_html=True)
    st.sidebar.markdown("GitHub: [Kishankumar1328](https://github.com/Kishankumar1328)", unsafe_allow_html=True)
    st.sidebar.markdown("LinkedIn: [Kishan Kumar](https://www.linkedin.com/in/kishan-kumar-suresh-kumar-037175259/)",
                        unsafe_allow_html=True)
    st.sidebar.markdown("Phone: [+91 6380383183](tel:+916380383183)", unsafe_allow_html=True)

    if st.sidebar.button("Download Resume"):
        with open("Kishan_Kumar_Resume.pdf", "rb") as file:
            st.sidebar.download_button(
                label="Download Resume",
                data=file,
                file_name="Kishan_Kumar_Resume.pdf",
                mime="application/pdf"
            )


def About():
    st.title("About Me")
    st.markdown("""
    Skilled in Python with a solid understanding of data science fundamentals. 
    Actively developing expertise in machine learning algorithms and model engineering, 
    with a commitment to advancing artificial intelligence. Passionate about leveraging 
    technology to solve complex problems, I excel in tackling challenges that demand innovative solutions.
    """)


def Education():
    st.title("Education")
    with st.expander("High School"):
        st.header("Golden Choice Matric.Hr.Sec.School")
        st.markdown("**Grade 10:** 80% (2019-2020)")
        st.markdown("**Grade 12:** 82.5% (2021-2022)")

    with st.expander("Undergraduate"):
        st.header("M.Kumarasamy College Of Engineering")
        st.markdown("**Degree:** Bachelor's in Artificial Intelligence and Data Science (2022 - 2026)")


def Projects():
    st.title("Projects")
    with st.expander("Emotion Detection"):
        st.markdown("**Completed Year:** 2024")
        st.markdown("""
        - Proficient in AI and ML for developing emotion detection systems.
        - Specialized in computer vision, NLP, and affective computing.
        - Experienced in research and practical applications across diverse domains.
        - Skilled in designing and implementing deep learning architectures like CNNs, RNNs, and transformer models.
        """)

    with st.expander("Stock Dashboard with GPT & ML Model"):
        st.markdown("**Completed Year:** 2024")
        st.markdown("""
        - Experienced AI and ML specialist, skilled at solving complex business problems.
        - Proficient in using advanced technologies for actionable insights and decision-making.
        - Expertise in building predictive models for financial markets and creating interactive data visualizations.
        - Committed to staying updated with AI and ML trends for delivering innovative solutions.
        """)

    with st.expander("Stock Prediction"):
        st.markdown("**Completed Year:** 2023")
        st.markdown("""
        - Skilled in stock prediction using data analysis and ML techniques.
        - Experienced in developing models to forecast stock prices and trends.
        - Proficient in utilizing historical data and market indicators for predictive modeling.
        - Dedicated to leveraging technology for accurate and informed investment decisions.
        """)


def Skills():
    st.title("Skills")
    col1, col2 = st.columns(2)

    with col1:
        st.header("Technical Skills")
        st.markdown("""
        - **Python:** Advanced
        - **Data Analysis:** Advanced
        - **Data Science:** Advanced
        - **Machine Learning:** Intermediate
        - **C:** Intermediate
        - **Java:** Intermediate
        - **HTML:** Intermediate
        - **CSS:** Intermediate
        """)

    with col2:
        st.header("Soft Skills")
        st.markdown("""
        - Teamwork
        - Adaptability
        - Communication
        - Time management
        - Creativity
        - Decision-making
        """)


def Certifications():
    st.title("Certifications & Badges")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Python:** [HackerRank](https://www.hackerrank.com/certificates/8c2f4f9d69d8)")
        st.markdown(
            "**Python For Data Science:** [IBM](https://www.credly.com/badges/f7efca15-02ec-46be-a0ac-84c62fea02b3/linked_in_profile)")
        st.markdown(
            "**Data Analysis Using Python:** [IBM](https://www.credly.com/badges/ef16ffb5-db3c-4ded-b41b-fcaa35b2d2da/linked_in_profile)")
        st.markdown(
            "**Data Visualization Using Python:** [IBM](https://www.credly.com/badges/a33539eb-e491-449c-8a12-6f1f925248ba/linked_in_profile)")
        st.markdown(
            "**Applied Data Science:** [IBM](https://www.credly.com/badges/7b399bf8-3691-4ede-b4a9-77cfa15fb325/linked_in_profile)")

    with col2:
        st.markdown(
            "**Machine Learning with Python:** [IBM](https://www.credly.com/badges/77aad513-7672-4d04-bfb8-39b37e55d986)")
        st.markdown(
            "**Prompt Engineering:** [IBM](https://courses.cognitiveclass.ai/certificates/e605bffd4da945149049fe4a2955efd4)")
        st.markdown(
            "**Data Science Methodology:** [IBM](https://www.credly.com/badges/70ae2196-2b81-4544-b703-16d7b09cdccb/linked_in_profile)")
        st.markdown(
            "**Data Science Foundation:** [IBM](https://www.credly.com/badges/ff7ceaf4-a2b6-4b41-a27e-ac1b361f060f/linked_in_profile)")
        st.markdown(
            "**Intro To Generative AI:** [Google](https://www.cloudskillsboost.google/public_profiles/c48c7f95-8155-458b-87af-46cb13ef6f95/badges/8493572?utm_medium=social&utm_source=linkedin&utm_campaign=ql-social-share)")


def Contact():
    st.title("Contact Me")
    col1, col2 = st.columns(2)

    with col1:
        st.header("Address")
        st.markdown("93, Govindammal Nagar,")
        st.markdown("Seelanaickenpatty,")
        st.markdown("Salem - 636 201")

    with col2:
        st.header("Connect With Me")
        st.markdown("Mail: [krss132005@gmail.com](mailto:krss132005@gmail.com)", unsafe_allow_html=True)
        st.markdown("GitHub: [Kishankumar1328](https://github.com/Kishankumar1328)", unsafe_allow_html=True)
        st.markdown("LinkedIn: [Kishan Kumar](https://www.linkedin.com/in/kishan-kumar-suresh-kumar-037175259/)",
                    unsafe_allow_html=True)


sidebar()
About()
Education()
Projects()
Skills()
Certifications()
Contact()
