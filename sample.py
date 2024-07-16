import streamlit as st
from pathlib import Path
import base64
import altair as alt
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Kishan Kumar Suresh Kumar",
    page_icon=":memo:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Helper function to convert image to bytes
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

# Sidebar function
def sidebar():
    st.sidebar.markdown(
        f'''<img src='data:image/png;base64,{img_to_bytes("kish.jpg")}' class='img-fluid' width=225 height=280>''',
        unsafe_allow_html=True
    )
    st.sidebar.markdown("""
        <div style="text-align: center; margin-bottom: 20px;">
            <h2 style="color: #2E86C1;">Kishan Kumar Suresh Kumar</h2>
        </div>
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <i class='bx bx-calendar' style="font-size: 24px;"></i>
            <span style="margin-left: 10px;"><strong>Date of Birth:</strong> 13 / 01 / 2005</span>
        </div>
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <i class='bx bx-map' style="font-size: 24px;"></i>
            <span style="margin-left: 10px;"><strong>Place:</strong> Salem</span>
        </div>
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <i class='bx bx-user' style="font-size: 24px;"></i>
            <span style="margin-left: 10px;"><strong>Age:</strong> 19</span>
        </div>
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <i class='bx bx-envelope' style="font-size: 24px;"></i>
            <span style="margin-left: 10px;"><strong>Mail:</strong> <a href="mailto:krss132005@gmail.com">krss132005@gmail.com</a></span>
        </div>
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <i class='bx bxl-github' style="font-size: 24px;"></i>
            <span style="margin-left: 10px;"><strong>GitHub:</strong> <a href="https://github.com/Kishankumar1328">Kishankumar1328</a></span>
        </div>
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <i class='bx bxl-linkedin' style="font-size: 24px;"></i>
            <span style="margin-left: 10px;"><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/kishan-kumar-suresh-kumar-037175259/">Kishan Kumar</a></span>
        </div>
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <i class='bx bx-phone' style="font-size: 24px;"></i>
            <span style="margin-left: 10px;"><strong>Phone:</strong> <a href="tel:+916380383183">+91 6380383183</a></span>
        </div>
    """, unsafe_allow_html=True)

    if st.sidebar.button("Download Resume"):
        with open("Kishan_Kumar_Resume.pdf", "rb") as file:
            st.sidebar.download_button(
                label="Download Resume",
                data=file,
                file_name="Kishan_Kumar_Resume.pdf",
                mime="application/pdf"
            )

# About section
def About():
    st.title("About Me")
    st.markdown("""
    <style>
    .about-text {
        font-size: 20px;
        line-height: 1.6;
    }
    </style>
    <div class="about-text">
    I am a proficient Python developer with a robust foundation in data science fundamentals.
    Currently, I am intensifying my expertise in machine learning algorithms and model engineering, 
    driven by a deep commitment to advancing the field of artificial intelligence. 
    My passion for leveraging technology to solve intricate problems propels my ability to address challenges that require innovative and effective solutions.
    </div>
    """, unsafe_allow_html=True)

# Education section
def Education():
    st.title("Education")
    with st.expander("High School"):
        st.subheader("Golden Choice Matric.Hr.Sec.School")
        st.markdown("**Grade 10:** 80% (2019-2020)")
        st.markdown("**Grade 12:** 82.5% (2021-2022)")
    with st.expander("Undergraduate"):
        st.subheader("M.Kumarasamy College Of Engineering")
        st.markdown("**Degree:** Bachelor's in Artificial Intelligence and Data Science (2022 - 2026)")

# Projects section
def Projects():
    st.title("Projects")
    with st.expander("Emotion Detection (2024)"):
        st.markdown("""
        - Proficient in AI and ML for developing emotion detection systems.
        - Specialized in computer vision, NLP, and affective computing.
        - Experienced in research and practical applications across diverse domains.
        - Skilled in designing and implementing deep learning architectures like CNNs, RNNs, and transformer models.
        """)
    with st.expander("Stock Dashboard with GPT & ML Model (2024)"):
        st.markdown("""
        - Experienced AI and ML specialist, skilled at solving complex business problems.
        - Proficient in using advanced technologies for actionable insights and decision-making.
        - Expertise in building predictive models for financial markets and creating interactive data visualizations.
        - Committed to staying updated with AI and ML trends for delivering innovative solutions.
        """)
    with st.expander("Stock Prediction (2023)"):
        st.markdown("""
        - Skilled in stock prediction using data analysis and ML techniques.
        - Experienced in developing models to forecast stock prices and trends.
        - Proficient in utilizing historical data and market indicators for predictive modeling.
        - Dedicated to leveraging technology for accurate and informed investment decisions.
        """)
    with st.expander("Medicine Recommendation System (2024)"):
        st.markdown("""
        The **Allopathy Medicine Recommendation System** is an advanced tool designed to assist healthcare professionals in making informed decisions regarding the diagnosis and treatment of various diseases. Key features include:
        - **Machine Learning Techniques:** Leveraging algorithms for accurate diagnosis.
        - **Clinical Expertise Integration:** Combining AI with human expertise for improved outcomes.
        - **Efficiency Improvement:** Enhancing clinical decision-making and patient care.
        - **User-Friendly Interface:** Easy-to-use platform for healthcare providers.
        - **Real-Time Recommendations:** Providing timely and relevant medication suggestions.
        """)

