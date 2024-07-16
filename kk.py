import streamlit as st
from pathlib import Path
import base64
import mysql.connector


# Main Function
st.set_page_config(page_title="Kishan kumar Suresh Kumar",
                   page_icon="kk.jpg",
                   layout="wide",
                   initial_sidebar_state="expanded")
def connect_to_database():
    conn = mysql.connector.connect(
        host="your_host",
        user="your_username",
        password="your_password",
        database="your_database_name"
    )
    return conn

def img_to_bytes(img_path):
    img_path = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_path).decode()
    return encoded

def sidebar():
    st.sidebar.markdown(f'''<img src='data:image/png;base64,{img_to_bytes("")}' class='img-fluid' width=225 height=280>''', unsafe_allow_html=True)
    st.sidebar.title("Kishan Kumar Suresh Kumar")
    st.sidebar.markdown("Date of Birth : 13 / 01 / 2005 ")
    st.sidebar.markdown("Place : Salem")
    st.sidebar.markdown("Age : 19")
    st.sidebar.markdown("""Mail : [krss132005@gmail.com](mailto:krss132005@gmail.com)""", unsafe_allow_html=True)
    st.sidebar.markdown("""LinkedIn : [Kishan kumar](https://www.linkedin.com/in/kishan-kumar-suresh-kumar-037175259/)""", unsafe_allow_html=True)
    st.sidebar.markdown("""GitHub : [Kishankumar1328](https://github.com/Kishankumar1328)""", unsafe_allow_html=True)
    st.sidebar.markdown("""Phone : [+91 6380383183](tel:+916380383183)""", unsafe_allow_html=True)
    data = "profile.jpg"

def About():
    st.title("Myself")
    st.markdown("Skilled in Python with a solid understanding of data science fundamentals. Actively developing expertise in machine learning algorithms and model engineering, with a commitment to advancing artificial intelligence. Passionate about leveraging technology to solve complex problems, I excel in tackling challenges that demand innovative solutions.")

def Education():
    a, b = st.columns(2)
    a.title("Education")
    a.header("Grade 10")
    a.markdown("2019-2020")
    a.markdown("Golden Choice Matric.Hr.Sec.School")
    a.markdown("I completed my Grade 10th with an overall score of 80%.")
    a.header("Grade 12")
    a.markdown("2021-2022")
    a.markdown("Golden Choice Matric.Hr.Sec.School")
    a.markdown("I completed my Grade 12th with an overall score of 82.5%.")
    # college
    a.header("Undergraduate")
    a.markdown("2022 - 2026")
    a.markdown("M.Kumarasamy College Of Engineering")
    a.markdown("I am currently pursuing a Bachelor's Degree in Artificial Intelligence and Data Science")
    a.title("Languages")
    a.markdown("🔹 English  - Intermediate")
    a.markdown("🔹 Telugu   - Native")
    a.markdown("🔹 Tamil    - Advanced")

    # projects
    b.title("Project")
    b.header("Emotion Detection")
    b.markdown("Completed Year : 2024")
    b.markdown("🔹 Proficient in artificial intelligence and machine learning for developing emotion detection systems.")
    b.markdown("🔹 Specialized in computer vision, natural language processing, and affective computing.")
    b.markdown("🔹 Experienced in research and practical applications across diverse domains.")
    b.markdown(
        "🔹 Skilled in designing and implementing deep learning architectures like CNNs, RNNs, and transformer mode")

    b.header("Stock Dashboard with GPT & Ml model")
    b.markdown("Completed Year : 2024")
    b.markdown("🔹 Experienced AI and ML specialist, skilled at solving complex business problems.")
    b.markdown("🔹 Proficient in using advanced technologies for actionable insights and decision-making.")
    b.markdown(
        "🔹 Expertise in building predictive models for financial markets and creating interactive data visualizations.")
    b.markdown("🔹 Committed to staying updated with AI and ML trends for delivering innovative solutions.")

    b.header("Stock Prediction")
    b.markdown("Completed Year : 2023")
    b.markdown("🔹 Skilled in stock prediction using data analysis and machine learning techniques.")
    b.markdown("🔹 Experienced in developing models to forecast stock prices and trends.")
    b.markdown("🔹 Proficient in utilizing historical data and market indicators for predictive modeling.")
    b.markdown("🔹 Dedicated to leveraging technology for accurate and informed investment decisions.")

    st.markdown("---")

    c, d = st.columns(2)

    c.title("Technical Skills")
    # Disable widgets to remove interactivity:
    c.markdown("🔹 Python           - Advanced")
    c.markdown("🔹 Data Analysis    - Advanced")
    c.markdown("🔹 Data Science     - Advanced")
    c.markdown("🔹 Machine Learning - Intermediate")
    c.markdown("🔹 c                - Intermediate")
    c.markdown("🔹 java             - Intermediate")
    c.markdown("🔹 HTML             - Intermediate")
    c.markdown("🔹 CSS              - Intermediate")

    d.title("Soft Skills")
    d.markdown("🔹Teamwork")
    d.markdown("🔹Adaptability")
    d.markdown("🔹Communication")
    d.markdown("🔹Time management")
    d.markdown("🔹Creativity")
    d.markdown("🔹Decision-making")

    st.markdown("---")
    st.title("Certifications & Badges")
    e, f = st.columns(2)
    e.markdown("""🔹Python - [HackerRank](https://www.hackerrank.com/certificates/8c2f4f9d69d8)""")
    e.markdown("""🔹Python For Data Science - [IBM](https://www.credly.com/badges/f7efca15-02ec-46be-a0ac-84c62fea02b3/linked_in_profile)""")
    e.markdown("""🔹Data Analysis Using Python - [IBM](https://www.credly.com/badges/ef16ffb5-db3c-4ded-b41b-fcaa35b2d2da/linked_in_profile)""")
    e.markdown("""🔹Data Visualization Using Python - [IBM](https://www.credly.com/badges/a33539eb-e491-449c-8a12-6f1f925248ba/linked_in_profile)""")
    e.markdown("""🔹Applied Data Science - [IBM](https://www.credly.com/badges/7b399bf8-3691-4ede-b4a9-77cfa15fb325/linked_in_profile)""")
    f.markdown("""🔹Machine Learning with Python - [IBM](https://www.credly.com/badges/77aad513-7672-4d04-bfb8-39b37e55d986)""")
    f.markdown("""🔹Prompt Engineering - [IBM](https://courses.cognitiveclass.ai/certificates/e605bffd4da945149049fe4a2955efd4)""")
    f.markdown("""🔹Data Science Methodology -[IBM](https://www.credly.com/badges/70ae2196-2b81-4544-b703-16d7b09cdccb/linked_in_profile)""")
    f.markdown("""🔹Data Science Foundation - [IBM](https://www.credly.com/badges/ff7ceaf4-a2b6-4b41-a27e-ac1b361f060f/linked_in_profile)""")
    f.markdown("""🔹Intro To Generative AI - [Google](https://www.cloudskillsboost.google/public_profiles/c48c7f95-8155-458b-87af-46cb13ef6f95/badges/8493572?utm_medium=social&utm_source=linkedin&utm_campaign=ql-social-share)""")

    st.markdown("---")



    st.title("Contact Me")
    g, h = st.columns(2)
    g.header("Address")
    g.markdown("93,Govindammal Nagar,")
    g.markdown("Seelanaickenpatty,")
    g.markdown("Salem - 636 201")

    h.header("Connect With Me")
    h.markdown("""Mail : [krss132005@gmail.com](mailto:krss132005@gmail.com)""", unsafe_allow_html=True)
    h.markdown("""GitHub : [Kishankumar1328](https://github.com/Kishankumar1328)""", unsafe_allow_html=True)
    h.markdown("""LinkedIn : [Kishan kumar](https://www.linkedin.com/in/kishan-kumar-suresh-kumar-037175259/)""", unsafe_allow_html=True)

    conn = connect_to_database()
    cursor = conn.cursor()

    with st.form(key="Submit"):
        i, j = st.columns(2)
        username = i.text_input("Name")
        email = j.text_input("Email")
        message = st.text_input("Message")
        if st.form_submit_button("Hire Me"):
            # Insert data into the database on form submission
            try:
                cursor.execute("INSERT INTO applications (username, email, message) VALUES (%s, %s, %s)",
                               (username, email, message))
                conn.commit()
                st.success("Application submitted successfully!")
            except Exception as e:
                st.error(f"Error: {str(e)}")


sidebar()
About()
Education()