# Skills section
def Skills():
    st.title("Skills")

    skills_data = {
        "Python": 90,
        "Data Analysis": 85,
        "Data Science": 80,
        "Machine Learning": 75,
        "C": 70,
        "Java": 65,
        "HTML": 60,
        "CSS": 55
    }

    soft_skills = {
        "Teamwork": "Collaborated effectively with team members to achieve project goals and ensure smooth workflow.",
        "Adaptability": "Adapted to new challenges and environments quickly, maintaining high performance.",
        "Communication": "Communicated complex technical concepts clearly to non-technical stakeholders.",
        "Time management": "Efficiently managed time to balance multiple projects and meet deadlines.",
        "Creativity": "Demonstrated creative problem-solving skills in developing innovative solutions."
    }

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Technical Skills")

        skills_df = pd.DataFrame(list(skills_data.items()), columns=['Skill', 'Proficiency'])

        chart = alt.Chart(skills_df).mark_bar().encode(
            x=alt.X('Proficiency', axis=alt.Axis(title='Proficiency (%)', titleFontSize=14)),
            y=alt.Y('Skill', sort='-x', axis=alt.Axis(title='', titleFontSize=14)),
            color=alt.condition(
                alt.datum.Proficiency > 50,
                alt.value('rgb(58, 71, 80)'),  # The positive color
                alt.value('rgb(199, 199, 199)')  # The negative color
            )
        ).properties(height=300)

        st.altair_chart(chart, use_container_width=True)

    with col2:
        st.subheader("Soft Skills")

        for skill, description in soft_skills.items():
            if st.button(skill):
                st.markdown(f"**{skill}:** {description}")

# Certifications section
def Certifications():
    st.title("Certifications & Badges")

    certifications = [
        {"title": "Python", "provider": "HackerRank", "link": "https://www.hackerrank.com/certificates/8c2f4f9d69d8"},
        {"title": "Data Analysis Using Python", "provider": "IBM", "link": "https://www.credly.com/badges/ef16ffb5-db3c-badges/linked_in_profile"},
        {"title": "Data Visualization Using Python", "provider": "IBM", "link": "https://www.credly.com/badges/a33539eb-e491-449c-8a12-6f1f925248ba/linked_in_profile"},
        {"title": "Applied Data Science", "provider": "IBM", "link": "https://www.credly.com/badges/7b399bf8-3691-4ede-b4a9-77cfa15fb325/linked_in_profile"},
        {"title": "Machine Learning with Python", "provider": "IBM", "link": "https://www.credly.com/badges/77aad513-7672-4d04-bfb8-39b37e55d986"},
        {"title": "Prompt Engineering", "provider": "IBM", "link": "https://courses.cognitiveclass.ai/certificates/e605bffd4da945149049fe4a2955efd4"},
        {"title": "Data Science Methodology", "provider": "IBM", "link": "https://www.credly.com/badges/70ae2196-2b81-4544-b703-16d7b09cdccb/linked_in_profile"},
        {"title": "Data Science Foundation", "provider": "IBM", "link": "https://www.credly.com/badges/ff7ceaf4-a2b6-4b41-a27e-ac1b361f060f/linked_in_profile"},
        {"title": "Intro To Generative AI", "provider": "Google", "link": "https://www.cloudskillsboost.google/public_profiles/c48c7f95-8155-458b-87af-46cb13ef6f95/badges/8493572?utm_medium=social&utm_source=linkedin&utm_campaign=ql-social-share"}
    ]

    col1, col2 = st.columns(2)
    for idx, cert in enumerate(certifications):
        cert_html = f"""
           <div class="card" style="margin-bottom: 20px;">
               <a href="{cert['link']}" target="_blank" style="text-decoration: none;">
                   <div class="card-body">
                       <h5 class="card-title">{cert['title']}</h5>
                       <p class="card-text">{cert['provider']}</p>
                   </div>
               </a>
           </div>
       """
        if idx % 2 == 0:
            with col1:
                st.markdown(cert_html, unsafe_allow_html=True)
        else:
            with col2:
                st.markdown(cert_html, unsafe_allow_html=True)

    st.markdown("""
       <style>
       .card {
           border: 1px solid #eaeaea;
           border-radius: 8px;
           transition: box-shadow 0.3s ease-in-out;
       }
       .card:hover {
           box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
       }
       .card-body {
           padding: 15px;
           background-color: #f9f9f9;
       }
       .card-title {
           font-size: 18px;
           margin-bottom: 8px;
           color: #333;
       }
       .card-text {
           font-size: 14px;
           color: #777;
       }
       </style>
       """, unsafe_allow_html=True)

# Contact section
def Contact():
    st.title("Contact Me")
    col1, col2 = st.columns(2)

    with col1:
        st.header("Address")
        st.markdown("""
            <div style="font-size: 16px;">
                93, Govindammal Nagar,<br>
                Seelanaickenpatty,<br>
                Salem - 636 201
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.header("Connect With Me")
        st.markdown("""
            <style>
            .contact-item {
                display: flex;
                align-items: center;
                margin-bottom: 10px;
                font-size: 18px;
            }
            .contact-item span {
                margin-right: 10px;
            }
            .contact-item a {
                text-decoration: none;
                color: #2E86C1;
            }
            </style>
            <div class="contact-item">
                <span>📧</span>
                <a href="mailto:krss132005@gmail.com">krss132005@gmail.com</a>
            </div>
            <div class="contact-item">
                <span>🐙</span>
                <a href="https://github.com/Kishankumar1328" target="_blank">GitHub: Kishankumar1328</a>
            </div>
            <div class="contact-item">
                <span>🔗</span>
                <a href="https://www.linkedin.com/in/kishan-kumar-suresh-kumar-037175259/" target="_blank">LinkedIn: Kishan Kumar</a>
            </div>
        """, unsafe_allow_html=True)

# Main function to build the app
def main():
    sidebar()
    About()
    Education()
    Projects()
    Skills()
    Certifications()
    Contact()

if __name__ == "__main__":
    main()
